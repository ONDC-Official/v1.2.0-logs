import requests
import json

# collect candidate json
search_full_catalog_refresh = json.load(open('./Flow1/full_catalog_search_1.json'))
on_search_full_catalog_refresh = json.load(open('./Flow1/full_catalog_on_search_2.json'))
search_inc_refresh = json.load(open('./Flow1/incremental_search_3.json'))
on_search_inc_refresh = json.load(open('./Flow1/incremental_on_search(for_provider_changes_disable_4).json'))
select = json.load(open('./Flow2/select_9.json'))
on_select = json.load(open('./Flow2/on_select_10.json'))
init = json.load(open('./Flow2/init_11.json'))
on_init = json.load(open('./Flow2/on_init_12.json'))
confirm = json.load(open('./Flow2/confirm_13.json'))
on_confirm = json.load(open('./Flow2/on_confirm_14.json'))
on_status_pending = json.load(open('./Flow2/on_status_16(solicited).json'))
on_status_picked = json.load(open('./Flow2/on_status_17(unsolicited)_order_packed.json'))
on_status_delivered = json.load(open('./Flow2/on_status_18(unsolicited)_out_for_delivery.json'))

url = "https://log-validation.ondc.org/api/validate"

payload = json.dumps({
  "domain": "ONDC:RET12",
  "version": "1.2.0",
  "payload": {
    "search_full_catalog_refresh": search_full_catalog_refresh,
    "on_search_full_catalog_refresh": on_search_full_catalog_refresh,
    "search_inc_refresh": search_inc_refresh,
    "on_search_inc_refresh": on_search_inc_refresh,
    "select": select,
    "on_select": on_select,
    "init": init,
    "on_init": on_init,
    "confirm": confirm,
    "on_confirm": on_confirm,
    "on_status_pending": on_status_pending,
    "on_status_picked": on_status_picked,
    "on_status_delivered": on_status_delivered
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
json_formatted_str = json.dumps(json.loads(response.text), indent=2)
print(json_formatted_str)
