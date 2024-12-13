{
  "context": {
    "ttl": "PT30S",
    "city": "std:080",
    "action": "issue",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "pramaan.ondc.org/alpha/mock-server",
    "domain": "ONDC:RET11",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://pramaan.ondc.org/alpha/mock-server/seller",
    "country": "IND",
    "timestamp": "2024-12-13T11:06:45.417Z",
    "message_id": "7128c8c7-31c7-4b56-a5f7-a8563273b843",
    "core_version": "1.2.0",
    "transaction_id": "aed484c0-3c66-4a58-86f5-ba218a9a98a9"
  },
  "message": {
    "issue": {
      "id": "d5511daa-3845-493d-afc6-71674140a91f",
      "rating": "THUMBS-UP",
      "status": "CLOSED",
      "created_at": "2024-12-13T11:06:04.386Z",
      "updated_at": "2024-12-13T11:06:45.417Z",
      "issue_actions": {
        "complainant_actions": [
          {
            "short_desc": "Complaint created",
            "updated_at": "2024-12-13T11:06:04.386Z",
            "updated_by": {
              "org": {
                "name": "stage.agrikheti.com::ONDC:RET11"
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
            "updated_at": "2024-12-13T11:06:45.417Z",
            "updated_by": {
              "org": {
                "name": "stage.agrikheti.com::ONDC:RET11"
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