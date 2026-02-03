import sys
import os
from utils import logging_util

log = logging_util.logger(__name__)

#If env not given, default will be below
property_file = 'properties/automation_int.properties'
env = 'int'

all_arguments = sys.argv
properties = {}

def load_environment():
    global property_file
    env = load_property_from_commandline_argument('env')
    log.info("Given env was: %s", env)
    if env != None and env != "":
        env = env.lower()
        if env == 'int' or env == 'stg' or env == 'prod':
            property_file = 'properties/automation_' + env + '.properties'
        else:
            log.error("Invalid env " + env + " was given, Please give int or stg or prod")
            exit ("Invalid env " + env + " was given, Please give int or stg or prod")
    else:
        log.info("No env was given. So using default env: int")
        env = 'int'
    log.info("Property file used was:" + property_file)

def load_property_from_environment_variable(key):
     value = None
     if os.environ.get(key) != None and os.environ.get(key) != "":
         value = os.environ.get(key)
     return value

def load_property_from_commandline_argument(key):
     value = None
     for arg in all_arguments:
        if arg.startswith('--' + key):
            value = arg[arg.index('=') + 1:]
            break
     return value

def load_property():
    all_properties = open(property_file)
    for each_property in all_properties:
        each_property = each_property.replace('\n', '')
        property_key = each_property[:each_property.index('=')]
        property_value = each_property[each_property.index('=') + 1:len(each_property)]
        property_value_in_environment_variable = load_property_from_environment_variable(property_key)
        if property_value_in_environment_variable != None and property_value_in_environment_variable != "":
            property_value = property_value_in_environment_variable
        property_value_in_cmd = load_property_from_commandline_argument(property_key)
        if property_value_in_cmd != None and property_value_in_cmd != "":
            property_value = property_value_in_cmd
        properties[property_key] = property_value
    for key, val in properties.items():
        log.info(key + "=" + val)

def get_value(key):
    return properties[key]

def get_value_or_default(key, default_value):
    value = properties[key]
    if value == None or value == "":
        value = default_value
    return value