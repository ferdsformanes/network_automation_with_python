# How to Use *args and **kwargs in Python (with Netmiko)

"""
*args in a function or method definition → packs positional arguments into a tuple.
*args in a function or method call → unpacks a tuple into positional arguments.

**kwargs in a function or method definition → packs keyword arguments into a dictionary.
**kwargs in a function or method call → unpacks a dictionary into keyword arguments.
"""

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "route-views.routeviews.org",
    "username": "rviews",
}


def run_commands(*args, **kwargs):
    print("Packed positional arguments (*args):")
    print(args)

    print("\nPacked keyword arguments (**kwargs):")
    print(kwargs)

    connection = ConnectHandler(**device)

    for command in args:
        print(f"\n###{command}###\n")

        output = connection.send_command(
            command_string=command,
            **kwargs
        )

        print(output)

    connection.disconnect()


# Tuple of commands
commands = (
    "show version",
    "show clock",
    "show ip interface brief",
)

# Dictionary of keyword arguments
options = {
    "read_timeout": 5,
    "strip_prompt": False,
}

# These two calls are equivalent

run_commands(
    "show version",
    "show clock",
    "show ip interface brief",
    read_timeout=5,
    strip_prompt=False,
)

# run_commands(
#     *commands,
#     **options
# )
