# Python Type Hints Explained (with Netmiko)
# Type hints are recommendations, not rules.
# They help programmers and code editors catch mistakes early.

# Parameter type hint:
# parameter_name: expected_type

# Return type hint:
# -> return_type

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "route-views.routeviews.org",
    "username": "rviews",
}

def run_command(command: str) -> str:
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    return output


result = run_command("show version")
print(type(result)) 
print(result)