# SOP: Picking Station – V1

**Purpose:**  
Ensure accurate picking of order items from inventory shelves, using pick lists and barcode verification.

---

## Procedure

1. Retrieve printed pick list from staging printer.
2. Locate items by SKU and quantity in warehouse aisles.
3. Place picked items into blue bins labeled by order ID.
4. Cross-check each item against the printed list.
5. Move completed bins to packing station rack.

---

## Known Weaknesses

- No digital tracking or real-time scan verification.
- Printed pick lists can be out of sync with live inventory.
- No barcode scanner requirement—manual matching prone to error.
- Operator judgment used for bin accuracy without escalation path.

---

## Alignment

- Reference Standard: `inventory_accuracy.md` *(not yet written)*
- Chaos Sources Exposed:
  - `mis_pick`
  - `missing_item`
  - `bin_swap`
  - `sku_alias_conflict`

---

## Version

- v1  
- Author: ShippingGPT_Developer  
- Date: 2025-04-06
