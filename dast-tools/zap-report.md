# 🧪 OWASP ZAP DAST Scan Report

## Overview
This report summarizes the results of a dynamic analysis scan performed using OWASP ZAP against the Flask app hosted at `http://127.0.0.1:5000`.

## Scan Details
- **Tool**: OWASP ZAP Baseline Scan
- **Method**: GitHub Actions workflow (`zap-dast.yml`)
- **Target**: `http://127.0.0.1:5000`
- **Trigger**: Manual (`workflow_dispatch`)

## Findings Summary

| Alert Name           | Risk Level | URL                            | Description                          |
|----------------------|------------|----------------------------------|--------------------------------------|
| Reflected XSS        | Medium     | `/vulnerable?input=test`        | Input reflected without sanitization |
| Missing CSP Header   | Low        | `/`                              | No Content Security Policy detected  |

## Remediation Notes
- Reflected XSS was patched using `flask.escape()`
- CSP header can be added via Flask response headers

## Status
✅ Scan completed  
✅ Vulnerabilities documented  
🔜 Additional hardening planned
