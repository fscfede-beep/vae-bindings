# VAE Bindings

Dedicated commitment-only authority lane for Verified Agent Economics work-unit bindings.

This repository intentionally contains **no raw provider generation/request IDs, no work-unit IDs, no API keys, and no private reveal sidecars**. Public files under `bindings/*.public.json` contain salted SHA-256 commitments only.

The pinned GitHub Actions workflow attests only binding files added or modified in the triggering push. Private reveals and local trust policy remain outside Git.

Source design: VERIFIED_AGENT_ECONOMICS P2B keyless work-unit binding.
