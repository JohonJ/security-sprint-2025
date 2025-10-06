# SBOM Automation

This folder contains SBOM tooling integrated into the CI/CD pipeline using Syft and Grype.

- **Syft** generates a Software Bill of Materials from source code
- **Grype** scans the SBOM for known vulnerabilities (CVEs)

The workflow runs automatically on every push to `main`, ensuring supply chain visibility and continuous dependency scanning.

Tools:
- [Syft](https://github.com/anchore/syft)
- [Grype](https://github.com/anchore/grype)
