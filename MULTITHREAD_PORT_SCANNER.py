import socket
import threading
from queue import Queue
from datetime import datetime

print("===================================")
print("  MULTITHREADED PYTHON PORT SCANNER")
print("===================================")

target = input("Enter target IP or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    exit()

# Color codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(f"\n{CYAN}Scanning target:{RESET} {target_ip}")
print(f"{CYAN}Ports:{RESET} 1 - 65535")
print(f"{CYAN}Started at:{RESET} {datetime.now()}")
print("-----------------------------------")

THREAD_COUNT = 100
queue = Queue()
print_lock = threading.Lock()

open_ports = []

def scan_port():
    while not queue.empty():
        port = queue.get()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            with print_lock:
                print(f"{GREEN}[OPEN]{RESET} Port {port}")
                open_ports.append(port)

        s.close()
        queue.task_done()


# Add ports to queue
for port in range(1, 65536):
    queue.put(port)

# Start threads
for _ in range(THREAD_COUNT):
    thread = threading.Thread(target=scan_port)
    thread.daemon = True
    thread.start()

queue.join()

print("-----------------------------------")
print(f"{CYAN}Scan completed at:{RESET} {datetime.now()}")

# Save results
filename = f"scan_results_{target_ip}.txt"

with open(filename, "w") as file:
    file.write(f"Port Scan Results for {target_ip}\n")
    file.write(f"Scan Time: {datetime.now()}\n\n")

    if open_ports:
        for port in open_ports:
            file.write(f"Port {port} OPEN\n")
    else:
        file.write("No open ports found.\n")

print(f"{CYAN}Results saved to:{RESET} {filename}")