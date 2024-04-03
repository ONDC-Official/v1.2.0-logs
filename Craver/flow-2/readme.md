# Flow - 2
## Seller - seller-app-preprod-v2.ondc.org
### Provider - Craver Restro

a. Buyer selects multiple items (> 1 qty for each item) for checkout (`select_1.json`)

b. Seller NP provides all fulfillment slots (different fulfillment types), some with tracking enabled (`on_select_1.json`)

c. Buyer selects different type or different slot for which tracking is enabled (`init_1.json`)

d. Seller NP accepts and proceeds to checkout (`on_init_1.json`)

e. Order is confirmed (`confirm_1.json` and `on_confirm_1.json`)

f. Buyer NP tracks live status of order (`status_1(Agent-assigned).json` and `on_status_1(Agent-assigned).json`)

g. Status updates for order until delivery (`on_status_1(Agent-assigned).json`, `on_status_2(Order-picked-up).json`, `on_status_3(Out-for-delivery).json`, `on_status_4(Order-delivered).json`)