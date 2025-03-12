# 0zer0RCE - Remote Code Execution Scanner & Exploiter
# Author: AryzXploit
# nak rename? ijin owner dulu

import os
import sys
import requests
import json
import pyfiglet
import time
from termcolor import colored

secret_path = os.path.expanduser('~/.0zer0RCE/')
auth_status_file = os.path.join(secret_path, 'auth_status.json')

if not os.path.exists(auth_status_file):
    print(colored("❌ Unauthorized Access! Please login through Start.py.", 'red'))
    sys.exit(1)

with open(auth_status_file, 'r') as file:
    auth_status = json.load(file)

if not auth_status.get('authenticated') or 'token' not in auth_status:
    print(colored("❌ Unauthorized Access! Please login through Start.py.", 'red'))
    sys.exit(1)

print(colored("✅ Access Granted!", 'green'))
time.sleep(3)

def show_available_rce_payloads():
    print(colored('📜 Available RCE Payloads:', 'yellow'))
    with open('rce_payloads.json', 'r') as file:
        payloads = json.load(file)["payloads"]  # Tambah ["payloads"]
        for payload in payloads:
            print(colored(f"- {payload['cve']} - {payload['description']}", 'cyan'))  # Perbaiki kunci

def scan_single_url(url):
    with open('rce_payloads.json', 'r') as file:
        payloads = json.load(file)["payloads"]  # Tambah ["payloads"]

    print(colored(f'🔍 Scanning {url} for RCE vulnerabilities...', 'yellow'))

    for payload in payloads:
        print(colored(f"[-] Testing {payload['cve']} - {payload['description']}", 'cyan'))  # Perbaiki kunci
        try:
            response = requests.get(url)
            if payload['payload'] in response.text:  # Perbaiki kunci
                print(colored(f"[✅] Vulnerable to {payload['cve']}", 'green'))
            else:
                print(colored('[❌] Not Vulnerable', 'red'))
        except Exception as e:
            print(colored(f'[!] Error: {e}', 'red'))

def run_nuclei_scan(target):
    print(colored(f'🔍 Running Nuclei scan on {target}...', 'yellow'))
    os.system(f'nuclei -u {target} -t cves/ -o nuclei_results.txt')
    print(colored('[✅] Nuclei scan completed!', 'green'))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(pyfiglet.figlet_format('0zer0RCE', font='slant'), 'red'))
        print(colored('1. Single URL Scan', 'yellow'))
        print(colored('2. Nuclei Machine Scanner', 'yellow'))
        print(colored('3. Show Available RCE Payloads', 'yellow'))
        print(colored('0. Exit', 'yellow'))

        choice = input(colored('🤖 Pilih opsi: ', 'yellow'))

        if choice == '1':
            url = input(colored('🌐 Masukkan URL target: ', 'yellow'))
            scan_single_url(url)
            input(colored('Press Enter to continue...', 'cyan'))

        elif choice == '2':
            target = input(colored('🌐 Masukkan Target untuk Nuclei Scanner: ', 'yellow'))
            run_nuclei_scan(target)
            input(colored('Press Enter to continue...', 'cyan'))

        elif choice == '3':
            show_available_rce_payloads()
            input(colored('Press Enter to continue...', 'cyan'))

        elif choice == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(pyfiglet.figlet_format('GoodBye Sir', font='slant'), 'green'))
            break

        else:
            print(colored('❌ Invalid Option! Please try again.', 'red'))
            time.sleep(3)


if __name__ == '__main__':
    main()
