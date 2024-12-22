{
  "context": {
    "ttl": "PT30S",
    "city": "*",
    "action": "on_issue_status",
    "bap_id": "stage.agrikheti.com",
    "bpp_id": "pramaan.ondc.org/alpha/mock-server",
    "domain": "ONDC:RET10",
    "bap_uri": "https://stage.agrikheti.com/api/ondc",
    "bpp_uri": "https://pramaan.ondc.org/alpha/mock-server/seller",
    "country": "IND",
    "timestamp": "2024-12-22T04:50:31.632Z",
    "message_id": "f0ec61c3-b9ff-40ac-96c1-ddbaef65d308",
    "core_version": "1.2.0",
    "transaction_id": "84f9b14d-ae87-41b0-871f-cb0edb7e7715"
  },
  "message": {
    "issue": {
      "id": "2789b78c-2d28-4a19-a114-aa09b1923e71",
      "created_at": "2024-12-22T04:50:45.778Z",
      "resolution": {
        "long_desc": "For this complaint, refund is to be initiated",
        "short_desc": "Refund to be initiated",
        "refund_amount": "100",
        "action_triggered": "REFUND"
      },
      "updated_at": "2024-12-22T04:50:31.632Z",
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
          },
          {
            "short_desc": "Complaint resolved",
            "updated_at": "2024-12-22T04:50:31.632Z",
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
            "respondent_action": "RESOLVED"
          }
        ]
      },
      "resolution_provider": {
        "respondent_info": {
          "type": "TRANSACTION-COUNTERPARTY-NP",
          "organization": {
            "org": {
              "name": "pramaan.ondc.org/alpha/mock-server::ONDC:RET10"
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