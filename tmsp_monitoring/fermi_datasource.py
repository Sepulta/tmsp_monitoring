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
        self.ancillary_location = join(self.base, "ancillary")
        if not os.path.exists(self.ancillary_location):
            os.makedirs(self.ancillary_location)

        self.photons_server = "legacy.gsfc.nasa.gov"
        self.photons_directory = "/fermi/data/lat/weekly/photon/"
        self.spacecraft_directory = "/FTP/fermi/data/lat/mission/spacecraft/"
        self.photon_file_list = join(self.photons_location,"filelist.txt")

    def update_photons(self):
        ftp = FTP(self.photons_server)
        ftp.login()
        for f, data in ftp.mlsd(self.spacecraft_directory):
            lsm_name = "lat_spacecraft_merged.fits"
            if f==lsm_name:
                target = join(self.ancillary_location,lsm_name)
                if (not os.path.exists(target) 
                    or ('size' in data and os.path.getsize(target) != data['size'])):
                    print(f, target)
                    urllib.request.urlretrieve(
                        "ftp://"+self.photons_server+self.spacecraft_directory+"/"+f,
                        filename=target)
        new_photons = False
        photon_files = []
        for f, data in ftp.mlsd(self.photons_directory):
            target = join(self.photons_location,f)
            if f.startswith("lat_photon_weekly"):
                photon_files.append(f)
                if (not os.path.exists(target) 
                    or ('size' in data and os.path.getsize(target) != data['size'])):
                    print(f, target)
                    new_photons = True
                    urllib.request.urlretrieve(
                        "ftp://"+self.photons_server+self.photons_directory+"/"+f,
                        filename=target)
        photon_files.sort()
        
        with open(self.photons_file_list, "wt") as fl:
            for f in photon_files:
                print(f, file=fl)


            
