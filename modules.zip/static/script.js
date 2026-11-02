/* ============================================================
   AutoWise – Frontend Logic
   ============================================================
   Sections:
     1. Car Data & Autocomplete
     2. Variant Selector
     3. Form Validation & Submission UX
     4. Animated Progress Bars
     5. Flash Message Auto-dismiss
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    /* ──────────────────────────────────────────────
       1. CAR DATA & AUTOCOMPLETE
    ────────────────────────────────────────────── */

    const carsDataEl = document.getElementById('cars_data');
    if (!carsDataEl) return; // Not on the calculator page

    const ALL_CARS = JSON.parse(carsDataEl.textContent || '[]');

    const searchInput  = document.getElementById('car_search');
    const dropdown     = document.getElementById('car_dropdown');
    const noResults    = document.getElementById('no_results');
    const searchClear  = document.getElementById('search_clear');
    const selectedChip = document.getElementById('selected_chip');
    const chipText     = document.getElementById('selected_chip_text');
    const chipClear    = document.getElementById('chip_clear');
    const hidBrand     = document.getElementById('hid_brand');
    const hidModel     = document.getElementById('hid_model');
    const hidVariant   = document.getElementById('hid_variant');

    // Build deduplicated brand+model map
    const carMap = {};
    ALL_CARS.forEach(function (c) {
        const key = (c.brand || '') + '|||' + (c.model || '');
        if (!carMap[key]) {
            carMap[key] = {
                brand:     c.brand     || '',
                model:     c.model     || '',
                fuel_type: c.fuel_type || 'Petrol',
                variants:  []
            };
        }
        carMap[key].variants.push(c);
    });

    const CAR_ENTRIES = Object.values(carMap);

    /* ── Render dropdown ── */
    function renderDropdown(query) {
        const q = query.trim().toLowerCase();
        // Remove old car-option buttons
        dropdown.querySelectorAll('.car-option').forEach(function (el) { el.remove(); });

        let count  = 0;
        const MAX  = 80;

        for (let i = 0; i < CAR_ENTRIES.length && count < MAX; i++) {
            const entry = CAR_ENTRIES[i];
            const text  = (entry.brand + ' ' + entry.model).toLowerCase();
            if (q && !text.includes(q)) continue;

            const btn = document.createElement('button');
            btn.type      = 'button';
            btn.className = 'car-option';
            btn.setAttribute('role', 'option');
            btn.dataset.brand = entry.brand;
            btn.dataset.model = entry.model;

            const fuelClass = getFuelClass(entry.fuel_type);
            const varCount  = entry.variants.length;

            btn.innerHTML =
                '<div class="car-option-icon">🚗</div>' +
                '<div class="car-option-info">' +
                    '<div class="car-option-name">' + entry.brand + ' ' + entry.model + '</div>' +
                    '<div class="car-option-meta">' + varCount + ' variant' + (varCount !== 1 ? 's' : '') + '</div>' +
                '</div>' +
                '<span class="fuel-badge ' + fuelClass + '">' + entry.fuel_type + '</span>';

            btn.addEventListener('click', function () {
                selectCar(entry);
            });

            dropdown.insertBefore(btn, noResults);
            count++;
        }

        noResults.style.display = count === 0 ? 'block' : 'none';
        dropdown.classList.toggle('open', count > 0 || (q.length > 0 && count === 0));
    }

    function getFuelClass(fuel) {
        if (!fuel) return 'fuel-other';
        const f = fuel.toLowerCase();
        if (f.includes('petrol'))                   return 'fuel-petrol';
        if (f.includes('diesel'))                   return 'fuel-diesel';
        if (f.includes('cng'))                      return 'fuel-cng';
        if (f.includes('electric') || f === 'ev')   return 'fuel-electric';
        if (f.includes('hybrid'))                   return 'fuel-hybrid';
        return 'fuel-other';
    }

    /* ── Select a car ── */
    function selectCar(entry) {
        hidBrand.value   = entry.brand;
        hidModel.value   = entry.model;
        hidVariant.value = '';

        searchInput.value = entry.brand + ' ' + entry.model;
        searchClear.classList.add('visible');
        dropdown.classList.remove('open');

        chipText.textContent = entry.brand + ' ' + entry.model +
            ' — ' + entry.variants.length + ' variant(s)';
        selectedChip.classList.add('visible');

        renderVariants(entry.variants);
    }

    /* ── Input events ── */
    searchInput.addEventListener('input', function () {
        renderDropdown(this.value);
        searchClear.classList.toggle('visible', this.value.length > 0);
        if (!this.value) clearSelection();
    });

    searchInput.addEventListener('focus', function () {
        if (!hidBrand.value) renderDropdown(this.value);
    });

    searchInput.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') dropdown.classList.remove('open');
    });

    searchClear.addEventListener('click', clearSelection);
    chipClear.addEventListener('click',  clearSelection);

    function clearSelection() {
        searchInput.value  = '';
        hidBrand.value     = '';
        hidModel.value     = '';
        hidVariant.value   = '';
        searchClear.classList.remove('visible');
        selectedChip.classList.remove('visible');
        dropdown.classList.remove('open');
        const vs = document.getElementById('variant_section');
        const vg = document.getElementById('variant_grid');
        if (vs) vs.classList.remove('visible');
        if (vg) vg.innerHTML = '';
    }

    // Close on outside click
    document.addEventListener('click', function (e) {
        if (!dropdown.contains(e.target) && e.target !== searchInput) {
            dropdown.classList.remove('open');
        }
    });


    /* ──────────────────────────────────────────────
       2. VARIANT SELECTOR
    ────────────────────────────────────────────── */

    function renderVariants(variants) {
        const section = document.getElementById('variant_section');
        const grid    = document.getElementById('variant_grid');
        if (!section || !grid) return;

        grid.innerHTML = '';

        if (!variants || variants.length === 0) {
            section.classList.remove('visible');
            return;
        }

        variants.forEach(function (v) {
            const btn = document.createElement('button');
            btn.type          = 'button';
            btn.className     = 'variant-btn';
            btn.dataset.variant = v.variant || '';
            btn.title         = v.variant || 'Default';

            const priceStr = v.price   ? '₹' + formatPrice(v.price)   : '';
            const mileStr  = v.mileage ? formatMileage(v.mileage, v.fuel_type) : '';
            const meta     = [priceStr, mileStr].filter(Boolean).join(' · ');

            btn.innerHTML =
                '<div style="font-weight:600;font-size:12px;">' + (v.variant || 'Base') + '</div>' +
                (meta ? '<div style="font-size:10px;color:var(--text-muted);margin-top:2px;">' + meta + '</div>' : '');

            btn.addEventListener('click', function () {
                grid.querySelectorAll('.variant-btn').forEach(function (b) {
                    b.classList.remove('selected');
                });
                btn.classList.add('selected');
                hidVariant.value = v.variant || '';
            });

            grid.appendChild(btn);
        });

        // Auto-select first
        const first = grid.querySelector('.variant-btn');
        if (first) {
            first.classList.add('selected');
            hidVariant.value = first.dataset.variant;
        }

        section.classList.add('visible');
    }

    function formatPrice(raw) {
        if (!raw) return '';
        const digits = String(raw).replace(/[^\d]/g, '');
        if (!digits) return '';
        const num = parseInt(digits, 10);
        if (num >= 10000000) return (num / 10000000).toFixed(2) + ' Cr';
        if (num >= 100000)   return (num / 100000).toFixed(2)   + ' L';
        return num.toLocaleString('en-IN');
    }

    function formatMileage(raw, fuelType) {
        const value = String(raw).replace(/\s*km\s*\/\s*(?:litre|l|kg)\s*$/i, '').trim();
        const unit = /cng/i.test(fuelType || '') ? 'km/kg' : 'km/l';
        return value ? value + ' ' + unit : '';
    }


    /* ──────────────────────────────────────────────
       3. FORM VALIDATION & SUBMIT UX
    ────────────────────────────────────────────── */

    const form      = document.getElementById('costForm');
    const submitBtn = document.getElementById('submit-btn');
    const btnIcon   = document.getElementById('btn-icon');
    const btnText   = document.getElementById('btn-text');

    if (form) {
        form.addEventListener('submit', function (e) {
            // Must have selected a car
            if (!hidBrand.value || !hidModel.value) {
                e.preventDefault();
                shake(searchInput);
                searchInput.focus();
                return;
            }
            // Must have valid km & price
            const km    = parseFloat(document.getElementById('annual_km').value);
            const price = parseFloat(document.getElementById('fuel_price').value);
            if (!km || km <= 0) {
                e.preventDefault();
                shake(document.getElementById('annual_km'));
                return;
            }
            if (!price || price <= 0) {
                e.preventDefault();
                shake(document.getElementById('fuel_price'));
                return;
            }
            // Loading state
            submitBtn.disabled  = true;
            btnIcon.textContent = '⏳';
            btnText.textContent = 'Calculating…';
        });
    }

    function shake(el) {
        el.style.borderColor = '#ef4444';
        el.style.boxShadow   = '0 0 0 3px rgba(239,68,68,0.15)';
        el.animate([
            { transform: 'translateX(-4px)' },
            { transform: 'translateX(4px)' },
            { transform: 'translateX(-3px)' },
            { transform: 'translateX(3px)' },
            { transform: 'none' }
        ], { duration: 300, easing: 'ease' });
        setTimeout(function () {
            el.style.borderColor = '';
            el.style.boxShadow   = '';
        }, 2000);
    }


    /* ──────────────────────────────────────────────
       4. ANIMATED PROGRESS BARS
    ────────────────────────────────────────────── */

    const resultDataEl = document.getElementById('result_data');
    if (resultDataEl) {
        const data = JSON.parse(resultDataEl.textContent || '{}');
        renderBars(data);

        // Scroll result into view smoothly
        const panel = document.getElementById('result_panel');
        if (panel) {
            setTimeout(function () {
                panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 200);
        }
    }

    // Colors matching light theme icons
    const BAR_COLORS = [
        '#d97706',   // fuel      – amber
        '#2563eb',   // insurance – blue
        '#16a34a',   // servicing – green
        '#7c3aed',   // puc       – violet
        '#dc2626',   // tyres     – red
        '#0d9488',   // repairs   – teal
    ];

    const BAR_ITEMS = [
        { key: 'fuel_cost',        label: 'Fuel Cost' },
        { key: 'insurance',        label: 'Insurance' },
        { key: 'servicing',        label: 'Servicing' },
        { key: 'puc',              label: 'PUC' },
        { key: 'tyre_replacement', label: 'Tyre Replacement' },
        { key: 'repairs',          label: 'Repairs' },
    ];

    function renderBars(data) {
        const container = document.getElementById('bar_section');
        if (!container) return;

        const total = data.total_cost || 1;

        BAR_ITEMS.forEach(function (item, i) {
            if (item.key === 'tyre_replacement' && !data.tyre_replacement_applicable) return;

            const val   = data[item.key] || 0;
            const pct   = Math.min((val / total) * 100, 100);
            const color = BAR_COLORS[i];

            const row = document.createElement('div');
            row.className = 'bar-row';
            row.innerHTML =
                '<div class="bar-row-header">' +
                    '<span class="bar-row-label">' + item.label + '</span>' +
                    '<span class="bar-row-value">' +
                        '₹' + val.toLocaleString('en-IN', { maximumFractionDigits: 0 }) +
                        ' <span style="color:var(--text-muted);font-weight:400;">(' + pct.toFixed(1) + '%)</span>' +
                    '</span>' +
                '</div>' +
                '<div class="bar-track">' +
                    '<div class="bar-fill" style="background:' + color + '" data-pct="' + pct + '"></div>' +
                '</div>';

            container.appendChild(row);
        });

        // Animate after paint
        requestAnimationFrame(function () {
            setTimeout(function () {
                container.querySelectorAll('.bar-fill').forEach(function (el) {
                    el.style.width = el.dataset.pct + '%';
                });
            }, 100);
        });
    }


    /* ──────────────────────────────────────────────
       5. FLASH MESSAGE AUTO-DISMISS
    ────────────────────────────────────────────── */

    const flashContainer = document.getElementById('flash-container');
    if (flashContainer) {
        setTimeout(function () {
            flashContainer.style.transition = 'opacity 0.4s ease';
            flashContainer.style.opacity    = '0';
            setTimeout(function () { flashContainer.remove(); }, 400);
        }, 4500);
    }

});
