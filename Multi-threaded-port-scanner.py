import argparse
import pyfiglet
import socket
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue
import time

# ASCII Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
ascii_banner1 = pyfiglet.figlet_format("BY ranj1thh", "digital")
print(ascii_banner, ascii_banner1)

# Initialize Colorama
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED

# Lock for thread-safe printing
print_lock = Lock()
q = Queue()
progress = 0


def port_scan(host, port):
    """ Scan a single port on the target host."""
    global progress
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                service = socket.getservbyport(port, "tcp") if port <= 65535 else "Unknown"
                with print_lock:
                    print(f"{GREEN}{host:15}:{port:5} is OPEN  ({service}){RESET}")
            else:
                with print_lock:
                    print(f"{GRAY}{host:15}:{port:5} is closed{RESET}", end='\r')
    except (socket.error, socket.gaierror):
        with print_lock:
            print(f"{RED}Error scanning {host}:{port}{RESET}")
    finally:
        progress += 1
        q.task_done()


def scan_thread(host):
    """ Thread worker function that processes ports from the queue."""
    while True:
        port = q.get()
        port_scan(host, port)


def main(host, ports, num_threads=100):
    """ Main function to initiate the scan."""
    global q, progress
    start_time = time.time()
    print(f"\nScanning {host} from ports {ports[0]} to {ports[-1]} with {num_threads} threads...\n")
    
    for _ in range(num_threads):
        t = Thread(target=scan_thread, args=(host,), daemon=True)
        t.start()
    
    for port in ports:
        q.put(port)
    
    q.join()
    duration = time.time() - start_time
    print(f"\n{GREEN}Scan complete in {duration:.2f} seconds.{RESET}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-threaded port scanner with enhancements")
    parser.add_argument("host", nargs='?', default=socket.gethostbyname(socket.gethostname()), help="Target host (default: local machine)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range to scan (default: 1-1024)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads (default: 100)")
    args = parser.parse_args()
    
    start_port, end_port = map(int, args.ports.split("-"))
    ports = list(range(start_port, end_port + 1))
    
    main(args.host, ports, args.threads)
