# VAE Bindings

[![public-privacy-gate](https://github.com/fscfede-beep/vae-bindings/actions/workflows/privacy-gate.yml/badge.svg?branch=main)](https://github.com/fscfede-beep/vae-bindings/actions/workflows/privacy-gate.yml)
[![attest-bindings](https://github.com/fscfede-beep/vae-bindings/actions/workflows/attest-binding.yml/badge.svg?branch=main)](https://github.com/fscfede-beep/vae-bindings/actions/workflows/attest-binding.yml)

A small public reference for **privacy-preserving commitments and attestations around agent work-unit bindings**.

This repository intentionally contains **no raw provider generation/request IDs, no work-unit IDs, no API keys, and no private reveal sidecars**. Public files under `bindings/*.public.json` contain salted SHA-256 commitments only.

The GitHub Actions attestation workflow processes only binding files added or modified in the triggering push. Private reveals and local trust policy remain outside Git.

## What is publicly verifiable

- public binding files contain salted SHA-256 commitments rather than raw private identifiers;
- the privacy gate checks the repository's public-data boundary;
- the attestation workflow is scoped to changed `bindings/*.public.json` files;
- GitHub artifact attestations bind the selected public files to the workflow execution.

A successful public attestation run is archived in [GitHub Actions run #1](https://github.com/fscfede-beep/vae-bindings/actions/runs/33289893844).

## Claim boundary

This repository does **not** reveal or prove the contents of private sidecars, economic value, provider authenticity beyond the published commitments, or production deployment. It demonstrates the public commitment-and-attestation mechanism only.

Source design: VERIFIED_AGENT_ECONOMICS P2B keyless work-unit binding.
