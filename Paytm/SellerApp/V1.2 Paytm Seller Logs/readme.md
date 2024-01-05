1. For Cancel Flow:
Currently we as a Paytm seller will live with F&B category only so user cancellation is not supported. If some buyer sends us cancel request then will NACK it.
All our products are F&B and "@ondc/org/cancellable": false in on_search payload

2. For Return Flow
Currently we as a Paytm seller will live with F&B category only so return is not supported.

3. since this is due to reason "011", why isn't /cancel from buyer app included in logs?
As discussed with Supriyo, this is fine for now

