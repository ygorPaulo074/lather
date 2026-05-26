"""
core/registry.py
================

Defines `DriverRegistry`: the component responsible for mapping file
extensions (e.g. ".pdf", ".docx", ".csv") to the driver class capable of
reading them.

The registry is the SDK's extension point: adding support for a new
format means creating a driver that inherits from `BaseDriver` and
registering it here. The `Lather` class consults the registry on every
`read()` call to figure out which driver to instantiate based on the
given path.

Keeping this mapping isolated avoids coupling `Lather` to specific
drivers and makes it possible to enable/disable drivers via configuration.
"""


class DriverRegistry:
    """
    Maps file extensions to the drivers responsible for reading them.

    The registry is populated at SDK initialization time (usually inside
    `Lather.__init__`) with the built-in drivers. The user-supplied
    `drivers` configuration may be used to filter which drivers are
    effectively enabled in the session.

    Expected attributes (to be defined in the implementation):
        _mapping : dict[str, type[BaseDriver]] — keys are extensions
                   (lowercase, including the dot, e.g. ".pdf") and values
                   are the corresponding driver classes.
    """

    def __init__(self):
        """
        Initialize the registry with an empty mapping.

        Population happens via `register()` or through an external
        bootstrap routine that knows the available drivers.
        """
        # Initialize self._mapping as an empty dict.
        pass

    def register(self, driver_cls) -> None:
        """
        Register a driver class for every extension it declares in its
        `extensions` attribute.

        Parameters:
            driver_cls: class (not instance) inheriting from `BaseDriver`
                        that exposes the `extensions` list.

        On collision (two classes registering the same extension), the
        implementation must define a clear policy — overwrite, raise, or
        warn — rather than silently dropping one of them.
        """
        # For each extension declared by driver_cls, store it in self._mapping.
        pass

    def resolve(self, path: str):
        """
        Receive the file path and return an INSTANCE of the correct driver.

        Expected flow:
            1. Extract the extension from `path` (lowercased).
            2. Look up the corresponding class in `_mapping`.
            3. Instantiate the driver and return it.
            4. If the extension is not registered, raise a descriptive
               exception (e.g. `UnsupportedExtensionError`).

        Important: the registry returns a ready-to-use instance, not a
        class — so the caller doesn't need to know construction details.
        """
        # Extract extension from path, look up the class, and return a ready instance.
        pass
