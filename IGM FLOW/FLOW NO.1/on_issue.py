{
  "context": {
    "ttl": "PT30S",
    "city": "*",
    "action": "on_issue",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "pramaan.ondc.org/alpha/mock-server",
    "domain": "ONDC:RET10",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://pramaan.ondc.org/alpha/mock-server/seller",
    "country": "IND",
    "timestamp": "2024-12-22T04:50:00.111Z",
    "message_id": "fb2ec5f2-22b0-454b-84d8-797e776eba2f",
    "core_version": "1.2.0",
    "transaction_id": "84f9b14d-ae87-41b0-871f-cb0edb7e7715"
  },
  "message": {
    "issue": {
      "id": "2789b78c-2d28-4a19-a114-aa09b1923e71",
      "created_at": "2024-12-22T04:50:45.778Z",
      "updated_at": "2024-12-22T04:50:00.111Z",
      "issue_actions": {
        "respondent_actions": [
          {
            "short_desc": "Complaint is being processed",
            "updated_at": "2024-12-22T04:50:00.111Z",
            "updated_by": {
              "org": {
                "name": "pramaan.ondc.org/alpha/mock-server::ONDC:RET10"
              },
              "person": {
                "name": "Mayur"
              },
              "contact": {
                "email": "mayur@gmail.com",
                "phone": "9450394140"
              }
            },
            "cascaded_level": 1,
            "respondent_action": "PROCESSING"
          }
        ]
      }
    }
  }
}