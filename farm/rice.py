"""Rice crop implementation."""

from farm.crop import Crop

class Rice(Crop):
    """Rice crop. Watering produces 5 grains; transplanting produces 10 grains."""

    def water(self):
        """Water the rice crop, producing 5 grains."""
        self.grains += 5

    def transplant(self):
        """Transplant the rice crop, producing 10 grains."""
        self.grains += 10
