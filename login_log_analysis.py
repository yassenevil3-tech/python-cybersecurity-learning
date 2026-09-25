# python-cybersecurity-learning
logs = [
    "10.0.0.3 login failed",
    "192.168.1.5 login success",
    "10.0.0.3 login failed",
    "172.16.0.5 login success",
    "192.168.1.5 llogsogin failed",
    "10.0.0.3 login success"
]

# failed counter code
failed_count = 0

for log in logs:
    parts = log.split()
    if parts[2] == "failed":
        failed_count = failed_count + 1

print("failed login:", failed_count)


# successful counter code
succsful_count = 0
i = 0

while i < len(logs):
    parts = logs[i].split()

    if parts[2] == "success":
        succsful_count = succsful_count + 1

    i = i + 1

print("succses logins:", succsful_count)


# IP failed logins code
for log in logs:
    parts = log.split()

    if parts[2] == "failed":
        print(parts[0])


# failed IP dictionary
failed_by_ip = {}

for log in logs:
    parts = log.split()

    if parts[2] == "failed":
        if parts[0] in failed_by_ip:
            failed_by_ip[parts[0]] = failed_by_ip[parts[0]] + 1
        else:
            failed_by_ip[parts[0]] = 1
#warning massige
for failed_ip in failed_by_ip:
  if failed_by_ip[failed_ip]>=2:
    print("WARNING",failed_ip)
