#!/bin/bash
# Backs up a folder into a dated .tar.gz file

SOURCE="$HOME/testdata"
DEST="$HOME/backups"
DATE=$(date +%Y-%m-%d_%H-%M)

mkdir -p "$DEST"
tar -czf "$DEST/backup_$DATE.tar.gz" "$SOURCE"

# Keep only the 5 newest backups
ls -t "$DEST"/backup_*.tar.gz | tail -n +6 | xargs -r rm

echo "Backup done: backup_$DATE.tar.gz"

