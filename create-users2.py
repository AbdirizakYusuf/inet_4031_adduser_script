#!/usr/bin/python3
# User Account Manager v2
# INET4031 - Enhanced with Interactive Dry-Run

import os
import re
import sys

def main():
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper() == 'Y'
    
    for line in sys.stdin:
        if re.match("^#", line):
            if dry_run:
                print(f"Dry-Run: Skipped comment line: {line.strip()}")
            continue

        fields = line.strip().split(':')
        if len(fields) != 5:
            if dry_run:
                print(f"Dry-Run Error: Malformed line (expected 5 fields): {line.strip()}", file=sys.stderr)
            continue

        username = fields[0]
        gecos = f"{fields[3]} {fields[2]},,,"
        groups = [g for g in fields[4].split(',') if g]

        if dry_run:
            print(f"\n=== Dry-Run ===\nWould create user: {username}")
            print(f"Command: adduser --disabled-password --gecos '{gecos}' {username}")
            for group in groups:
                print(f"Would add to group: {group}")
                print(f"Command: adduser {username} {group}")
            continue

        os.system(f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}")
        for group in groups:
            os.system(f"/usr/sbin/adduser {username} {group}")

if __name__ == "__main__":
    main()
