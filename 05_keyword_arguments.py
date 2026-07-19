# How to Use Keyword Arguments in Python (with Netmiko)

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "route-views.routeviews.org",
    "username": "rviews",
}


def run_command(command, delay=1):

    connection = ConnectHandler(**device)

    output = connection.send_command(
        command_string=command,
        read_timeout=delay
    )

    connection.disconnect()

    return output


# Keyword arguments
result = run_command(command="show version", delay=5)

print(result)

# Keyword arguments pass values to a function or method by specifying the name of the parameter.
