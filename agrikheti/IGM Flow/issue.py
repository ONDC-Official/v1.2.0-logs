{
  "context": {
    "ttl": "PT30S",
    "city": "std:080",
    "action": "issue",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "pramaan.ondc.org/alpha/mock-server",
    "domain": "ONDC:RET11",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://pramaan.ondc.org/alpha/mock-server/seller",
    "country": "IND",
    "timestamp": "2024-12-13T11:06:04.386Z",
    "message_id": "cc8e509b-651f-4eaa-a3f6-7fbb1cbef608",
    "core_version": "1.2.0",
    "transaction_id": "aed484c0-3c66-4a58-86f5-ba218a9a98a9"
  },
  "message": {
    "issue": {
      "id": "d5511daa-3845-493d-afc6-71674140a91f",
      "source": {},
      "status": "OPEN",
      "category": "ITEM",
      "created_at": "2024-12-13T11:06:04.386Z",
      "issue_type": "ISSUE",
      "updated_at": "2024-12-13T11:06:04.386Z",
      "description": {
        "images": [
          "/downloads/crop_manuals/OIG3.u6ctnC12_1724393594.jpeg"
        ],
        "long_desc": "product quality is not correct. facing issues while using the product",
        "short_desc": "Issue with product quality",
        "additional_desc": {
          "url": "",
          "content_type": ""
        }
      },
      "sub_category": "ITM04",
      "issue_actions": {
        "complainant_actions": [
          {
            "short_desc": "Complaint created",
            "updated_at": "2024-12-13T11:06:04.386Z",
            "updated_by": {
              "org": {
                "name": "stage.agrikheti.com::ONDC:RET11"
              },
              "person": {
                "name": "John Doe"
              },
              "contact": {
                "email": "buyerapp@interface.com",
                "phone": "9450394039"
              }
            },
            "complainant_action": "OPEN"
          }
        ]
      },
      "order_details": {
        "id": "ondcLeitwn4u4bi9fuw5Q80ywRiXVNIh",
        "items": [
          {
            "id": "c8314c6d-8365-4f72-92f8-d89ec23291f1",
            "quantity": 1
          }
        ],
        "state": "Completed",
        "provider_id": "pramaan.ondc.org/alpha/mock-server",
        "fulfillments": []
      },
      "complainant_info": {
        "person": {
          "name": "NAINA SINGLA"
        },
        "contact": {
          "phone": "7814830896"
        }
      },
      "expected_response_time": {
        "duration": ""
      },
      "expected_resolution_time": {
        "duration": ""
      }
    }
  }
}