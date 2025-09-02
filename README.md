# 🛡️ Sentinel

Detect and analyze phishing websites from the command line or web dashboard.  

**Sentinel** is a powerful security tool designed to identify phishing websites, analyze suspicious domains, and provide detailed visualizations.  
It offers both a **command-line interface (CLI)** utility and a **web-based dashboard** powered by FastAPI.

---

## ✨ Features

- 🔍 **Phishing Detection** – Quickly identify suspicious websites.  
- 🖥️ **CLI Tool** – Perform fast scanning and analysis directly from the terminal.  
- 🌐 **Web Dashboard** – Intuitive FastAPI-powered interface with rich data visualization.  
- 📊 **Analysis & Charts** – Access domain details, SSL/TLS information, WHOIS data, and risk assessments.  
- ⚡ **Dual Interface** – Seamlessly switch between CLI and web interfaces based on your workflow.  

---

## 🛠 Installation

Follow these steps to set up Sentinel on your system:

### 1. Clone the Repository
```bash
git clone https://github.com/Fawz-Haaroon/sentinel.git
cd sentinel
```

### 2. Create and Activate a Virtual Environment

```
python -m venv .venv
```
### Activate it:

#### Linux/macOS:
```
source .venv/bin/activate
```
#### Windows (PowerShell):
```
.venv\Scripts\Activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Install Sentinel
```
pip install -e .
```
#### Now you can run Sentinel from anywhere using:
```
sentinel
```
#### Check available commands:
```
sentinel --help
```

## 🚀 Usage

## CLI Mode
#### Run phishing detection or website analysis directly from the terminal:

#### Check if a site is potentially phishing:
```bash
sentinel detect https://suspicious-site.com
```

#### Run full analysis on a site:
```
sentinel analyze https://example.com
```

## Server Mode
#### Launch the web dashboard:
```
sentinel serve
```

### 🛠 Development
#### Sentinel uses a Makefile to streamline common development tasks.

#### Available Commands
```
make venv     # Create a virtual environment
make install  # Install dependencies inside venv
make dev      # Run the app in development mode (with reload)
make run      # Run the app in production mode
make test     # Run pytest
make clean    # Remove cache and build files
make help     # Show available commands
```

### Typical Workflow

#### Set up environment and install dependencies:

```
make install
```

#### Run the development server:
```
make dev
```

#### Run tests:
```
make test
```

### 📊 Example Dashboard Features

- Website Risk Score Visualization – View risk levels in intuitive charts.
- SSL Certificate Validity Timelines – Monitor certificate status and expiration.
- Domain Registrar & WHOIS Lookup Results – Access detailed domain information.
- Suspicious Keyword/Content Detection – Identify potentially malicious content.

### 🔮 Roadmap

- Integrate real-time threat intelligence APIs.
- Add support for batch scanning of multiple URLs.
- Enable report exports to PDF/CSV formats.

### 🤝 Contributing

We welcome contributions! To get started:

1. Fork the repository.
2. Create a feature branch for your changes.
3. Submit a pull request with your improvements.

### 📜 License

Sentinel is licensed under the MIT License – free to use and modify.
