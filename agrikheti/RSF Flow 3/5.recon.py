{
  "context": {
    "ttl": "P1D",
    "action": "recon",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "pramaan.ondc.org/alpha/mock-server",
    "domain": "ONDC:NTS10",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://pramaan.ondc.org/alpha/mock-server/seller",
    "version": "2.0.0",
    "location": {
      "city": {
        "code": "*"
      },
      "country": {
        "code": "IND"
      }
    },
    "timestamp": "2024-12-15T03:47:15.828Z",
    "message_id": "29eabebf-2f83-488a-9021-3c02cf0dd4ec",
    "transaction_id": "bc5fe83b-35fb-4bf1-96ed-02ee3d900360"
  },
  "message": {
    "orders": [
      {
        "id": "ondcNVqdzjsc19Upeh3S0T0Zk2hywEJQ",
        "amount": {
          "value": "49996.0",
          "currency": "INR"
        },
        "settlements": [
          {
            "id": "4587d2ed-732b-42c5-b831-99924d8d1848",
            "tcs": {
              "value": "0.00",
              "currency": "INR"
            },
            "tds": {
              "value": "0.00",
              "currency": "INR"
            },
            "amount": {
              "value": "49996.0",
              "currency": "INR"
            },
            "status": "PENDING",
            "commission": {
              "value": "3.0",
              "currency": "INR"
            },
            "payment_id": "3a512bd7-ee9e-4ae2-9679-813e26f3144d",
            "updated_at": "2024-12-15T03:47:15.828Z",
            "withholding_amount": {
              "value": "10.0",
              "currency": "INR"
            }
          }
        ]
      }
    ]
  }
}