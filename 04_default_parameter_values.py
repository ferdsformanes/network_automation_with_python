# How to Use Default Parameter Values in Python (with Netmiko)

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "route-views.routeviews.org",
    "username": "rviews",
}

def run_command(command="show version"):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()

    # Ends the function and sends the output back to the caller.
    return output

print(run_command())

print(run_command("show ip interface brief"))
