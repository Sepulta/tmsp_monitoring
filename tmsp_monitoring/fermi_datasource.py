import tmsp_monitoring.datasource as datasource
import os
from os.path import join
from ftplib import FTP
import urllib.request

class FermiDatasource(datasource.Datasource):
    def __init__(self):
        super().__init__()
        self.base = join(self.base, "fermi")
        if not os.path.exists(self.base):
            os.makedirs(self.base)
        self.photons_location = join(self.base, "all-photons")
        if not os.path.exists(self.photons_location):
            os.makedirs(self.photons_location)

        self.photons_server = "legacy.gsfc.nasa.gov"
        self.photons_directory = "/fermi/data/lat/weekly/photon/"

    def update_photons(self):
        ftp = FTP(self.photons_server)
        ftp.login()
        for f, data in ftp.mlsd(self.photons_directory):
            target = os.path.join(self.photons_location,f)
            if not os.path.exists(target):
                print(f, target)
                urllib.request.urlretrieve(
                    "ftp://"+self.photons_server+self.photons_directory+"/"+f,
                    filename=target)
                                   

