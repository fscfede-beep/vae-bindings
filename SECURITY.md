# Security policy

## Scope

This repository publishes privacy-preserving commitments and workflow attestations around agent work-unit bindings. Private reveals and local trust policy are intentionally outside Git.

Security-relevant reports include:
- disclosure of raw private identifiers or reveal material;
- commitment or attestation integrity failures;
- workflow scope or identity-validation bypasses;
- privacy-gate bypasses;
- unintended secret or credential exposure.

## Report privately

Use GitHub's **Report a vulnerability** flow under the repository Security tab. Private vulnerability reporting is enabled for this repository.

Do not disclose an unpatched vulnerability in a public issue. Include the affected commit, reproduction steps, impact, and only the minimum data needed to demonstrate the problem.

## Supported version

Security fixes target current `main` and the latest public binding/attestation mechanism.

## Boundaries

This repository demonstrates a public commitment-and-attestation mechanism. It does not prove private sidecar contents, provider authenticity beyond published commitments, economic value, or production deployment.
