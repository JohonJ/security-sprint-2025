# 🧪 Semgrep SAST Scan Report

## Overview
This report documents the results of a Semgrep static analysis scan performed on the Flask app located in `ci-cd-pipeline/app.py`. The scan was triggered via GitHub Actions using the `p/security-audit` ruleset.

## Scan Trigger
- **Tool**: Semgrep
- **Method**: GitHub Actions CI/CD pipeline
- **Config**: `p/security-audit`
- **Branch**: `main`
- **Trigger**: Push to main / Pull Request

## Findings Summary

| Rule ID               | Severity | Location           | Description                                |
|-----------------------|----------|--------------------|--------------------------------------------|
| flask.xss-reflection  | Medium   | app.py:10          | Reflected user input without sanitization  |
| subprocess.shell      | High     | *(none detected)*  | *(No shell execution found)*               |

## Sample Finding

```plaintext
Rule: flask.xss-reflection
File: ci-cd-pipeline/app.py
Line: 10
Message: User input is reflected without sanitization, which may lead to XSS.
