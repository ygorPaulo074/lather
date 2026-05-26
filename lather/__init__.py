"""
lather
======

Public entry point of the SDK.

This module exposes the `Lather` class, which is the main interface for
using the library. All end-user interaction with the SDK must go through
this namespace — internal modules (`core`, `drivers`, `limits`) are
implementation details and should not be imported directly by consumers.

Expected usage:

    from lather import Lather

    lather = Lather()
    lather.configure({
        "privacy":    False,
        "data_limit": "medium",
        "drivers":    ["pdf"],
    })
    lather.read("contrato.pdf")
    result = lather.dump()
"""

# Re-export the Lather class from the core module so consumers can simply
# do `from lather import Lather` without knowing the internal layout.
# from .core.lather import Lather

# __all__ defines what is considered the public API of this SDK.
# __all__ = ["Lather"]
