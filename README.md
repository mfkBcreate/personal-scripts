# Scripts

A collection of Bash and Python scripts I wrote while learning
Linux, networking, and security. Tested on Ubuntu (WSL) on Windows.

## Scripts

| Script | Description |
|--------|-------------|
| `backup.sh` | Archives a folder into a timestamped `.tar.gz` and keeps the 5 newest backups |
| `port_scanner.py` | Scans a host for open TCP ports in a given range (for use on your own machines) |

## Usage
1. Download the script
2. Make it executable: `chmod +x script_name.sh`
3. Edit any variables at the top of the script
4. Run it: `./script_name.sh`

## Scheduling with cron (example for backup.sh)
Runs daily at 9 PM:

    0 21 * * * $HOME/scripts/backup.sh
