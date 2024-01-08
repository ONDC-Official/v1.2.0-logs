# Flow - 2
## Seller - ondc.uengage.in
### Provider - ondc-testing-outlet2

a. Buyer selects multiple items (> 1 qty for each item) for checkout (select.json)

b. Seller NP provides all fulfillment slots (different fulfillment types), some with tracking enabled (on_select.json)

c. Buyer selects different type or different slot for which tracking is enabled (init.json)

d. Seller NP accepts and proceeds to checkout (on_init.json)

e. Order is confirmed (confirm.json and on_confirm.json)

f. Buyer NP tracks live status of order (status_0.json, on_status_0(pending).json, track_0.json, on_track_0.json)

g. Status updates for order until delivery

### ⚠️ Couldn't update the order's status due to not having access to seller's app.