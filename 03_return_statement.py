# How the return Statement Works in Python (with Netmiko)

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "route-views.routeviews.org",
    "username": "rviews",
}

def run_command(command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    # Ends the function and sends the output back to the caller.
    return output

result = run_command("show version")
print(result)
