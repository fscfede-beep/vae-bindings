# Contributing

This repository is deliberately narrow: it publishes privacy-preserving commitments and workflow attestations for agent work-unit bindings.

## Suitable contributions

- privacy-gate fixes and regression coverage;
- attestation-scope and identity-validation improvements;
- documentation that makes the public commitment mechanism easier to verify;
- narrowly scoped workflow hardening that does not reveal private sidecars.

## Do not include

- raw provider generation/request IDs or work-unit IDs;
- API keys, credentials, or private reveal sidecars;
- private trust-policy material;
- claims that published commitments prove economic value, private sidecar contents, or provider authenticity beyond the documented boundary.

## Before opening a pull request

Run `python scripts/verify_public_privacy.py` with the authorized deny-hash environment available, run `git diff --check`, and preserve the canonical GitHub noreply commit identity required by the privacy gate.

Undisclosed vulnerabilities must use the private **Report a vulnerability** flow.