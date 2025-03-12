#!/bin/bash

# Setup-Dashboard
figlet Setup-Dashboard | lolcat

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
        echo "Checking installed packages..."
        sleep 1

        # Cek apakah Python sudah terinstall
        if command -v python3 &>/dev/null; then
            echo "✅ Python3 already installed."
        else
            echo "Installing Python..."
            if [ "$OS_TYPE" == "Android" ]; then
                pkg install python python-pip -y
            else
                sudo apt install python3 python3-pip -y
            fi
        fi

        # Cek apakah pip sudah terinstall
        if command -v pip3 &>/dev/null; then
            echo "✅ pip3 already installed."
        else
            echo "Installing pip3..."
            python3 -m ensurepip --default-pip
        fi

        # Cek apakah pyfiglet, termcolor, dan lolcat sudah ada
        if python3 -c "import pyfiglet, termcolor" 2>/dev/null; then
            echo "✅ Python packages already installed."
        else
            echo "Installing Python packages..."
            pip3 install pyfiglet termcolor lolcat
        fi

        # Cek apakah Nuclei sudah terinstall
        if command -v nuclei &>/dev/null; then
            echo "✅ Nuclei already installed."
        else
            echo "Installing Nuclei..."
            wget https://github.com/projectdiscovery/nuclei/releases/download/v2.9.9/nuclei_2.9.9_linux_amd64.zip
            unzip nuclei_2.9.9_linux_amd64.zip
            if [ "$OS_TYPE" == "Android" ]; then
                mv nuclei $PREFIX/bin/
            else
                sudo mv nuclei /usr/local/bin/
            fi
            rm nuclei_2.9.9_linux_amd64.zip
        fi

        # Cek apakah Nuclei templates sudah di-download
        if [ -d "$HOME/nuclei-templates" ]; then
            echo "✅ Nuclei templates already installed."
        else
            echo "Downloading Nuclei templates..."
            nuclei -update-templates
        fi

        # Cek apakah direktori secret sudah ada
        if [ -d "$HOME/.0zer0RCE" ]; then
            echo "✅ Secret directory already exists."
        else
            echo "Creating secret directory..."
            mkdir -p ~/.0zer0RCE/
        fi

        echo "✅ Setup selesai!"
        sleep 2
        clear
        python3 start.py
        break

    elif [ "$choice" == "2" ]; then
        echo "Deleting installed packages..."
        sleep 1

        if [ "$OS_TYPE" == "Android" ]; then
            pkg uninstall python -y
            rm -f $PREFIX/bin/nuclei
        else
            sudo apt remove python3 python3-pip -y
            sudo rm -f /usr/local/bin/nuclei
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
