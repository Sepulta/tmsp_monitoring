import tmsp_monitoring.datasource as datasource
import os
from os.path import join

class FermiDatasource(dataource.Datasource):
    def __init__(self):
        super().__init__()
        self.base = join(self.base, "fermi")
        if not os.path.exists(self.base):
            os.makedirs(self.base)
        self.photons_location = join(self.base, "all-photons")
        if not os.path.exists(self.photons_location):
            os.makedirs(self.photons_location)
