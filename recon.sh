#!/bin/bash

# Prompt the user for the target IP address
read -p "Enter the target IP address: " target_ip

# Run nmap to scan all ports on the target IP quickly
echo "Scanning all open ports on $target_ip using nmap (fast mode)..."
nmap_output=$(nmap -p- --min-rate=10000 -T5 $target_ip)

# Extract open ports from nmap output
open_ports=$(echo "$nmap_output" | grep -oP '\d+/tcp\s+open' | cut -d'/' -f1 | tr '\n' ',' | sed 's/,$//')

if [ -z "$open_ports" ]; then
    echo "No open ports found."
    exit 1
fi

echo "Open ports found: $open_ports"

# Run nmap with service and script detection on the open ports
echo "Running Intensive on $target_ip with open ports..."
nmap -sV -sC -p$open_ports $target_ip --min-rate=10000 -T5 -oN nmap_output.txt
