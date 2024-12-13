{
  "context": {
    "ttl": "PT30S",
    "city": "std:080",
    "action": "on_issue",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "pramaan.ondc.org/alpha/mock-server",
    "domain": "ONDC:RET11",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://pramaan.ondc.org/alpha/mock-server/seller",
    "country": "IND",
    "timestamp": "2024-12-13T11:05:04.696Z",
    "message_id": "cc8e509b-651f-4eaa-a3f6-7fbb1cbef608",
    "core_version": "1.2.0",
    "transaction_id": "aed484c0-3c66-4a58-86f5-ba218a9a98a9"
  },
  "message": {
    "issue": {
      "id": "d5511daa-3845-493d-afc6-71674140a91f",
      "created_at": "2024-12-13T11:06:04.386Z",
      "updated_at": "2024-12-13T11:05:04.696Z",
      "issue_actions": {
        "respondent_actions": [
          {
            "short_desc": "Complaint is being processed",
            "updated_at": "2024-12-13T11:05:04.696Z",
            "updated_by": {
              "org": {
                "name": "pramaan.ondc.org/alpha/mock-server::ONDC:RET11"
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