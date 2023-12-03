from sch.scripts.ssh import ssh
from sch.helpers import (
    definitions,
    request,
    last_down_onu,
    optical,
)

# FUNCTION IMPORT DEFINITIONS
db_request = request.db_request
endpoints = definitions.endpoints
olt_devices = definitions.olt_devices
payload = definitions.payload
down_values = last_down_onu.down_values
optical_values = optical.optical_values


# def client_lookup(comm, command, quit_ssh, device, action):
def client_finder(data):
    payload["lookup_type"] = "C"
    payload["lookup_value"] = {"contract": data["contract"], "olt": data["olt"]}
    req = db_request(endpoints["get_client"], payload)
    if req["data"] is None:
        return None
    client = req["data"]
    (comm, command, quit_ssh) = ssh(olt_devices[str(client["olt"])])
    (client["temp"], client["pwr"]) = optical_values(comm, command, client)
    (
        client["last_down_cause"],
        client["last_down_time"],
        client["last_down_date"],
        client["status"],
    ) = down_values(comm, command, client)
    quit_ssh()
    client["name"] = f'{client["name_1"]} {client["name_2"]} {client["contract"]}'
    return client


def optical_finder(data):
    response = {"name": None, "pwr": None}
    payload["lookup_type"] = "C"
    payload["lookup_value"] = {"contract": data["contract"], "olt": data["olt"]}
    req = db_request(endpoints["get_client"], payload)
    if req["data"] is None:
        return None
    client = req["data"]
    (comm, command, quit_ssh) = ssh(olt_devices[str(client["olt"])])
    (_, response["pwr"]) = optical_values(comm, command, client)
    quit_ssh()
    response["name"] = f'{client["name_1"]} {client["name_2"]} {client["contract"]}'
    return response
