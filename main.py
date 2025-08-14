import sys

def command_help():
    print(r"help - Prints the help dialogue")
    print(r"exit - Exits the program")
    print(r"ping {ip_addr:port} - Sends a message to an IP address")

def command_exit():
    sys.exit(0)

def take_command():
    cmd = input("\n> ")
    eval(f"command_{cmd}()")


print("Welcome to GitLine")
command_help()

while True:
    take_command()
