# Multi-threaded-port-scanner

## Overview
This is an advanced multi-threaded port scanner built in Python, designed for high-speed scanning of a target host’s open ports within a specified range. The script efficiently utilizes threading to speed up the scanning process and includes additional enhancements such as service detection, error handling, and progress tracking.

## Features
- Highly efficient multi-threaded scanning for rapid results
- Service detection for identifying common applications running on open ports
- Improved error handling for increased stability
- Automatic detection of localhost if no host is specified
- Customizable thread count for optimal performance tuning
- Live progress indicator to track scanning status
- Enhanced output formatting for better readability

## Requirements
Ensure you have Python 3 installed along with the following dependencies:
```bash
pip install pyfiglet colorama
```

## Usage
Run the script using:
```bash
python port_scanner.py <target_host> -p <start_port>-<end_port> -t <threads>
```

### Examples:
- Scan all ports (default: 1-1024) on a specific host:
  ```bash
  python port_scanner.py 192.168.1.1
  ```
- Scan ports 20-1000 on a target with 200 threads:
  ```bash
  python port_scanner.py 192.168.1.1 -p 20-1000 -t 200
  ```
- Scan your own machine (localhost) with 50 threads:
  ```bash
  python port_scanner.py -t 50
  ```

## How It Works
1. The script initializes a banner and prepares multi-threading.
2. Ports are added to a queue, and multiple threads begin scanning simultaneously.
3. If a port is open, the script displays the port number along with its associated service.
4. Real-time progress is shown, updating as scanning proceeds.
5. At the end, a summary of all open ports is displayed along with the total scanning time.

## Disclaimer
This tool is intended for educational and ethical security testing only. Unauthorized scanning of networks without permission may violate laws and regulations. The developer is not responsible for any misuse of this tool.

## License
MIT License © 2025 @ranj1thh

---
Happy Scanning! 🚀

