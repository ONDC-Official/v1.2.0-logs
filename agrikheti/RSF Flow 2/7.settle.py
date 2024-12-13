{
  "context": {
    "ttl": "P1D",
    "action": "settle",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "sa_nocs.nbbl.com",
    "domain": "ONDC:NTS10",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://sa_nocs.nbbl.com/nocs_test",
    "version": "2.0.0",
    "location": {
      "city": {
        "code": "*"
      },
      "country": {
        "code": "IND"
      }
    },
    "timestamp": "2024-12-13T12:20:56.207Z",
    "message_id": "0fe4891b-21ad-4600-9bec-0d245f633840",
    "transaction_id": "75425405-dd81-49ac-ba44-2099cbccf2df"
  },
  "message": {
    "settlement": {
      "id": "e08f8eda-ee64-4317-a630-e8aa4cf5bdc2",
      "type": "NP-NP",
      "orders": [
        {
          "id": "ondch3sBCVELRmLLBLGFJWUIVW81DqrS",
          "self": {
            "amount": {
              "value": "3.0",
              "currency": "INR"
            }
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
            }
          }
        }
      ]
    },
    "receiver_app_id": "pramaan.ondc.org/alpha/mock-server",
    "collector_app_id": "stage.agrikheti.com"
  }
}