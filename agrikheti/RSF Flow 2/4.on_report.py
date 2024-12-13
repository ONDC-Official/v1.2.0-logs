{
  "context": {
    "ttl": "PT10M",
    "action": "on_report",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "rsf-mock-service.ondc.org/seller_protocol_server",
    "domain": "ONDC:NTS10",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://rsf-mock-service.ondc.org/seller_protocol_server",
    "version": "2.0.0",
    "location": {
      "city": {
        "code": "*"
      },
      "country": {
        "code": "IND"
      }
    },
    "timestamp": "2024-12-13T12:17:42.089Z",
    "message_id": "e5c615b2-03e5-4e34-ad9b-79fdafba01a4",
    "transaction_id": "75425405-dd81-49ac-ba44-2099cbccf2df"
  },
  "message": {
    "settlement": {
      "id": "839bf2c0-2712-42fa-8698-5edb52125cbe",
      "type": "NP-NP",
      "orders": [
        {
          "id": "ondch3sBCVELRmLLBLGFJWUIVW81DqrS",
          "self": {
            "amount": {
              "value": "3.0",
              "currency": "INR"
            },
            "status": "NOT_SETTLED",
            "reference_no": "1238683618634"
          },
          "error": {
            "code": "70016"
          },
          "provider": {
            "status": "SETTLED",
            "reference_no": "1238683618634"
          },
          "collector": {
            "amount": {
              "value": "3.0",
              "currency": "INR"
            }
          },
          "inter_participant": {
            "amount": {
              "value": "351.0",
              "currency": "INR"
            },
            "status": "NOT_SETTLED",
            "reference_no": "1238683618634",
            "settled_amount": {
              "value": "351.0",
              "currency": "INR"
            }
          }
        }
      ]
    },
    "receiver_app_id": "pramaan.ondc.org/alpha/mock-server",
    "collector_app_id": "stage.agrikheti.com"
  }
}