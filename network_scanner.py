import socket  # Import socket module to work with network connections

# Ask user to enter the target IP address
target = input("Enter IP to scan: ")

# Print a header for better output readability
print("\n==============================")
print(f" Scanning Target: {target}")
print("==============================\n")

open_ports = []  # List to store all open ports found

# Loop through ports 1 to 1024 (common ports)
for port in range(1, 1025):
    # Create a socket object (IPv4, TCP connection)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set timeout so it doesn't wait forever
    socket.setdefaulttimeout(0.5)

    # Try to connect to the target IP and port
    result = s.connect_ex((target, port))

    # If result = 0 → connection successful → port is open
    if result == 0:
        open_ports.append(port)  # Save open port
        print(f"[+] Port {port} is OPEN")

    s.close()  # Close the connection after checking

# Print summary after scan completes
print("\nScan Completed.")
print(f"Open Ports Found: {open_ports}")