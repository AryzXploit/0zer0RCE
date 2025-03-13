# 0zer0RCE - Remote Code Execution Scanner & Exploiter

🚀 **0zer0RCE** - Tools keren buat para bug hunter buat nge-scan dan exploitasi RCE (Remote Code Execution) otomatis! Ini bukan tools sembarangan, bro. Ini alat buat para elite buat nge-hack dan exploit dengan mudah. 💀💻

---

## 📌 Fitur
- 🔍 **Single URL Scan:** Scan satu URL buat ngecek kerentanan RCE.
- 🤖 **Nuclei Machine Scanner:** Integrasi langsung sama Nuclei buat scanning CVE yang terdaftar.
- 📜 **List Available RCE Payloads:** Liat payload yang ada beserta CVE ID-nya.
- 🔒 **Auth System:** Aman karena pake authentication check.

---

## 🆕 Update Terbaru (v1.x) - Authentication System
Sekarang **0zer0RCE** udah support sistem login & token authentication buat ningkatin keamanan dan tracking session user.

### 🔄 Update yang Ditambahkan:
1. **🔑 Sistem Login & Register**
   - User sekarang harus **register** sebelum bisa akses tools.
   - Setelah register, user bisa **login** dengan username & password yang udah didaftarin.

2. **🛡️ Token Authentication**
   - Setelah login, sistem bakal **generate token** yang berlaku selama **24 jam**.
   - Token ini disimpan di `~/.0zer0RCE/auth_status.json`.
   - Kalau token expired, user harus **login ulang** buat dapetin token baru.

3. **📂 Penyimpanan Data User**
   - Username & password disimpan di `~/.0zer0RCE/session.json`.
   - Token session disimpan di `~/.0zer0RCE/auth_status.json`.
   - **Semua data terenkripsi & aman buat digunakan.**

---

## 📂 Dependencies
- Python 3.x
- pip3
- Nuclei (https://github.com/projectdiscovery/nuclei)

---

## 💻 Cara Install
Di Linux & Termux:
```bash
chmod +x setup.sh
./setup.sh
```

---

## 🚀 Cara Run
1. **Jalankan 0zer0Login.py untuk Register/Login:**
```bash
python3 0zer0Login.py
```
- Pilih **Register** buat akun baru.
- Pilih **Login** buat masuk dan generate token.

2. **Jalankan tools utama setelah login:**
```bash
0zer0RCE
```

---

## 📌 Cara Gunain Update Baru
### 📥 1. Install/Update Tools
Kalau lo belum install, bisa clone ulang repo atau update via Git:
```bash
git pull origin main
```
Kalau lo manual, cukup replace file `0zer0Login.py` dengan versi terbaru.

---

### 🆕 2. Register Akun (Pertama Kali Pakai)
Kalau belum pernah daftar, jalankan tools dan pilih opsi **Register**:
```bash
python3 0zer0Login.py
```
- Masukin **Username**
- Masukin **Password**
- Kalau berhasil, bakal muncul:
  ```bash
  ✅ Registration successful! Please login.
  ```

---

### 🔑 3. Login & Generate Token
Setelah register, masukin username & password buat login:
```bash
python3 0zer0Login.py
```
- Kalau berhasil login, bakal muncul token:
  ```bash
  ✅ Login successful!
  🔑 Your current token: ABCD1234XYZ
  ```
- Token ini bakal **valid selama 24 jam**.
- Kalau token expired, user harus login ulang buat dapetin token baru.

---

### 📌 4. Cek & Gunain Token di Tools Utama
Di script utama lo (`Start.py` atau tools lain), lo bisa tambahin pengecekan token sebelum user bisa jalanin exploit. Contohnya:

```python
from 0zer0Login import load_token, is_token_expired

if is_token_expired():
    print("❌ Token expired! Please login again.")
    exit()

token = load_token()["token"]
print(f"✅ Token loaded: {token}")
```
Kalau token masih aktif, tools bisa dijalanin tanpa login ulang.

---

## 👥 Tim Pengembang
- AryzXploit (Founder & Lead Developer)
- TimSecc (Contributor!)

---

## 📜 License
Cuman buat pembelajaran. Jangan buat tindakan ilegal, bro! 😜

---

## 🔗 Disclaimer
Gunakan dengan bijak! Penggunaan yang salah tanggung jawab lo sendiri
---
