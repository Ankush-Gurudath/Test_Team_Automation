import logging
import sys
import os
import datetime

log_file = None
log_directory = "results/logs"
log_file_pre_name = log_directory + "/automation"

class PackagePathFilter(logging.Filter):
    def filter(self, record):
        pathname = record.pathname
        record.relativepath = None
        abs_sys_paths = map(os.path.abspath, sys.path)
        for path in sorted(abs_sys_paths, key=len, reverse=True):
            if not path.endswith(os.sep):
                path += os.sep
            if pathname.startswith(path):
                record.relativepath = os.path.relpath(pathname, path)
                break
        return True

def setup_log_file():
    if not os.path.exists(log_directory):
        os.makedirs(log_directory, exist_ok=True)
    remove_log_file()
    time = datetime.datetime.now()
    global log_file, log_file_pre_name
    log_file = log_file_pre_name + "_" + time.strftime('%Y-%m-%d_%H_%M_%S.log')

def remove_log_file():
    global log_file_pre_name
    if os.path.exists(log_file_pre_name + ".log"):
        try:
            os.remove(log_file_pre_name + ".log")
        except FileNotFoundError:
            pass # Log file was already removed. So nothing to do

def logger(name):
    global log_file, log_file_pre_name
    if(log_file == None):
        setup_log_file()
    
    logger = logging.getLogger(name)
    logger.propagate = False
    
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    log_file_handler = logging.FileHandler(log_file)
    common_log_file_handler = logging.FileHandler(log_file_pre_name + ".log")
    stdout_handler.addFilter(PackagePathFilter())
    log_file_handler.addFilter(PackagePathFilter())
    common_log_file_handler.addFilter(PackagePathFilter())
    format_output = logging.Formatter('%(asctime)s : %(levelname)s : %(relativepath)s : %(funcName)s : %(lineno)d : %(message)s') # <-
    stdout_handler.setFormatter(format_output)
    log_file_handler.setFormatter(format_output)
    common_log_file_handler.setFormatter(format_output)
    logger.addHandler(stdout_handler)
    logger.addHandler(log_file_handler)
    logger.addHandler(common_log_file_handler)
    return logger

log = logger(__name__)