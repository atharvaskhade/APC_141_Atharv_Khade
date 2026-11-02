import os
import re
import sqlite3
from statistics import median
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "autowise-secret-key-2025"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Database Paths ──
CAR_DB     = os.path.join(BASE_DIR, "india_current_cars.db")
HISTORY_DB = os.path.join(BASE_DIR, "history.db")


# ── Database Helpers ──

def connect_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def create_history_table():
    with connect_db(HISTORY_DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS searches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_name TEXT,
                car_price REAL,
                fuel_type TEXT,
                annual_km REAL,
                mileage REAL,
                fuel_price REAL,
                fuel_cost REAL DEFAULT 0,
                insurance REAL DEFAULT 0,
                servicing REAL DEFAULT 0,
                puc REAL DEFAULT 300,
                tyre_replacement REAL DEFAULT 0,
                repairs REAL DEFAULT 0,
                total_cost REAL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


# ── Car Data Helpers ──

def get_cars():
    """Return all unique brand+model combos from the car database."""
    with connect_db(CAR_DB) as conn:
        rows = conn.execute("""
            SELECT
                Make               AS brand,
                Model              AS model,
                Variant            AS variant,
                "Ex-Showroom_Price" AS price,
                Fuel_Type          AS fuel_type,
                ARAI_Certified_Mileage AS mileage,
                Electric_Range     AS electric_range
            FROM cars
            WHERE Make IS NOT NULL
              AND Model IS NOT NULL
            ORDER BY Make, Model, Variant
        """).fetchall()

    cars = []
    for row in rows:
        car = dict(row)
        cars.append(car)

    return cars


def get_variants(brand, model):
    """Return all variants for a given brand + model."""
    with connect_db(CAR_DB) as conn:
        rows = conn.execute("""
            SELECT Variant AS variant,
                   "Ex-Showroom_Price" AS price,
                   Fuel_Type AS fuel_type,
                   ARAI_Certified_Mileage AS mileage,
                   City_Mileage AS city_mileage,
                   Highway_Mileage AS highway_mileage,
                   Displacement AS displacement,
                   Body_Type AS body_type
            FROM cars
            WHERE Make = ? AND Model = ?
            ORDER BY Variant
        """, (brand, model)).fetchall()
    return [dict(r) for r in rows]


def get_car_details(brand, model, variant=None):
    with connect_db(CAR_DB) as conn:
        if variant:
            row = conn.execute("""
                SELECT Make, Model, Variant,
                       "Ex-Showroom_Price",
                       Fuel_Type,
                       ARAI_Certified_Mileage,
                       City_Mileage,
                       Highway_Mileage,
                       Displacement,
                       Body_Type,
                       Electric_Range,
                       "Front_Tyre_&_Rim",
                       "Rear_Tyre_&_Rim",
                       Wheels_Size
                FROM cars
                WHERE Make = ? AND Model = ? AND Variant = ?
                LIMIT 1
            """, (brand, model, variant)).fetchone()
        else:
            row = conn.execute("""
                SELECT Make, Model, Variant,
                       "Ex-Showroom_Price",
                       Fuel_Type,
                       ARAI_Certified_Mileage,
                       City_Mileage,
                       Highway_Mileage,
                       Displacement,
                       Body_Type,
                       Electric_Range,
                       "Front_Tyre_&_Rim",
                       "Rear_Tyre_&_Rim",
                       Wheels_Size
                FROM cars
                WHERE Make = ? AND Model = ?
                ORDER BY Variant
                LIMIT 1
            """, (brand, model)).fetchone()

    return dict(row) if row else None


def parse_price(value):
    """Convert strings like 'Rs. 3,53,290' to a float of rupees."""
    if value is None:
        return 0
    digits = re.sub(r"[^\d]", "", str(value))
    return float(digits) if digits else 0


def get_mileage(value):
    """Extract numeric km/l from strings like '25.17 km/litre'."""
    if not value:
        return 0
    match = re.search(r"\d+(?:\.\d+)?", str(value))
    return float(match.group()) if match else 0


def get_estimated_mileage(car):
    mileage = get_mileage(car.get("ARAI_Certified_Mileage"))
    if mileage > 0:
        return mileage, False

    alternate_mileages = [
        get_mileage(car.get("City_Mileage")),
        get_mileage(car.get("Highway_Mileage")),
    ]
    alternate_mileages = [value for value in alternate_mileages if value > 0]
    if alternate_mileages:
        return sum(alternate_mileages) / len(alternate_mileages), True

    comparable_mileages = []
    for variant in get_variants(car["Make"], car["Model"]):
        if (variant["fuel_type"] or "").strip().lower() != (car["Fuel_Type"] or "").strip().lower():
            continue

        variant_mileage = get_mileage(variant["mileage"])
        if variant_mileage <= 0:
            alternate = [
                get_mileage(variant["city_mileage"]),
                get_mileage(variant["highway_mileage"]),
            ]
            alternate = [value for value in alternate if value > 0]
            if alternate:
                variant_mileage = sum(alternate) / len(alternate)
        if variant_mileage > 0:
            comparable_mileages.append(variant_mileage)

    if comparable_mileages:
        return sum(comparable_mileages) / len(comparable_mileages), True

    fuel_type = (car.get("Fuel_Type") or "").strip().lower()
    if not fuel_type or "electric" in fuel_type or fuel_type == "ev":
        return 0, False

    fuel_class = "cng" if "cng" in fuel_type else fuel_type
    displacement_match = re.search(r"\d+(?:\.\d+)?", str(car.get("Displacement") or ""))
    displacement = float(displacement_match.group()) if displacement_match else None
    body_type = (car.get("Body_Type") or "").strip().lower()
    body_peer_mileages = []
    displacement_peer_mileages = []

    with connect_db(CAR_DB) as conn:
        peers = conn.execute("""
            SELECT Fuel_Type AS fuel_type,
                   Displacement AS displacement,
                   Body_Type AS body_type,
                   ARAI_Certified_Mileage AS mileage,
                   City_Mileage AS city_mileage,
                   Highway_Mileage AS highway_mileage
            FROM cars
            WHERE Make != ? OR Model != ?
        """, (car["Make"], car["Model"])).fetchall()

    for peer in peers:
        peer_fuel = (peer["fuel_type"] or "").strip().lower()
        peer_fuel_class = "cng" if "cng" in peer_fuel else peer_fuel
        if peer_fuel_class != fuel_class:
            continue

        peer_displacement_match = re.search(r"\d+(?:\.\d+)?", str(peer["displacement"] or ""))
        if displacement_match and peer_displacement_match:
            peer_displacement = float(peer_displacement_match.group())
            if abs(peer_displacement - displacement) > max(500, displacement * 0.35):
                continue

        peer_mileage = get_mileage(peer["mileage"])
        if peer_mileage <= 0:
            peer_alternates = [
                get_mileage(peer["city_mileage"]),
                get_mileage(peer["highway_mileage"]),
            ]
            peer_alternates = [value for value in peer_alternates if value > 0]
            if peer_alternates:
                peer_mileage = sum(peer_alternates) / len(peer_alternates)
        if peer_mileage > 0:
            displacement_peer_mileages.append(peer_mileage)
            peer_body_type = (peer["body_type"] or "").strip().lower()
            if body_type and peer_body_type == body_type:
                body_peer_mileages.append(peer_mileage)

    peer_mileages = body_peer_mileages or displacement_peer_mileages
    if peer_mileages:
        return median(peer_mileages), True

    return 0, False


def get_tyre_size(front, rear, wheels):
    """Extract tyre width, aspect ratio, and rim diameter from car specifications."""
    specs = [str(value) for value in (front, rear, wheels) if value]
    size_pattern = re.compile(
        r"(?P<width>\d{3})\s*/\s*(?P<aspect>\d{2,3})"
        r"(?:\s*/\s*|\s*Z?R\s*)(?P<rim>1[3-9]|2[0-2])\b",
        re.IGNORECASE,
    )

    for spec in specs:
        match = size_pattern.search(spec)
        if match:
            return tuple(int(match.group(key)) for key in ("width", "aspect", "rim"))

    partial_pattern = re.compile(r"(?P<width>\d{3})\s*/\s*(?P<aspect>\d{2,3})")
    width_rim_pattern = re.compile(
        r"(?P<width>\d{3})\s*R\s*(?P<rim>1[3-9]|2[0-2])\b",
        re.IGNORECASE,
    )
    rim_pattern = re.compile(
        r"(?:R\s*|/)(?P<rim>1[3-9]|2[0-2])\b|^\s*(?P<bare_rim>1[3-9]|2[0-2])\s*$",
        re.IGNORECASE,
    )
    partial = None
    rim = None
    width_rim = None
    for spec in specs:
        if partial is None:
            partial = partial_pattern.search(spec)
        if rim is None:
            rim = rim_pattern.search(spec)
        if width_rim is None:
            width_rim = width_rim_pattern.search(spec)
    default_aspect_by_rim = {
        13: 70, 14: 65, 15: 65, 16: 60, 17: 60,
        18: 55, 19: 55, 20: 50, 21: 45, 22: 40,
    }

    if partial and rim:
        return int(partial.group("width")), int(partial.group("aspect")), int(rim.group("rim"))

    if width_rim:
        rim_diameter = int(width_rim.group("rim"))
        return int(width_rim.group("width")), default_aspect_by_rim[rim_diameter], rim_diameter

    if rim:
        rim_diameter = int(rim.group("rim") or rim.group("bare_rim"))
        default_width_by_rim = {
            13: 155, 14: 175, 15: 185, 16: 205, 17: 215,
            18: 235, 19: 255, 20: 265, 21: 285, 22: 295,
        }
        return default_width_by_rim[rim_diameter], default_aspect_by_rim[rim_diameter], rim_diameter

    return None


ANNUAL_MAINTENANCE_BASELINE_KM = 10_000
TYRE_REPLACEMENT_INTERVAL_KM = 40_000


def estimate_usage_based_costs(car_price, annual_km):
    """Estimate service and repair costs in proportion to annual distance."""
    usage_factor = annual_km / ANNUAL_MAINTENANCE_BASELINE_KM
    servicing = car_price * 0.01 * usage_factor
    repairs = car_price * 0.005 * usage_factor
    return round(servicing, 2), round(repairs, 2)


def estimate_tyre_replacement(annual_km, car):
    if annual_km < TYRE_REPLACEMENT_INTERVAL_KM:
        return 0

    tyre_size = get_tyre_size(
        car["Front_Tyre_&_Rim"],
        car["Rear_Tyre_&_Rim"],
        car["Wheels_Size"],
    )
    if not tyre_size:
        known_model_sizes = {
            ("Mg", "Hector"): (215, 60, 17),
            ("Bmw", "X7"): (285, 45, 21),
        }
        tyre_size = known_model_sizes.get((car["Make"], car["Model"]))

    if not tyre_size:
        raise ValueError(f"Tyre size is unavailable for {car['Make']} {car['Model']}.")

    width, aspect, rim = tyre_size
    base_price_by_rim = {
        13: 2500,
        14: 3400,
        15: 4500,
        16: 6000,
        17: 7500,
        18: 9500,
        19: 12500,
        20: 15000,
        21: 18000,
        22: 22000,
    }
    tyre_price = (
        base_price_by_rim[rim]
        + round((width - 195) / 10) * 200
        + max(0, (55 - aspect) // 10) * 300
    )
    tyre_set_cost = tyre_price * 4
    return round((annual_km / TYRE_REPLACEMENT_INTERVAL_KM) * tyre_set_cost, 2)


def save_history(data):
    with connect_db(HISTORY_DB) as conn:
        conn.execute("""
            INSERT INTO searches (
                car_name, car_price, fuel_type, annual_km,
                mileage, fuel_price, fuel_cost, insurance,
                servicing, puc, tyre_replacement, repairs,
                total_cost
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["car_name"],
            data["car_price"],
            data["fuel_type"],
            data["annual_km"],
            data["mileage"],
            data["fuel_price"],
            data["fuel_cost"],
            data["insurance"],
            data["servicing"],
            data["puc"],
            data["tyre_replacement"],
            data["repairs"],
            data["total_cost"]
        ))


# ── Routes ──

@app.route("/")
def index():
    try:
        create_history_table()
        cars = get_cars()
        return render_template("index.html", cars=cars)
    except sqlite3.Error as err:
        return f"Database error: {err}", 500


@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        create_history_table()

        brand   = request.form.get("brand",   "").strip()
        model   = request.form.get("model",   "").strip()
        variant = request.form.get("variant", "").strip()

        annual_km_raw  = request.form.get("annual_km",  "0").strip()
        fuel_price_raw = request.form.get("fuel_price", "0").strip()

        # Basic validation
        if not brand or not model:
            flash("Please search for and select a car from the list.")
            return redirect(url_for("index"))

        try:
            annual_km  = float(annual_km_raw)
            fuel_price = float(fuel_price_raw)
        except ValueError:
            flash("Please enter valid numbers for kilometres and fuel price.")
            return redirect(url_for("index"))

        if annual_km <= 0:
            flash("Annual kilometres must be greater than zero.")
            return redirect(url_for("index"))

        if fuel_price <= 0:
            flash("Fuel price must be greater than zero.")
            return redirect(url_for("index"))

        # Look up car
        car = get_car_details(brand, model, variant or None)

        if not car:
            flash("Car not found in the database. Please try a different selection.")
            return redirect(url_for("index"))

        car_price  = parse_price(car["Ex-Showroom_Price"])
        fuel_type  = str(car["Fuel_Type"] or "").strip()
        mileage, mileage_is_estimated = get_estimated_mileage(car)

        # EV notice
        if "electric" in fuel_type.lower() or fuel_type.lower() == "ev":
            flash("Electric vehicles require electricity cost per km — coming soon!")
            return redirect(url_for("index"))

        if mileage <= 0:
            flash("Mileage data is unavailable for this variant. Please choose another variant.")
            return redirect(url_for("index"))

        # ── Cost Calculations ──
        fuel_cost        = (annual_km / mileage) * fuel_price
        insurance        = car_price * 0.03              # ~3% of ex-showroom price
        servicing, repairs = estimate_usage_based_costs(car_price, annual_km)
        puc              = 300                           # PUC annual cost (INR)

        try:
            tyre_replacement = estimate_tyre_replacement(annual_km, car)
        except ValueError as error:
            flash(str(error))
            return redirect(url_for("index"))

        total_cost = fuel_cost + insurance + servicing + puc + tyre_replacement + repairs

        car_name_parts = [car.get("Make", brand), car.get("Model", model)]
        car_variant    = car.get("Variant", "") or variant
        if car_variant:
            car_name_parts.append(car_variant)
        car_name = " ".join(car_name_parts).strip()

        result = {
            "car_name":        car_name,
            "car_price":       car_price,
            "fuel_type":       fuel_type,
            "annual_km":       annual_km,
            "mileage":         round(mileage, 2),
            "mileage_is_estimated": mileage_is_estimated,
            "fuel_price":      fuel_price,
            "fuel_cost":       round(fuel_cost, 2),
            "insurance":       round(insurance, 2),
            "servicing":       round(servicing, 2),
            "puc":             puc,
            "tyre_replacement": tyre_replacement,
            "tyre_replacement_applicable": annual_km >= TYRE_REPLACEMENT_INTERVAL_KM,
            "repairs":         round(repairs, 2),
            "total_cost":      round(total_cost, 2),
        }

        save_history(result)

        return render_template(
            "index.html",
            cars=get_cars(),
            result=result
        )

    except (ValueError, TypeError):
        flash("Please enter valid numeric values.")
        return redirect(url_for("index"))
    except sqlite3.Error as err:
        return f"Database error: {err}", 500


@app.route("/history")
def history():
    create_history_table()
    with connect_db(HISTORY_DB) as conn:
        searches = conn.execute("""
            SELECT * FROM searches
            ORDER BY id DESC
        """).fetchall()

    searches = [dict(row) for row in searches]
    for row in searches:
        if not row.get("tyre_replacement") and row.get("tyre"):
            row["tyre_replacement"] = row["tyre"]
        row["tyre_replacement_applicable"] = (
            (row.get("annual_km") or 0) >= TYRE_REPLACEMENT_INTERVAL_KM
        )

    return render_template(
        "history.html",
        searches=searches
    )


@app.route("/clear-history", methods=["POST"])
def clear_history():
    create_history_table()
    with connect_db(HISTORY_DB) as conn:
        conn.execute("DELETE FROM searches")
    flash("Calculation history cleared successfully.")
    return redirect(url_for("history"))


if __name__ == "__main__":
    create_history_table()
    app.run(debug=True)