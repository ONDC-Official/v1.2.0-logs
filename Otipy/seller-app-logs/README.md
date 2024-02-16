NP Type : Seller ISN
Domain: ONDC:RET10

Transactional test cases.


Initial Information: Our business model is next day morning delivery model, so anything you order till midnight (11:59 PM) will be delivered next day morning to your doorsteps.So delivery will be done next day.
We are only adding the "Fruits & Vegetables" catagory under grocery domain. We don't have customizable products and variants. So there will be plain vanilla products which user can pick and get them delivered next day.

Flow-1
1. Buyer App initiates a full catalog refresh
2. Seller responsd back with full catalog data.
3. Buyer app initiates a one time incremental refresh request
4. Seller app respond back with incremantal catalog data


Flow-2
When buyer browse the catalog of Otipy, will try to place the order.
1. User select products and hit checkout.
2. Seller app respond back with details.
3. User initializing the order placement by calling /init api.
4. Seller app respond with success via /on_init api.
5. Buyer app hits /confirm api
6. Seller app confirms the order placement with the items
7. Once Order is packed at ware-house, seller app sends unsolicited /on_status api with order state changes. (Fulfillment state : Order-picked-up)
8. Once order is sent to last mile logistics, seller app sends unsolicited /on_status api with order state changes. (Fulfillment state : Out-for-delivery)
9. When order is finally delivered, seller app sends unsolicited /on_status api with order state changes. (Fulfillment state : Order-delivered)



Flow-3
Buyer adds out of stock products and later remove from cart and place correct order
1. User select products and hit checkout.
2. Seller app respond back with details, if any of the items are out of stock.
3. User removes out of stock products from the cart and send back a fresh /select api with available products
4. Seller app respond back with details.
5. User initializing the order placement by calling /init api.
6. Seller app respond with success via /on_init api.
7. Buyer app hits /confirm api
8. Seller app confirms the order placement with the items
9. Once Order is packed at ware-house, seller app sends unsolicited /on_update api with order state changes. (Fulfillment state : Order-picked-up)
10. Once order is sent to last mile logistics, seller app sends unsolicited /on_status api with order state changes. (Fulfillment state : Out-for-delivery)
11. When order is finally delivered, seller app sends unsolicited /on_status api with order state changes. (Fulfillment state : Order-delivered)



Flow-4
Buyer NP cancel the order before pick up
1. User select products and hit checkout.
2. Seller app respond back with details.
3. User initializing the order placement by calling /init api.
4. Seller app respond with success via /on_init api.
5. Buyer app hits /confirm api
6. Seller app confirms the order placement with the items
7. Buyer app cancel the complete order.
8. Seller app initiates the complete cancellation of the order.



Flow-5
Seller NP Cancels the order due to unavailability of the buyer
1. User select products and hit checkout.
2. Seller app respond back with details, if any of the items are out of stock.
3. User initializing the order placement by calling /init api.
4. Seller app respond with success via /on_init api.
5. Buyer app hits /confirm api
6. Seller app confirms the order placement with the items
7. Once Order is packed at ware-house, seller app sends unsolicited /on_status api with order state changes. (Fulfillment state : Order-picked-up)
8. Once order is sent to last mile logistics, seller app sends unsolicited /on_status api with order state changes. (Fulfillment state : Out-for-delivery)
9. At the delivery location, buyer was not available, so delivery boy cancels the order and send unsolicitated on_state to the buyer (Fulfilment : RTO-Disposed).


Flow-6
Seller NP Cancels the order due to unavailability of the buyer
1. User select products and hit checkout.
2. Seller app respond back with details via /on_select api
3. User initializing the order placement by calling /init api.
4. Seller app respond with success via /on_init api.
5. Buyer app hits /confirm api
6. Seller app confirms the order placement with the items
7. At ware-house, one of the item was not available at seller, so seller cancels that item from the order and remaining items are packed. So seller app sends unsolicited /on_update api with order state changes. (Forward Fulfillment state : Pending, cancel fulfillment state : Cancelled)
8. Once order is sent to last mile logistics, seller app sends unsolicited /on_status api with order state changes. (Forward Fulfillment state : Out-for-delivery, cancel fulfillment state : Cancelled)
9. When order is finally delivered, seller app sends unsolicited /on_status api with order state changes. (Forward Fulfillment state : Delivered, cancel fulfillment state : Cancelled)
10. Buyer returns an item for the quality issue, so send /update api with return request.
11. Seller sends /on_update with with the fulfillment  "Return-initiated".
12. Seller approves the return request but doesn't want the product back, so send unsolicitated /on_update request to the buyer app (fulfillment state : liquidated)
# As fruits & vegetables are not considered for RTO return pickup. So return pick requests are not eligible for it.

