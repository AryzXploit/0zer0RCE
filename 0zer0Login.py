#!/usr/bin/python3
# 0zer0Login.py - User Authentication for 0zer0RCE
# Author: AryzXploit

import os
import json
import pyfiglet
import time
import random
import string
from datetime import datetime, timedelta
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
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def save_token(token):
    token_data = {
        "token": token,
        "created_at": datetime.now().isoformat()
    }
    with open(auth_status_file, 'w') as file:
        json.dump(token_data, file)

def load_token():
    if not os.path.exists(auth_status_file):
        return None
    with open(auth_status_file, 'r') as file:
        return json.load(file)

def is_token_expired():
    token_data = load_token()
    if not token_data:
        return True
    created_at = datetime.fromisoformat(token_data["created_at"])
    return datetime.now() > created_at + timedelta(hours=24)

def login():
    session_data = load_session()
    if not session_data:
        print(colored("❌ No user registered. Please register first.", 'red'))
        return False

    print(colored(pyfiglet.figlet_format('Login-Pages', font='slant'), 'magenta'))
    print(colored("\n🔑 LOGIN", 'yellow'))
    username = input("Username: ")
    password = input("Password: ")

    if session_data['username'] == username and session_data['password'] == password:
        print(colored("✅ Login successful!", 'green'))
        
        if is_token_expired():
            token = generate_token()
            save_token(token)
            print(colored(f"🆕 New token generated: {token}", 'cyan'))
        else:
            token = load_token()["token"]
            print(colored(f"🔑 Your current token: {token}", 'cyan'))

        time.sleep(2)
        os.system('clear')
        return True
    else:
        print(colored("❌ Invalid credentials.", 'red'))
        return False

def main():
    setup_secret_path()
    while True:
        os.system('clear')
        print(colored(pyfiglet.figlet_format('0zer0RCE Auth', font='slant'), 'cyan'))
        print(colored("🔑 1. Login", 'yellow'))
        print(colored("❌ 0. Exit", 'yellow'))

        choice = input(colored("🤖 Pilih opsi: ", 'yellow'))

        if choice == '1':
            if login():
                break
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
