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
    "timestamp": "2024-12-22T05:24:38.753Z",
    "message_id": "c0d90fa2-1f5d-41d7-8ede-bf2262fd61e9",
    "transaction_id": "e17287d4-4b4c-4745-bfc1-668584d5bd3b"
  },
  "message": {
    "settlement": {
      "id": "86b9e814-0ccc-4162-8744-f7244a80019c",
      "type": "NP-NP",
      "orders": [
        {
          "id": "ondcc6BHoMM7oGOdIS5ZQy0OI6q4TKM4",
          "self": {
            "amount": {
              "value": "29.849999999999998",
              "currency": "INR"
            },
            "status": "NOT_SETTLED",
            "reference_no": "1238683618634"
          },
          "provider": {
            "status": "SETTLED",
            "reference_no": "1238683618634"
          },
          "collector": {
            "amount": {
              "value": "29.849999999999998",
              "currency": "INR"
            }
          },
          "inter_participant": {
            "amount": {
              "value": "965.15",
              "currency": "INR"
            },
            "status": "NOT_SETTLED",
            "reference_no": "1238683618634",
            "settled_amount": {
              "value": "965.15",
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