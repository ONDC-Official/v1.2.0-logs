{
  "context": {
    "ttl": "PT30S",
    "city": "std:080",
    "action": "on_issue_status",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "pramaan.ondc.org/alpha/mock-server",
    "domain": "ONDC:RET11",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://pramaan.ondc.org/alpha/mock-server/seller",
    "country": "IND",
    "timestamp": "2024-12-13T11:05:37.969Z",
    "message_id": "f953bb3b-5475-42ad-b30b-f92ab515440a",
    "core_version": "1.2.0",
    "transaction_id": "aed484c0-3c66-4a58-86f5-ba218a9a98a9"
  },
  "message": {
    "issue": {
      "id": "d5511daa-3845-493d-afc6-71674140a91f",
      "created_at": "2024-12-13T10:17:23.652Z",
      "resolution": {
        "long_desc": "For this complaint, refund is to be initiated",
        "short_desc": "Refund to be initiated",
        "refund_amount": "100",
        "action_triggered": "REFUND"
      },
      "updated_at": "2024-12-13T11:05:37.969Z",
      "issue_actions": {
        "respondent_actions": [
          {
            "short_desc": "Complaint is being processed",
            "updated_at": "2024-12-13T10:16:24.020Z",
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
          },
          {
            "short_desc": "Complaint resolved",
            "updated_at": "2024-12-13T11:05:37.969Z",
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
            "respondent_action": "RESOLVED"
          }
        ]
      },
      "resolution_provider": {
        "respondent_info": {
          "type": "TRANSACTION-COUNTERPARTY-NP",
          "organization": {
            "org": {
              "name": "pramaan.ondc.org/alpha/mock-server::ONDC:RET11"
            },
            "person": {
              "name": "resolution provider org contact person name"
            },
            "contact": {
              "email": "mayur@gmail.com",
              "phone": "9059304940"
            }
          },
          "resolution_support": {
            "gros": [
              {
                "person": {
                  "name": "Mayur"
                },
                "contact": {
                  "email": "mayur@gmail.com",
                  "phone": "9605960796"
                },
                "gro_type": "TRANSACTION-COUNTERPARTY-NP-GRO"
              }
            ],
            "contact": {
              "email": "mayur@gmail.com",
              "phone": "9949595059"
            },
            "chat_link": "http://chat-link/respondent"
          }
        }
      }
    }
  }
}