{
  "context": {
    "ttl": "PT30S",
    "city": "*",
    "action": "issue",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "pramaan.ondc.org/alpha/mock-server",
    "domain": "ONDC:RET10",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://pramaan.ondc.org/alpha/mock-server/seller",
    "country": "IND",
    "timestamp": "2024-12-22T05:01:20.104Z",
    "message_id": "7053d778-5fb9-40ee-8279-3e1b1bcf469c",
    "core_version": "1.2.0",
    "transaction_id": "84f9b14d-ae87-41b0-871f-cb0edb7e7715"
  },
  "message": {
    "issue": {
      "id": "2789b78c-2d28-4a19-a114-aa09b1923e71",
      "rating": "THUMBS-UP",
      "status": "CLOSED",
      "created_at": "2024-12-22T04:50:45.778Z",
      "updated_at": "2024-12-22T05:01:20.104Z",
      "issue_actions": {
        "complainant_actions": [
          {
            "short_desc": "Complaint created",
            "updated_at": "2024-12-22T04:50:45.778Z",
            "updated_by": {
              "org": {
                "name": "stage.agrikheti.com::ONDC:RET10"
              },
              "person": {
                "name": "John Doe"
              },
              "contact": {
                "email": "interfacingapp@interface.com",
                "phone": "9450394039"
              }
            },
            "complainant_action": "OPEN"
          },
          {
            "short_desc": "Complaint closed",
            "updated_at": "2024-12-22T05:01:20.104Z",
            "updated_by": {
              "org": {
                "name": "stage.agrikheti.com::ONDC:RET10"
              },
              "person": {
                "name": "John Doe"
              },
              "contact": {
                "email": "interfacingapp@interface.com",
                "phone": "9450394039"
              }
            },
            "complainant_action": "CLOSE"
          }
        ]
      }
    }
  }
}