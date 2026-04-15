# LanceIQ ONDC LOG10 Certification Logs

These JSON payloads are the sanitized LOG10 `2.0.0` reference logs for LanceIQ's B2B Domestic Logistics provider path.

## Submission Path

Use the repository root as the Git repository path in the ONDC portal, then reference this folder:

`logs/log10`

## Scope

- Domain: `ONDC:LOG10`
- Version: `2.0.0`
- Role: LSP / BPP / provider-side logistics node
- Subscriber: `lanceiq.com`
- Subscriber URL: `https://lanceiq.com/api/ondc/inbound`

## Core Workflow Logs

Located in `logs/log10/core`:

- `search.json`
- `on_search.json`
- `select.json`
- `on_select.json`
- `init.json`
- `on_init.json`
- `confirm.json`
- `on_confirm.json`
- `status.json`
- `on_status.json`
- `cancel.json`
- `on_cancel.json`

## IGM Workflow Logs

Located in `logs/log10/igm`:

- `issue.json`
- `on_issue.json`
- `issue_status.json`
- `on_issue_status.json`

## Notes

These logs are safe to commit. They do not contain private keys, authorization headers, real customer data, or production shipment details.
