{
  "context": {
    "ttl": "PT10M",
    "action": "on_recon",
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
    "timestamp": "2024-12-15T03:46:29.416Z",
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
              "currency": "INR",
              "diff_value": "0"
            },
            "tds": {
              "value": "0.00",
              "currency": "INR",
              "diff_value": "0"
            },
            "amount": {
              "value": "49996.0",
              "currency": "INR",
              "diff_value": "100"
            },
            "status": "PENDING",
            "commission": {
              "value": "3.0",
              "currency": "INR",
              "diff_value": "100"
            },
            "payment_id": "3a512bd7-ee9e-4ae2-9679-813e26f3144d",
            "updated_at": "2024-12-15T03:47:15.828Z",
            "withholding_amount": {
              "value": "10.0",
              "currency": "INR",
              "diff_value": "100"
            }
          }
        ],
        "recon_accord": "false"
      }
    ]
  }
}