# SBOM Automation

This module adds automated SBOM generation and vulnerability scanning to the CI/CD pipeline.

- **Syft** generates a Software Bill of Materials from source code
- **Grype** scans the SBOM for known vulnerabilities (CVEs)

The workflow runs on every push to `main`, ensuring supply chain visibility and continuous dependency hygiene.

Tools:
- [Syft](https://github.com/anchore/syft)
- [Grype](https://github.com/anchore/grype)

Impact:
- Aligns with modern security standards (e.g. Executive Order 14028, NIST guidance)
- Demonstrates awareness of third-party risk and software composition analysis
