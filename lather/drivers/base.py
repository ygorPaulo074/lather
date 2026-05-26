"""
drivers/base.py
===============

Defines `BaseDriver`: the abstract base class that every driver in the
SDK must inherit from.

A driver is the component that knows how to physically read a specific
file format (PDF, DOCX, CSV, etc.) and turn it into an intermediate
structure suitable for the core pipeline (privacy filter -> data-limit
filter -> renderer).

By forcing every driver through this contract, the rest of the SDK can
treat all formats uniformly. The `DriverRegistry` only needs to know
that any registered class respects this interface — nothing else.
"""

from abc import ABC, abstractmethod


class BaseDriver(ABC):
    """
    Abstract contract that every driver must implement.

    Required interface:
        extensions : list[str]
            Class attribute listing the file extensions handled by this
            driver. Extensions must be lowercase and include the leading
            dot (e.g. [".pdf"]). The registry uses this list to populate
            its internal mapping.

        read(source: str) -> str
            Read the file located at `source` and return the extracted
            content. The exact return shape is a contract between the
            driver and the core pipeline (typically text or a structured
            dict of pages/tables that the renderer knows how to handle).

    Drivers MUST NOT call LLMs nor perform privacy filtering — those
    concerns belong to the core. A driver's only job is to faithfully
    extract content from its target format.
    """

    # List of file extensions handled by this driver.
    # Subclasses must override this attribute (e.g. extensions = [".pdf"]).
    extensions: list = []

    @abstractmethod
    def read(self, source: str) -> str:
        """
        Read the file located at `source` and return the extracted content.

        Parameters:
            source: path of the file to be read (absolute or relative).

        Returns:
            Extracted content. The shape (plain string, dict of pages,
            list of sections, etc.) is defined by the contract agreed
            between the driver and `SemanticRenderer`.

        Concrete drivers must implement this method. The base class
        intentionally provides no default implementation.
        """
        # Concrete drivers must implement file reading specific to their format.
        ...
