import sqlite3

DATABASE = "autowise.db"

def get_connection():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    con = get_connection()

    con.execute("""
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_name TEXT,
            car_price REAL,
            fuel_type TEXT,
            annual_km REAL,
            mileage REAL,
            fuel_price REAL,
            fuel_cost REAL,
            insurance REAL,
            servicing REAL,
            puc REAL,
            tyre_replacement REAL,
            repairs REAL,
            total_cost REAL,
            searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    con.commit()
    con.close()

def save_search(name, price, fuel, km, mileage, fuel_price,
                fuel_cost, insurance, servicing, puc,
                tyre, repairs, total):

    con = get_connection()

    con.execute("""
        INSERT INTO searches
        (car_name, car_price, fuel_type, annual_km, mileage, fuel_price,
         fuel_cost, insurance, servicing, puc,
         tyre_replacement, repairs, total_cost)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name, price, fuel, km, mileage, fuel_price,
        fuel_cost, insurance, servicing, puc,
        tyre, repairs, total
    ))

    con.commit()
    con.close()

def get_history():
    con = get_connection()
    rows = con.execute(
        "SELECT * FROM searches ORDER BY id DESC"
    ).fetchall()
    con.close()
    return [dict(row) for row in rows]

def clear_history():
    con = get_connection()
    con.execute("DELETE FROM searches")
    con.commit()
    con.close()