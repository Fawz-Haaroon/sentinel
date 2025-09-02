Sentinel 🛡️

Detect and analyze phishing websites from the command line or web dashboard.

Sentinel is a security tool with both a CLI utility and a web-based dashboard powered by FastAPI.
It helps you detect phishing websites, analyze suspicious domains, and visualize site information with charts and reports.


---

✨ Features

🔍 Phishing Detection – Identify suspicious websites.

🖥️ CLI Tool – Quick scanning and analysis from the terminal.

🌐 Web Dashboard – FastAPI-powered interface with data visualization.

📊 Analysis & Charts – Get domain details, SSL/TLS info, WHOIS data, and risk levels.

⚡ Dual Interface – Use either CLI or web, depending on your workflow.



---
### 1. Clone the Repository  

```bash
git clone https://github.com/Fawz-Haaroon/sentinel.git
cd sentinel
```

### 2. Create and Activate a Virtual Environment

python -m venv .venv

Activate it:

Linux/macOS

source .venv/bin/activate

Windows (PowerShell)

.venv\Scripts\Activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Install Sentinel

pip install -e .

Now you can run Sentinel from anywhere with: sentinel

Try:
sentinel --help

---

🚀 Usage

#### CLI Mode

Run phishing detection or website analysis directly:

## Check if a site is potentially phishing
sentinel detect https://suspicious-site.com

## Run full analysis on a site
sentinel analyze https://example.com

#### SERVER Mode
sentinel serve

---
## 🛠 Development  

This project uses a **Makefile** to simplify common tasks.  

### Available Commands  

```bash
make venv     # Create a virtual environment
make install  # Install dependencies inside venv
make dev      # Run the app in development mode (with reload)
make run      # Run the app in production mode
make test     # Run pytest
make clean    # Remove cache and build files
make help     # Show available commands

Typical Workflow

# 1. Setup environment & install dependencies
make install  

# 2. Run development server
make dev  

# 3. Run tests
make test
```
---

📊 Example Dashboard

Website risk score visualization.

SSL certificate validity timelines.

Domain registrar & WHOIS lookup results.

Suspicious keyword/content detection.

---

🔮 Roadmap

[ ] Add real-time threat intelligence API integration.

[ ] Support batch scanning of multiple URLs.

[ ] Export reports to PDF/CSV.

---

🤝 Contributing

Contributions are welcome!

1. Fork the repo


2. Create a feature branch


3. Submit a pull request


---

📜 License

MIT License – free to use and modify.

---
