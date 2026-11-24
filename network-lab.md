# Two-VM Network Lab

## Setup
- Two Ubuntu Server VMs in VirtualBox: `server` (192.168.100.10) and `client` (192.168.100.20)
- Adapter 1: NAT (internet access). Adapter 2: Internal Network `labnet` (private lab network)
- Static IPs configured with Netplan; SSH enabled with OpenSSH

## What I tested
1. **Connectivity:** ping from client to server, 4/4 replies, 0% loss
2. **SSH:** logged into the server from the client
3. **Port scan:** ran my Python scanner (`port_scanner.py`) from the client against the server
   - Before starting a web server: only port 22 (SSH) open
   - After starting `python3 -m http.server 8000` on the server: ports 22 and 8000 open
4. **Traffic capture:** used `tcpdump` on the server to watch the scan

## What I learned
(2-3 sentences in your own words: the three-way handshake, why the scanner's
connections show SYN / SYN-ACK / ACK and then FIN, what a connect scan is)

## Screenshot
(upload your cropped tcpdump screenshot to the repo and link it here)

## Problems I ran into
(e.g. forgot to install OpenSSH, typo in the SSH username, web server started on the wrong VM)
