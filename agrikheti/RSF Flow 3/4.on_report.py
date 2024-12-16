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
    "timestamp": "2024-12-15T03:45:54.310Z",
    "message_id": "4ecadea2-6c46-4ef4-99ac-a062bd15e124",
    "transaction_id": "bc5fe83b-35fb-4bf1-96ed-02ee3d900360"
  },
  "message": {
    "settlement": {
      "id": "024acbd4-f58a-4625-9a33-80debaad0caa",
      "type": "NP-NP",
      "orders": [
        {
          "id": "ondcNVqdzjsc19Upeh3S0T0Zk2hywEJQ",
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
              "value": "49982.0",
              "currency": "INR"
            },
            "status": "NOT_SETTLED",
            "reference_no": "1238683618634",
            "settled_amount": {
              "value": "49982.0",
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