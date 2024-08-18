# Flow 1

- On Search Full Catalog Refresh
- provider/item/price: item.price.value should be greater than 0
- category in serviceability construct should be one of the category ids in bpp/providers/items/category_id

# Flow 2

### Select

- LongGpsErr: fulfillments location.gps is not as per the API contract as there is an extra space(latitude, longitude) which should be (latitude,longitude)

### On Select

- priceErr: Warning: Quoted Price in /on_select INR 431 does not match with the total price of items in /select INR 200 i.e price for the item mismatch in on_search and on_select

### Init

- item_FFErr0: Item Id 652bc2f0c74738e1e91d26b0 does not exist in /on_select
- item_FFErr1: Item Id 64f37f1847c6e1683c9644d6 does not exist in /on_select

### On Init

- schemaErr0: /message/order/provider must have required property 'locations'

### Confirm

- schemaErr0: /message/order/id Should be alphanumeric upto 32 letters max
- tmpstmp: Timestamp for /on_init api cannot be greater than or equal to /confirm api
- item_FFErr0: Item Id 652bc2f0c74738e1e91d26b0 does not exist in /on_select
- item_FFErr1: Item Id 64f37f1847c6e1683c9644d6 does not exist in /on_select
- sttlmntdtls: payment settlement_details mismatch in /on_init & /confirm
- quoteErr0: Mismatch found for item with item_id 6596b1113affdbaf0d33ebb5 while comparing quote object of on_select and confirm
- quoteErr1: Mismatch found for item with item_id 6596b1113affdbaf0d33ebb4 while comparing quote object of on_select and confirm

### On Confirm

- schemaErr0: /context/timestamp must match format "date-time"
- timestamp_err: Timestamp should be in date-time format
- updtdtmstmp: order.updated_at timestamp should be updated as per the context.timestamp (since default fulfillment state is added)
- invldUpdtdTmstp: updated_at timestamp should be equal to context timestamp for /on_confirm
- quoteErr0: Mismatch found for item with item_id 6596b1113affdbaf0d33ebb5 while comparing quote object of on_confirm and confirm
- quoteErr1: Mismatch found for item with item_id 6596b1113affdbaf0d33ebb4 while comparing quote object of on_confirm and confirm
- pymntObj: payment object mismatches in /confirm & /on_confirm
- message/order/tags/bpp_terms/np_type: np_type is missing in message/order/tags/bpp_terms for ON_CONFIRM

### On Status Pending

- schemaErr0: /message/order/id Should be alphanumeric upto 32 letters max
- tmpstmp: Created At timestamp for /on_status_pending should be equal to context timestamp at confirm
- tmpstmp1: Timestamp for /on_confirm api cannot be greater than or equal to /on_status_pending api

### On Status Packed

- schemaErr0: /message/order/id Should be alphanumeric upto 32 letters max
- tmpstmp: Created At timestamp for /on_status_packed.message.order should be equal to context timestamp at confirm
- tmpstmp1: Timestamp for /on_confirm api cannot be greater than or equal to /on_status_packed api

### On Status Picked

- schemaErr0: /message/order/id Should be alphanumeric upto 32 letters max
- tmpstmp1: Timestamp for /on_confirm api cannot be greater than or equal to /on_status_picked api
- tmpstmp: Created At timestamp for /on_status_picked should be equal to context timestamp at confirm
- updatedAt: order/updated_at timestamp can't be less than the pickup time

### On Status Out For Delivery

- schemaErr0: /message/order/id Should be alphanumeric upto 32 letters max
- tmpstmp1: Timestamp for /on_confirm api cannot be greater than or equal to /on_status_out-for-delivery api
- tmpstmp: Created At timestamp for /on_status_out-for-delivery should be equal to context timestamp at confirm
- updatedAt: order/updated_at timestamp can't be less than the Out_for_delivery time

### On Status Delivered

- schemaErr0: /message/order/id Should be alphanumeric upto 32 letters max
- tmpstmp1: Timestamp for /on_confirm api cannot be greater than or equal to /on_status_delivered api
- tmpstmp: Created At timestamp for /on_status_delivered should be equal to context timestamp at confirm
- delPickTime: delivery timestamp (/end/time/timestamp) can't be less than or equal to the pickup timestamp (start/time/timestamp)
- updatedAt: order/updated_at timestamp can't be less than the delivery time

# Flow 3

- Only provided select and on_select calls

# Flow 6-a (Part cancel) and # Flow 6-b (Reverse QC) is missing
