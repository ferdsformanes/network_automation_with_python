# Exception Handling (with Netmiko)

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "route-views.routeviews.org",
    "username": "rviews",
}

def run_command(command: str) -> str:
    try:
        connection = ConnectHandler(**device)
        output = connection.send_command(command)
        connection.disconnect()
        return output

    except Exception as error:
        return f"An error occurred: {error}"


# Intentionally use an invalid command.
result = run_command("show ferds")
print(result)