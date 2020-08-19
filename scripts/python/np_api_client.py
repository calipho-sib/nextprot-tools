import http.client
import json

conn = http.client.HTTPSConnection("api.nextprot.org")
conn.request("GET", "/entry/NX_P01308")
res = conn.getresponse()

entry_data = res.read()
entry_json = json.loads(entry_data)
overview = entry_json["entry"]["overview"]

print(json.dumps(overview, indent=4, sort_keys=True))