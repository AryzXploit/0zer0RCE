#!/usr/bin/python3
# 0zer0Login.py - User Authentication for 0zer0RCE
# Author: AryzXploit

import os
import json
import pyfiglet
import time
import random
import string
from termcolor import colored

secret_path = os.path.expanduser('~/.0zer0RCE/')
session_file = os.path.join(secret_path, 'session.json')
auth_status_file = os.path.join(secret_path, 'auth_status.json')

def setup_secret_path():
    if not os.path.exists(secret_path):
        os.makedirs(secret_path)

def save_session(data):
    with open(session_file, 'w') as file:
        json.dump(data, file)

def load_session():
    if not os.path.exists(session_file):
        return None
    with open(session_file, 'r') as file:
        return json.load(file)

def generate_token(length=32):
    """Generate a random authentication token."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def register():
    setup_secret_path()
    print(colored(pyfiglet.figlet_format('Register', font='slant'), 'magenta'))
    print(colored("\n📌 REGISTER", 'yellow'))
    username = input("Username: ")
    password = input("Password: ")
    session_data = {'username': username, 'password': password}
    save_session(session_data)
    print(colored("✅ Registration successful!", 'green'))

def login():
    session_data = load_session()
    if not session_data:
        print(colored("❌ No user registered. Please register first.", 'red'))
        return False

    print(colored(pyfiglet.figlet_format('Login', font='slant'), 'magenta'))
    print(colored("\n🔑 LOGIN", 'yellow'))
    username = input("Username: ")
    password = input("Password: ")

    if session_data['username'] == username and session_data['password'] == password:
        print(colored("✅ Login successful!", 'green'))

        # Generate and save token
        token = generate_token()
        with open(auth_status_file, 'w') as file:
            json.dump({'authenticated': True, 'token': token}, file)

        time.sleep(2)
        os.system('clear')
        print(colored("🔄 Starting 0zer0RCE...", 'cyan'))
        time.sleep(2)
        
        # Jalankan 0zer0RCE.py setelah login
        os.system(f'python3 /opt/0zer0RCE/0zer0RCE.py --token {token}')
        return True
    else:
        print(colored("❌ Invalid credentials.", 'red'))
        return False

def reset_password():
    print(colored(pyfiglet.figlet_format('Reset Password', font='slant'), 'magenta'))
    print(colored("\n🔄 RESET PASSWORD", 'yellow'))
    if load_session():
        new_password = input("New Password: ")
        session_data = load_session()
        session_data['password'] = new_password
        save_session(session_data)
        print(colored("✅ Password reset successful!", 'green'))
    else:
        print(colored("❌ No user registered. Please register first.", 'red'))

def main():
    while True:
        os.system('clear')
        print(colored(pyfiglet.figlet_format('0zer0Login', font='slant'), 'cyan'))
        print(colored("📌 1. Register", 'yellow'))
        print(colored("🔑 2. Login", 'yellow'))
        print(colored("🔄 3. Reset Password", 'yellow'))
        print(colored("❌ 0. Exit", 'yellow'))

        choice = input(colored("🤖 Pilih opsi: ", 'yellow'))

        if choice == '1':
            register()
            time.sleep(2)
        elif choice == '2':
            if login():
                break
            time.sleep(2)
        elif choice == '3':
            reset_password()
            time.sleep(2)
        elif choice == '0':
            print(colored("Goodbye!", 'cyan'))
            time.sleep(1)
            os.system('clear')
            break
        else:
            print(colored("❌ Invalid option. Try again.", 'red'))
            time.sleep(2)

if __name__ == "__main__":
    main()
