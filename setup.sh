#!/bin/bash

# Cek apakah dijalankan sebagai root (hanya untuk Linux)
if [[ "$OSTYPE" == "linux-gnu"* ]] && [[ $EUID -ne 0 ]]; then
    echo "❌ This installer must be run as root!"
    exit 1
fi

# Deteksi OS & Versi
OS="Unknown"
OS_VERSION="Unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [ -f "/data/data/com.termux/files/usr/bin/pkg" ]; then
        OS="Termux"
        OS_VERSION=$(getprop ro.build.version.release)
    else
        OS="Linux"
        OS_VERSION=$(lsb_release -d 2>/dev/null | cut -f2- -d":" | xargs)
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="MacOS"
    OS_VERSION=$(sw_vers -productVersion)
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    OS="Windows"
    OS_VERSION=$(wmic os get Caption,Version | awk 'NR==2 {print $1, $2}')
fi

echo "📌 Detected OS: $OS $OS_VERSION"

# Fungsi Install
install_0zer0RCE() {
    # Cek dependencies
    DEPENDENCIES=("nmap" "hping3" "python3" "pip3" "git" "ruby" "curl")
    echo "🔎 Checking dependencies..."
    MISSING=()

    for dep in "${DEPENDENCIES[@]}"; do
        if ! command -v $dep &> /dev/null; then
            MISSING+=("$dep")
        fi
    done

    if [ ${#MISSING[@]} -eq 0 ]; then
        echo "✅ All dependencies are installed."
    else
        echo "⚠️ Missing dependencies: ${MISSING[*]}"
        echo "🔄 Installing missing dependencies..."
        
        if [[ "$OS" == "Linux" ]]; then
            sudo apt-get update
            sudo apt-get install -y ${MISSING[*]}
        elif [[ "$OS" == "Termux" ]]; then
            pkg update
            pkg install -y ${MISSING[*]}
        elif [[ "$OS" == "MacOS" ]]; then
            brew install ${MISSING[*]}
        elif [[ "$OS" == "Windows" ]]; then
            echo "⚠️ Please install: ${MISSING[*]} manually."
        fi
    fi

    # Install Python modules
    echo "🐍 Installing Python dependencies..."
    pip3 install requests pyfiglet termcolor

    # Install Nuclei jika belum ada
    if ! command -v nuclei &> /dev/null; then
        echo "⚡ Installing Nuclei..."
        wget https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei-linux-amd64 -O /usr/bin/nuclei
        chmod +x /usr/bin/nuclei
    fi

    # Setup 0zer0RCE
    echo "📂 Setting up 0zer0RCE..."
    mkdir -p /opt/0zer0RCE

    if [ -d "tools" ]; then
        cp -R tools/ /opt/0zer0RCE/
    else
        echo "⚠️ Warning: 'tools/' directory not found, skipping..."
    fi

    if [ -f "0zer0RCE.py" ]; then
        cp 0zer0RCE.py /opt/0zer0RCE/0zer0RCE.py
    else
        echo "⚠️ Warning: '0zer0RCE.py' not found, skipping..."
    fi

    if [ -f "0zer0Login.py" ]; then
        cp 0zer0Login.py /opt/0zer0RCE/0zer0Login.py
    else
        echo "⚠️ Warning: '0zer0Login.py' not found, skipping..."
    fi

    echo "#!/usr/bin/python3" > /usr/bin/0zer0RCE
    echo "exec python3 /opt/0zer0RCE/0zer0RCE.py \"\$@\"" >> /usr/bin/0zer0RCE
    chmod +x /usr/bin/0zer0RCE

    echo "✅ 0zer0RCE has been successfully installed! Run '0zer0RCE' in your terminal."
}

# Fungsi Delete
delete_0zer0RCE() {
    echo "🗑️ Deleting 0zer0RCE..."
    rm -rf /opt/0zer0RCE
    rm -f /usr/bin/0zer0RCE
    echo "✅ 0zer0RCE has been removed!"
}

# Menu
echo ""
echo "📌 0zer0RCE Installer"
echo "1️⃣ Install 0zer0RCE"
echo "2️⃣ Delete 0zer0RCE"
echo "3️⃣ Exit"
read -p "👉 Choose an option: " OPTION

case $OPTION in
    1)
        install_0zer0RCE
        ;;
    2)
        delete_0zer0RCE
        ;;
    3)
        echo "👋 Exiting..."
        exit 0
        ;;
    *)
        echo "❌ Invalid option. Try again."
        ;;
esac
