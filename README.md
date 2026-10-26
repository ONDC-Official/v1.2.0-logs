# FREE11 Technologies Private Limited — ONDC Retail (RET10 v1.2.5) Buyer App log submission

| Field | Value |
|---|---|
| Entity | FREE11 Technologies Private Limited |
| Role | Buyer App (BAP) |
| Subscriber ID | `free11.com` |
| Subscriber URL | `https://free11.com/api/ondc` |
| Domain / Version | `ONDC:RET10` / `1.2.5` |
| Use case | Grocery |
| Environment | Pre-production |
| Testing tool | ONDC Protocol Workbench (Pramaan deprecated) |
| Workbench session ID | `i5IlDbMHGqt2fEgoIEQcAIEC_l-KDO0P` |
| Session run | 26-Oct-2026, 14:21–14:43 IST (08:51–09:13 UTC) — each flow run exactly once |
| Report | `Report_i5IlDbMHGqt2fEgoIEQcAIEC_l-KDO0P.html` (Workbench "Generate Report") |
| Raw logs | `i5IlDbMHGqt2fEgoIEQcAIEC_l-KDO0P-workbench-logs.json` (Workbench "Download logs", all 182 calls) |

## Folder structure

Every folder holds the raw request payload of each call in sequence (`NN_action.json`); `_sync_responses.json` lists, per call, the transaction_id, message_id, UTC timestamp, HTTP status and the synchronous ACK/NACK body.

| Folder | Workbench flow | Transaction ID | Calls |
|---|---|---|---|
| `Flow8A_Discovery_Full_Catalog` | Discovery_Flow_full_catalog | `d329a512-a110-4cef-a3b2-90e121210802` | search, on_search |
| `Flow8C_Discovery_Incremental_Catalog` | Discovery_Flow_incremental_catalog | `af32c632-4499-45af-ad3d-504f87021253` | search (start), on_search ×3, search (stop) |
| `Catalogue Rejection` | Catalog_Rejection_Flow | `f1c67fc3-7e54-4e08-b31f-373a8b39eac5` | search, on_search, catalog_rejection |
| `Flow1_Delivery_Prepaid` | Delivery_Flow | `df7ba272-a340-43cd-a0bc-9f8ffe7976e5` | select → on_confirm, on_status ×6, track, on_track |
| `Flow2_Buyer_Cancellation` | Cancellation_Flow | `aabc450b-dd89-4935-829a-e58072f46ea4` | select → on_confirm, cancel, on_cancel |
| `Flow005_Forced_Cancellation` | Forced_Cancellation_Flow | `2fb629bc-9bde-479b-9bdc-ff17bdf796bf` | select → on_confirm, on_status ×5, cancel (no), cancel (yes), on_cancel, update (settlement) |
| `Flow3_RTO_And_Part_Cancellation` | RTO_And_Part_Cancellation_Flow | `ad6ee588-6e90-4e75-9fd7-4850f754d7fd` | select → on_confirm, on_update (part cancel), update, on_status ×4, on_cancel (RTO), update, on_status |
| `Flow4_Return` | Return_Flow | `964fd17b-878c-4045-ab43-178a33c594b1` | select → on_confirm, on_status ×6, update (return), on_update ×3, update (settlement), on_update |
| `Flow5_Out_Of_Stock` | Out_Of_Stock_Flow | `25dce0ad-e303-4e50-8340-fbd1e149ee4c` | select, on_select (OOS), select (re-select), on_select → on_confirm, on_status ×6, track, on_track |
| `Flow5B_Out_Of_Stock_Error_Code` | Out_Of_Stock_Flow(Error-code) | `472992a8-a7a5-4979-adce-32451a0a3b40` | select, on_select (error 40002) |
| `IGM/IGM_v1.0.0_Delivery` | Delivery_Flow_With_IGM(v-1.0.0) | `ac517d84-0bf8-4d40-9e8c-6f67800c49a9` | order flow + issue, on_issue, on_issue_status, issue (close) |
| `IGM/IGM_v2.0.0_Delivery` | Delivery_Flow_With_IGM(v-2.0.0) | `0666324c-c937-4f41-a9a9-061fa375c048` | order flow + issue/on_issue cycle to resolution, on_update |
| `IGM/IGM_v2.0.0_No_Action` | Delivery_Flow_With_IGM_No_Action(v-2.0.0) | `3ef8d245-e35a-4590-9392-164cba1fdece` | order flow + issue/on_issue, BAP silent until BPP closes |
| `IGM/IGM_v2.0.0_Rejection` | Delivery_Flow_With_IGM_Rejection(v-2.0.0) | `51923ae0-2d1e-4604-9593-1aababe46fff` | order flow + issue/on_issue rejection cycle, on_update |

RSF: not applicable — FREE11 is a buyer app; no RSF APIs are enabled.

## Report notes for the reviewer

All BAP request validations in the Workbench report pass (search ×2, select/init/confirm ×6 flows, cancel ×3, track, update ×5 variants, all sync-response checks). Two items are flagged in the report but are Workbench template behaviour, not BAP payloads:

1. **Flow 1A `rating` / `on_rating`** — the Workbench Delivery_Flow for RET10 1.2.5 has no rating step, so the report validates an empty `{}` payload.
2. **Flow 8C `on_search` "sync response should exist"** — the incremental-catalog mock emits an `on_search` whose message_id the report cannot pair with a BAP sync response.

The remaining failures in the report are under `on_* request verification` and originate from the Workbench mock seller's own payloads.

Contact: Abhishek — Workbench login `Abhishek-free11`.
