# File containing logs
log_file = "sample_log.txt"

failed_attempts = {}  # Dictionary to count failed logins per user
ip_attempts = {}      # Dictionary to count attempts per IP

# Open the log file in read mode
with open(log_file, "r") as file:
    logs = file.readlines()  # Read all lines into a list

print("\nSuspicious Activity:\n")

# Loop through each line in the log file
for line in logs:
    # Check if line contains "FAILED LOGIN"
    if "FAILED LOGIN" in line:
        print(line.strip())  # Print the line (remove extra spaces)

        # Split line into parts (words)
        parts = line.split()

        # Extract user and IP from line
        user = parts[1]   # Example: "admin"
        ip = parts[3]     # Example: "192.168.1.10"

        # Count failed attempts per user
        if user in failed_attempts:
            failed_attempts[user] += 1
        else:
            failed_attempts[user] = 1

        # Count attempts per IP
        if ip in ip_attempts:
            ip_attempts[ip] += 1
        else:
            ip_attempts[ip] = 1

print("\nFailed Login Count:\n")

# Loop through users and print their failed attempts
for user, count in failed_attempts.items():
    print(f"{user}: {count} failed attempts")

    # Detect brute-force attempts
    if count >= 3:
        print(f"[HIGH ALERT] 🚨 Brute-force attack suspected on {user}!")
    elif count == 2:
        print(f"[WARNING] ⚠️ Multiple failed attempts on {user}")

print("\nIP Activity:\n")

# Loop through IPs and print activity
for ip, count in ip_attempts.items():
    print(f"{ip}: {count} attempts")

    # Detect suspicious IP behavior
    if count >= 3:
        print(f"[HIGH ALERT] 🚨 Suspicious activity from IP {ip}")