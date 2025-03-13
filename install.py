#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import json
from termcolor import colored

def check_root():
    if os.geteuid() != 0:
        sys.exit(colored("[!] 0zer0RCE installer must be run as root.", 'red'))

def install_dependencies():
    print(colored("[++] Updating package list and installing dependencies...", 'yellow'))
    os.system("apt-get update && apt-get install -y nmap hping3 build-essential python3-pip ruby-dev git libpcap-dev libgmp3-dev")
    os.system("pip3 install requests pyfiglet termcolor")
    
    # Install Nuclei if not present
    if not os.path.exists("/usr/bin/nuclei"):
        print(colored("[++] Installing Nuclei...", 'yellow'))
        os.system("wget https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei-linux-amd64 -O /usr/bin/nuclei && chmod +x /usr/bin/nuclei")

def setup_0zer0RCE():
    print(colored("[++] Setting up 0zer0RCE...", 'yellow'))
    os.makedirs("/opt/0zer0RCE", exist_ok=True)
    os.system("cp -R tools/ /opt/0zer0RCE/")
    os.system("cp 0zer0RCE.py /opt/0zer0RCE/0zer0RCE.py")
    os.system("cp banner.py /opt/0zer0RCE/banner.py")
    os.system("ln -sf /opt/0zer0RCE/0zer0RCE.py /usr/bin/0zer0RCE")
    os.system("chmod +x /usr/bin/0zer0RCE")
    print(colored("[✅] 0zer0RCE has been successfully installed! Execute '0zer0RCE' in your terminal.", 'green'))

def main():
    check_root()
    install_dependencies()
    setup_0zer0RCE()
    print(colored("[✅] Installation completed successfully!", 'green'))

if __name__ == "__main__":
    main()

        echo "❌ Invalid option. Try again."
        sleep 2
    fi

done
