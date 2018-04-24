import configparser
import sys
import os
from os.path import expanduser, join
home = expanduser("~")

# FIXME: deal with being imported as a module from some other context
config_file_name = join(home,".tmsp_monitoring")

if not os.path.exists(config_file_name):
    default_config = configparser.ConfigParser()
    default_config['Paths'] = dict(
        data_storage = join(sys.path[0], 'data'))
    with open(config_file_name, "wt") as f:
        default_config.write(f)

config = configparser.ConfigParser()
config.read(config_file_name)

class Locations(object):
    def __init__(self):
        self.base = config['Paths']['data_storage']


locations = Locations()
