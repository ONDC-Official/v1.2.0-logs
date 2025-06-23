{
    "context": {
        "ttl": "PT30S",
        "city": "std:080",
        "action": "on_search",
        "bap_id": "shopping-api-testing.phonepe.com",
        "domain": "nic2004:52110",
        "bap_uri": "https://shopping-api-testing.phonepe.com/apis/ondcConnector/bpp/callback/v1",
        "country": "IND",
        "timestamp": "2023-10-30T10:05:56.651Z",
        "message_id": "SRCPULL2310301534360632665932",
        "core_version": "1.2.0",
        "transaction_id": "PULL2310301534360632665932",
        "bpp_id": "biz.test.bitsila.com",
        "bpp_uri": "https://biz.test.bitsila.com/ecc/ondc/retail-bpp"
    },
    "message": {
      "catalog": {
        "bpp/providers": [
          {
            "id": "1016:1548",
            "items": [
                {
                    "id": "1254064",
                    "time": {
                        "label": "enable",
                        "timestamp": "2023-10-30T09:25:56.637Z"
                    },
                    "descriptor": {
                        "name": "apple cake NC stock type 1 kg",
                        "code": "5:BTSCCCnplouwmAVm",
                        "symbol": "https://enstore-test.sgp1.digitaloceanspaces.com/1016/item-1254064-RI2YwQfwPq.png",
                        "short_desc": null,
                        "long_desc": null,
                        "images": [
                            "https://enstore-test.sgp1.digitaloceanspaces.com/1016/item-1254064-RI2YwQfwPq.png"
                        ]
                    },
                    "quantity": {
                        "unitized": {
                            "measure": {
                                "unit": "kg",
                                "value": "1"
                            }
                        },
                        "available": {
                            "count": "180"
                        },
                        "maximum": {
                            "count": "24"
                        }
                    },
                    "price": {
                        "currency": "INR",
                        "value": "500",
                        "maximum_value": "500"
                    },
                    "category_id": "F\u0026B",
                    "fulfillment_id": "1",
                    "location_id": "L:1016:1548",
                    "@ondc/org/returnable": false,
                    "@ondc/org/cancellable": true,
                    "@ondc/org/return_window": "PT3H",
                    "@ondc/org/seller_pickup_return": true,
                    "@ondc/org/time_to_ship": "PT1H",
                    "@ondc/org/available_on_cod": false,
                    "@ondc/org/contact_details_consumer_care": "8745784512",
                    "tags": [
                        {
                            "code": "origin",
                            "list": [
                                {
                                    "code": "country",
                                    "value": "IND"
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "1195607",
                    "time": {
                        "label": "enable",
                        "timestamp": "2023-10-30T09:37:56.647Z"
                    },
                    "descriptor": {
                        "name": "Pizza NC 1 qty",
                        "code": "5:BTSF7OaxgJkaE663",
                        "symbol": "https://enstore-test.sgp1.digitaloceanspaces.com/1016/item-1195607-LLLdHnuGdd.png",
                        "short_desc": null,
                        "long_desc": null,
                        "images": [
                            "https://enstore-test.sgp1.digitaloceanspaces.com/1016/item-1195607-LLLdHnuGdd.png"
                        ]
                    },
                    "quantity": {
                        "unitized": {
                            "measure": {
                                "unit": "qty",
                                "value": "1"
                            }
                        },
                        "available": {
                            "count": "500"
                        },
                        "maximum": {
                            "count": "24"
                        }
                    },
                    "price": {
                        "currency": "INR",
                        "value": "50",
                        "maximum_value": "50"
                    },
                    "category_id": "F\u0026B",
                    "fulfillment_id": "1",
                    "location_id": "L:1016:1548",
                    "@ondc/org/returnable": false,
                    "@ondc/org/cancellable": true,
                    "@ondc/org/return_window": "PT3H",
                    "@ondc/org/seller_pickup_return": true,
                    "@ondc/org/time_to_ship": "PT1H",
                    "@ondc/org/available_on_cod": false,
                    "@ondc/org/contact_details_consumer_care": "8745784512",
                    "tags": [
                        {
                            "code": "origin",
                            "list": [
                                {
                                    "code": "country",
                                    "value": "IND"
                                }
                            ]
                        }
                    ]
                }
            ]
          }
        ]
      }
    }
}