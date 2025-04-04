# SOP: Picking Station – V2

**Purpose:**  
Ensure accurate, verifiable item selection using real-time pick lists and scanner validation.

---

## Procedure

1. **Digital Pick List Access**
   - Retrieve digital pick list from ERP on tablet or terminal.
   - Confirm timestamp is within last 5 minutes before beginning.

2. **Barcode-Verified Picking**
   - Scan each picked item before placing in bin.
   - If mismatch occurs, remove item and retry.
   - All failed scans must be logged with SKU and time.

3. **Bin Assignment**
   - Use pre-labeled bins with unique barcode per order.
   - Scanner must verify bin ID matches order before bin leaves the station.

4. **Escalation Path**
   - Any scan mismatch, missing item, or SKU conflict must be flagged via on-screen button and logged as a chaos event.

---

## Versioning

- v2  
- Author: ShippingGPT_Developer  
- Reviewed By: ConductorGPT  
- Date: 2025-04-06

---

## SOP Alignment

- Resolves:
  - `mis_pick`
  - `bin_swap`
  - `sku_alias_conflict`

- Related Standard: `inventory_accuracy.md` *(draft planned)*
