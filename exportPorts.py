import re

with open("ff.txt", "r", encoding="utf-8", errors="ignore") as file:
    content = file.read()

ports = re.findall(r'"port"\s*:\s*(\d+)', content)

unique_ports = sorted(set(int(port) for port in ports))

for port in unique_ports:
    print(port)

with open("unique_ports.txt", "w") as outfile:
    for port in unique_ports:
        outfile.write(str(port) + "\n")
