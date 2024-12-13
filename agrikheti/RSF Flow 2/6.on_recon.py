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
    "timestamp": "2024-12-13T12:18:51.473Z",
    "message_id": "f9b07f35-350b-4357-bcbd-2596d6424d85",
    "transaction_id": "75425405-dd81-49ac-ba44-2099cbccf2df"
  },
  "message": {
    "orders": [
      {
        "id": "ondch3sBCVELRmLLBLGFJWUIVW81DqrS",
        "amount": {
          "value": "365.0",
          "currency": "INR"
        },
        "settlements": [
          {
            "id": "60a55b0a-d6a2-407b-bfb4-652f004a1778",
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
              "value": "365.0",
              "currency": "INR",
              "diff_value": "100"
            },
            "status": "PENDING",
            "commission": {
              "value": "3.0",
              "currency": "INR",
              "diff_value": "100"
            },
            "payment_id": "7436695c-569c-4427-b66c-a86498c03ee3",
            "updated_at": "2024-12-13T12:19:22.673Z",
            "withholding_amount": {
              "value": "10.0",
              "currency": "INR",
              "diff_value": "10"
            }
          }
        ],
        "recon_accord": "true"
      }
    ]
  }
}