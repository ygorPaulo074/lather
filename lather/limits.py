"""
limits.py
=========

Central catalog of the `data_limit` presets accepted by the SDK configuration.

This file concentrates, in a single place, all the numeric ceilings that
govern how much content the SDK is allowed to extract from a document
before truncating the result. Keeping the limits isolated here avoids
"magic numbers" scattered across the code and makes it easy to tune the
profiles without touching read logic.

Each preset is a dictionary with three fields:

- `max_pages` : maximum number of pages to read from the document.
- `max_rows`  : maximum number of rows to extract from tables.
- `max_chars` : maximum number of text characters returned.

Available presets:

- `testing`   : very low values, intended for fast tests and CI.
- `poor`      : minimal extraction, useful for previews or short prompts.
- `medium`    : recommended default for most use cases.
- `rich`      : broad extraction, for more thorough analyses.
- `unlimited` : no effective ceiling (sentinel values such as `math.inf`
                or `None`); use with care on LLMs with limited context.
"""

# Public dictionary mapping preset name -> ceiling values.
# Consumed by `core/config.py` during validation of `configurations`.
#
# Expected structure (to be filled in during implementation):
#
# DATA_LIMITS = {
#     "testing":   {"max_pages": ..., "max_rows": ..., "max_chars": ...},
#     "poor":      {"max_pages": ..., "max_rows": ..., "max_chars": ...},
#     "medium":    {"max_pages": ..., "max_rows": ..., "max_chars": ...},
#     "rich":      {"max_pages": ..., "max_rows": ..., "max_chars": ...},
#     "unlimited": {"max_pages": ..., "max_rows": ..., "max_chars": ...},
# }
DATA_LIMITS = {}
