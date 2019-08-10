import os
from os.path import join
from tmsp_monitoring.config import locations

from astropy.coordinates import SkyCoord

# TODO: 
# - orbital information
# - add astropy position information
# - add more precision (via catalogue) for optical
# - add radius around object

class PulsarObject(object):
    def __init__(self, Name, SkyPosition):
        self.base = join(locations.base, "datasources")
        if not os.path.exists(self.base):
            os.makedirs(self.base)
        self.Name = Name
        self.SkyPosition = SkyPosition
        self.radius=1

    def __str__(self):
        return self.Name

    def display_coordinates(self):
        return self.SkyPosition

class FermiPulsarObject(PulsarObject):
    def __init__(self, Name, SkyPosition):
        super().__init__(Name, SkyPosition)




PulsarSet = [
		  FermiPulsarObject('PSR J0002+6216', SkyCoord(0.74, 62.27, frame='icrs', unit='deg'))
        ]
