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
    "timestamp": "2024-12-13T11:17:52.882Z",
    "message_id": "7e2c4105-82eb-41c1-9f48-33a009e33967",
    "transaction_id": "7c1f6d4e-edba-4998-bb76-8fa5b5fb301a"
  },
  "message": {
    "settlement": {
      "id": "6e4df9f0-1ebc-48d1-9bcb-a5e8b5c5b60f",
      "type": "NP-NP",
      "orders": [
        {
          "id": "ondcwUWvVmeqByJYL6LEdga3me02ziJu",
          "self": {
            "amount": {
              "value": "3.0",
              "currency": "INR"
            },
            "status": "SETTLED",
            "reference_no": "1238683618634"
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
            "status": "SETTLED",
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