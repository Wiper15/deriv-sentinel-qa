# 🛡️ Deriv Sentinel QA
> **Software 3.0 Autonomous QA & Compliance Ecosystem**

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-Credits-blue?logo=google-cloud)](https://cloud.google.com)
[![Gemini 1.5](https://img.shields.io/badge/Model-Gemini_1.5_Pro-purple)](https://deepmind.google/technologies/gemini/)

## 🚀 Overview
**Deriv Sentinel QA** is an autonomous "Software 3.0" system built for high-stakes fintech environments. It doesn't just run tests; it **reasons** through them. By utilizing a multi-agent loop on **Google Cloud Vertex AI**, it self-heals broken test scripts and enforces **PCI DSS 4.0** and **GDPR** compliance at the point of creation.

---

## ✅ Problem Statement
Traditional QA in fintech is brittle and carries high security risks:
1. **The Maintenance Trap:** Static scripts break during UI updates, creating "false alarms" that stall deployment.
2. **Compliance Risks:** Automated tests often bypass security protocols or accidentally leak PII (Personally Identifiable Information) into logs.
**Sentinel QA** solves this by making security and compliance an autonomous "gatekeeper" in the development lifecycle.

---

## 📸 Solution Flow
Our architecture follows an agentic pattern, ensuring no code is executed without a compliance audit.

1. **Architect Agent (Gemini 1.5 Pro):** Translates user requirements into Playwright/Python code.
2. **Sentinel Auditor (Gemini 1.5 Flash + RAG):** Audits code against a **Compliance Vault** (stored in Vertex AI Search).
3. **Execution Sandbox (Cloud Run):** Runs approved code in a secure, headless environment.
4. **Self-Healing Loop:** If a test fails due to a UI change, the agent re-inspects the DOM and patches the script automatically.

---

## 🛠️ Implementation & Architecture
### Technical Stack
* **Orchestration:** Python-based state machine logic.
* **AI Engine:** Google Vertex AI (Gemini 1.5 Pro & Flash).
* **Compliance RAG:** Vertex AI Search grounded in **PCI DSS** & **GDPR** documentation.
* **Execution:** Playwright (Python) running in a serverless sandbox.

### Engineering Judgment (Clean Code)
* **Separation of Concerns:** Distinct logic for `architect.py` (Creation) and `sentinel.py` (Audit).
* **Security-First:** No hardcoded API keys; utilizes Google **Application Default Credentials (ADC)**.
* **Traceability:** Logs capture the "Chain of Thought" for every AI decision.

---

## ⚙️ Installation & Usage
### Prerequisites
- A Google Cloud Project with **Vertex AI API** enabled.
- Python 3.9+

### Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/deriv-sentinel-qa.git
   cd deriv-sentinel-qa
