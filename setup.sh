#!/bin/bash

# Setup-Dasboard
figlet Setup-Dasboard | lolcat

OS_TYPE="$(uname -o)"
if [ "$OS_TYPE" == "Android" ]; then
    echo "📂 Detected OS: Termux (Android)"
else
    OS_NAME="$(grep '^ID=' /etc/os-release | cut -d= -f2)"
    OS_VERSION="$(grep 'VERSION_ID=' /etc/os-release | cut -d= -f2)"
    echo "📂 Detected OS: Linux ($OS_NAME $OS_VERSION)"
fi

while true; do
    echo "📌 1. Install Packages"
    echo "🧹 2. Delete My Packages"
    echo "❌ 3. Exit"
    read -p "🤖 Pilih opsi: " choice

    if [ "$choice" == "1" ]; then
        echo "Installing packages..."
        sleep 1

        # Update package list and install dependencies (Linux & Termux support)
        if [ "$OS_TYPE" == "Android" ]; then
            pkg update && pkg upgrade -y
            pkg install python python-pip -y
            pip install pyfiglet termcolor lolcat
        else
            sudo apt update && sudo apt upgrade -y
            sudo apt install python3 python3-pip -y
            pip3 install pyfiglet termcolor lolcat
        fi

        # Install Nuclei
        wget https://github.com/projectdiscovery/nuclei/releases/download/v2.9.9/nuclei_2.9.9_linux_amd64.zip
        unzip nuclei_2.9.9_linux_amd64.zip
        if [ "$OS_TYPE" == "Android" ]; then
            mv nuclei $PREFIX/bin/
        else
            sudo mv nuclei /usr/local/bin/
        fi
        rm nuclei_2.9.9_linux_amd64.zip

        # Install Nuclei Templates
        nuclei -update-templates

        # Create secret directory
        mkdir -p ~/.0zer0RCE/

        echo "✅ Setup selesai!"
        sleep 2
        clear
        python3 Start.py
        break
    elif [ "$choice" == "2" ]; then
        echo "Deleting installed packages..."
        sleep 1
        if [ "$OS_TYPE" == "Android" ]; then
            pkg uninstall python -y
            rm $PREFIX/bin/nuclei
        else
            sudo apt remove python3 python3-pip -y
            sudo rm /usr/local/bin/nuclei
        fi
        rm -rf ~/.0zer0RCE/
        echo "✅ Packages deleted successfully."
        sleep 2
        clear
    elif [ "$choice" == "3" ]; then
        echo "Goodbye!"
        sleep 1
        clear
        break
    else
        echo "❌ Invalid option. Try again."
        sleep 2
    fi

done
