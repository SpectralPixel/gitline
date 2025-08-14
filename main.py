def command_help():
    print(r"help - Prints the help dialogue")
    print(r"exit - Exits the program")
    print(r"ping {ip_addr:port} - Sends a message to an IP address")

def take_command():
    cmd = input("\n> ")
    eval(f"command_{cmd}")
