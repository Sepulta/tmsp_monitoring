import tmsp_monitoring.config as config
import os
from os.path import join

class Datasource(object):
    def __init__(self):
        self.base = join(config.locations.base, "datasources")
        if not os.path.exists(self.base):
            os.makedirs(self.base)


