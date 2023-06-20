headers = {"Content-Type": "application/json"}
# domain = "http://127.0.0.1:8000"
domain = "http://db-api.conext.net.ve"
payload = {"lookup_type": None, "lookup_value": None}
endpoints = {
    "get_client": "/get-client",
    "get_clients": "/get-clients",
    "add_client": "/add-client",
    "update_client": "/update-client",
    "remove_client": "/remove-client",
}
olt_devices = {"1": "181.232.180.7", "2": "181.232.180.5", "3": "181.232.180.6"}
rtr_devices = {
    "e1": "181.232.180.1",
    "e2": "181.232.180.2",
    "a1": "181.232.180.3",
    "a2": "181.232.180.4",
}
