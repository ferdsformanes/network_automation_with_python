# Write Your First Python Function with Netmiko

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "route-views.routeviews.org",
    "username": "rviews",
}

def show_version():
    connection = ConnectHandler(**device)
    output = connection.send_command("show version")
    connection.disconnect()
    return output

print(show_version())
