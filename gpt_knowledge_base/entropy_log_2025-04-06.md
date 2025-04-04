# Entropy Log – 2025-04-06

> Context: Picking Station  
> SOP: picking_station_v1.md  
> Agent: ShippingGPT  
> Logged By: ConductorGPT

---

## Event #001

- **event_type:** mis_pick
- **timestamp:** 2025-04-06T10:12:33Z
- **location:** Aisle 3B
- **operator_id:** JHUNT
- **resolution_status:** escalated
- **notes:** Operator picked SKU #8121 (syrup) instead of #8211 (spray) due to alias confusion on printed pick list.
- **root_cause_tag:** sku_alias_conflict

---

## Event #002

- **event_type:** bin_swap
- **timestamp:** 2025-04-06T10:35:09Z
- **location:** Packing Station Entry Rack
- **operator_id:** JHUNT
- **resolution_status:** unresolved
- **notes:** Bin labeled for Order #A273 was placed in rack location for Order #A275. No error detected until pack review.
- **root_cause_tag:** sop_gap

---

## ConductorGPT Observations

- SOP lacks barcode scanning at pick time.
- Printed pick list is static and error-prone.
- Bin validation step before pack handoff is not enforced.

→ Triggering SOP revision suggestion + chaos source expansion.
