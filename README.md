# security-sprint-2025
# 🔐 Security Sprint Portfolio – John Freeman

Welcome to my hands-on security portfolio, built during a focused 4-day sprint to deepen expertise in CI/CD, OWASP Top 10, DAST, SAST, SCA, SBOM, and threat modeling. Each folder demonstrates practical skills aligned with application security roles, including automation, vulnerability analysis, and secure SDLC practices.


## 📊 SAST: pip-audit Report

This repo includes a pip-audit scan of the Flask application, identifying known vulnerabilities in dependencies.
📍 [View the full report](sast-tools/pip-audit-report.md)

✅ Key Findings:

- `debug=True` detected in `app.py` → refactored to use environment variable:

```python
  import os
  app.run(debug=os.getenv("FLASK_DEBUG", "False") == "True")
```
- Directly returned format string → replaced with `render_template()` to prevent XSS:
  
```python
  return render_template("response.html", user_input=user_input)
```

## Dynamic Analysis (ZAP)
🌐 OWASP ZAP Report: Dynamic scan of running app  
📄 [`zap-report.html`](./dast-tools/zap-report.html)

📦 SBOM (CycloneDX): Software Bill of Materials for supply chain visibility  
📄 [`sbom.json`](./sast-tools/sbom.json)

# CI/CD Pipeline
Details on GitHub Actions, automated scans, and integration

## Folder Structure
Breakdown of `/sast-tools`, `/dast-tools`, `/ci-cd-pipeline`, etc.

🛠️ Earlier commits failed Semgrep due to unresolved XSS and debug mode. 
✅ All issues remediated and verified in CI as of commit 54023fd.

✅ All vulnerabilities resolved as of Oct 3, 2025.  
Dependencies upgraded based on pip-audit findings:
- Flask → 2.3.2
- requests → 2.32.4
- gunicorn → 22.0.0
- idna → 3.7
- urllib3 → 2.5.0

Tested locally and verified with pip-audit: no known vulnerabilities.

📦 Note: This project uses a virtual environment (`venv-secure`) for dependency isolation.  
To install securely:

```bash
python3 -m venv venv-secure
source venv-secure/bin/activate
pip install -r requirements.txt
```
---

## 🧱 Project Structure

| Folder              | Description                                                  |
|---------------------|--------------------------------------------------------------|
| .github/workflows   | GitHub Actions workflows for CI/CD and security automation   |
| owasp-top10         | Examples and mitigations for OWASP Top 10 vulnerabilities    |
| sast-tools          | Static analysis tools (e.g., Semgrep) and scan reports       |
| dast-tools          | Dynamic analysis tools (e.g., OWASP ZAP) and vulnerability docs |

---

## 🛠️ Tools Used

- **CI/CD**: GitHub Actions
- **SAST**: Semgrep, SonarQube
- **DAST**: OWASP ZAP, Nikto
- **SCA**: Snyk, Dependency-Check
- **Threat Modeling**: OWASP Threat Dragon
- **Cloud**: AWS EC2, S3, IAM
- **SDLC Mapping**: Lucidchart / Draw.io

---

## 📌 Highlights

- Built and secured a CI/CD pipeline with integrated SAST/DAST/SCA tools
- Modeled threats using OWASP frameworks and documented mitigation strategies
- Deployed a sample app to AWS with secure IAM and S3 configurations
- Mapped security controls across SDLC phases for proactive risk management
- Created STAR-format stories with measurable outcomes for interview readiness

---

## 📫 Contact

I'm actively exploring remote security roles and PhD opportunities in AI, robotics, and secure systems. Feel free to reach out!

- **LinkedIn**: [linkedin.com/in/freeman264](https://www.linkedin.com/in/freeman264/)
- **Resume**: [Download PDF](https://drive.google.com/file/d/1EnVf0PyUDh35joEeTBd33E5IVq_vfOgI/view?usp=drive_link)
- **Email**: john.freeman.cyber@gmail.com 

---

## 🚀 Next Steps

- Expand threat modeling to include multi-tier architectures
- Explore Terraform for cloud infrastructure as code
- Contribute to open-source security tools

---

## 🔐 Security Reports

This section highlights vulnerability scans and security tooling used throughout the sprint.

- 📊 [pip-audit Report](sast-tools/pip-audit-report.md): Identifies vulnerable Flask dependencies
- 🧪 [Semgrep Report](sast-tools/semgrep-report.docx): Static analysis of insecure patterns
- 🌐 [OWASP ZAP Report](dast-tools/zap-report.docx): Dynamic scan of running app
- 📦 [SBOM (CycloneDX)](sast-tools/sbom.json): Software Bill of Materials for supply chain visibility

---

## 📊 Repo Status

[![Semgrep Scan](https://img.shields.io/badge/Semgrep-Passed-brightgreen)](https://github.com/JohonJ/security-sprint-2025/actions)
[![ZAP Scan](https://img.shields.io/badge/ZAP-Completed-blue)](https://github.com/JohonJ/security-sprint-2025/actions)
[![Build Status](https://img.shields.io/github/actions/workflow/status/JohonJ/security-sprint-2025/security.yml?branch=main)](https://github.com/JohonJ/security-sprint-2025/actions)
[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Repo Size](https://img.shields.io/github/repo-size/JohonJ/security-sprint-2025)](https://github.com/JohonJ/security-sprint-2025)
[![Last Commit](https://img.shields.io/github/last-commit/JohonJ/security-sprint-2025)](https://github.com/JohonJ/security-sprint-2025/commits/main)
