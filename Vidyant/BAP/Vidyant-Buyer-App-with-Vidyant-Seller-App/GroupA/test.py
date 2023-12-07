import requests
import json

# collect candidate json
on_search_full_catalog_refresh = json.load(open('./Flow1/full_catalog_on_search_2.json'))
select = json.load(open('./Flow2/select_9.json'))
url = "https://log-validation.ondc.org/api/validate"

payload = json.dumps({
  "domain": "ONDC:RET12",
  "version": "1.2.0",
  "payload": {
    "search_full_catalog_refresh": {},
    "on_search_full_catalog_refresh": on_search_full_catalog_refresh,
    "search_inc_refresh": {},
    "on_search_inc_refresh": {},
    "select": select,
    "on_select": {},
    "init": {},
    "on_init": {},
    "confirm": {},
    "on_confirm": {},
    "on_status_pending": {},
    "on_status_picked": {},
    "on_status_delivered": {}
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
json_formatted_str = json.dumps(json.loads(response.text), indent=2)
print(json_formatted_str)
