# 🛡️ PROJECT BLACKOUT: Hybrid OSINT Investigator

## 🛠️ System Requirements
To ensure the environment operates at peak performance, the following specifications are required:
* **Operating System:** Windows 10/11 or Linux (Kali/Debian preferred).
* **Compiler:** GCC (MinGW) for compiling the C-based core.
* **Runtimes:** VcRuntime140
* **Network:** Stable internet connection (VPN recommended for OpSec).

## 📝 About the Program
This is a high-performance **Hybrid Reconnaissance Suite**. It integrates a **C-based Controller** with a **Python-driven OSINT Engine**. The program automates the process of digital forensics and nickname tracking across over 300 global platforms. It features an integrated Web Application Firewall (WAF) and SQL persistence to log investigation history securely while filtering out noise and false positives.

---

## 🚀 Step-by-Step Installation Guide

Follow these steps in the exact order to ensure all critical components are linked:

### 1. Install Python 3.14
Download and install **Python 3.14**. During installation, make sure to check the box **"Add Python to PATH"**. This is essential for the C core to trigger Python scripts.

### 2. Setup Sherlock Engine
Clone or download the **Sherlock** engine into the `/core` directory of this project. This provides the primary search logic used by the investigator.

### 3. Initialize Local Environment
Open your terminal in the project's root directory and execute the mandatory linking command:
```bash
python3 -m pip install .