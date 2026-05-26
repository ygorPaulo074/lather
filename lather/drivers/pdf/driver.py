"""
drivers/pdf/driver.py
=====================

Concrete driver for PDF files.

Implements `BaseDriver` using `pdfplumber` to extract native text from
PDFs, page by page. Images are intentionally ignored at the Core level
— OCR and image extraction are out of scope for this driver and may be
addressed by separate, specialized drivers in the future.

This driver's only responsibility is faithful text extraction from the
PDF. Limits (`data_limit`), privacy filtering and Markdown rendering all
happen later, in the core pipeline.
"""

from ..base import BaseDriver


class PdfDriver(BaseDriver):
    """
    Driver responsible for reading native-text PDF files.

    Implementation notes:
        - Uses `pdfplumber` to open the file and iterate over its pages.
        - For each page, extracts plain text and, when applicable,
          structured tables.
        - Skips embedded images (no OCR happens here).
        - Returns an intermediate structure that `SemanticRenderer` knows
          how to consume (typically a dict containing metadata + an
          ordered list of pages, each holding text and tables).
    """

    # Extensions handled by this driver. Consumed by the DriverRegistry
    # to populate its internal mapping.
    extensions = [".pdf"]

    def read(self, source: str) -> str:
        """
        Read a PDF file from `source` and return its extracted content.

        Expected flow:
            1. Open the PDF using `pdfplumber`.
            2. Iterate over the pages preserving the original order.
            3. For each page:
                a. Extract native text.
                b. Extract tables (if any) preserving rows/columns.
                c. Ignore images.
            4. Aggregate everything into an intermediate structure
               containing document metadata (file name, page count) +
               ordered list of pages.

        Parameters:
            source: PDF file path (absolute or relative).

        Returns:
            Intermediate structure that `SemanticRenderer` will turn into
            structured Markdown.
        """
        # Open the PDF with pdfplumber, iterate over pages, extract text + tables,
        # and assemble the intermediate structure consumed by the renderer.
        pass
