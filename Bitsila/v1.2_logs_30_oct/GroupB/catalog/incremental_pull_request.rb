{
    "context": {
        "ttl": "PT30S",
        "city": "std:080",
        "action": "search",
        "bap_id": "shopping-api-testing.phonepe.com",
        "domain": "nic2004:52110",
        "bap_uri": "https://shopping-api-testing.phonepe.com/apis/ondcConnector/bpp/callback/v1",
        "country": "IND",
        "timestamp": "2023-10-30T10:04:36.213Z",
        "message_id": "SRCPULL2310301534360632665932",
        "core_version": "1.2.0",
        "transaction_id": "PULL2310301534360632665932"
    },
    "message": {
        "intent": {
            "tags": [
                {
                    "code": "catalog_inc",
                    "list": [
                        {
                            "code": "start_time",
                            "value": "2023-10-30T09:04:36.214168968Z"
                        },
                        {
                            "code": "end_time",
                            "value": "2023-10-30T10:04:36.214168968Z"
                        }
                    ]
                }
            ],
            "payment": {
                "@ondc/org/buyer_app_finder_fee_type": "percent",
                "@ondc/org/buyer_app_finder_fee_amount": "3"
            },
            "fulfillment": {
                "type": "Delivery and Self-Pickup"
            }
        }
    }
}