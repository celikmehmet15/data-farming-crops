"""Base crop model shared by all crops."""

class Crop:  # pylint: disable=too-few-public-methods
    """Common behavior for all crops."""

    def __init__(self):
        """Initialize crop with zero grains."""
        self.grains = 0

    def ripe(self):
        """Return True if the crop has at least 15 grains."""
        return self.grains >= 15
