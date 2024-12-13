{
  "context": {
    "ttl": "PT10M",
    "action": "on_settle",
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
    "timestamp": "2024-12-13T11:20:30.457Z",
    "message_id": "76b021a1-e7ab-49ed-92ab-14517ea22685",
    "transaction_id": "bc6483c6-a770-4e6b-877c-3d0684359096"
  },
  "message": {
    "settlement": {
      "id": "c8c900d9-c373-472a-a105-a30efff89363",
      "type": "MISC",
      "orders": [
        {
          "self": {
            "amount": {
              "value": "55",
              "currency": "INR"
            },
            "status": "SETTLED",
            "reference_no": "1238683618634"
          }
        }
      ]
    }
  }
}