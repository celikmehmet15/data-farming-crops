"""Corn crop implementation."""

from farm.crop import Crop

class Corn(Crop):
    """Corn crop. Watering produces 10 grains."""

    def water(self):
        """Water the corn crop, producing 10 grains."""
        self.grains += 10
