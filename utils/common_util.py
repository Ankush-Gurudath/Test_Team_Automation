from utils import logging_util

log = logging_util.logger(__name__)
class LocatorUtil:
    @staticmethod
    def give_locator(locator, *values):
        for index in range(0,len(values)):
            locator = locator.replace("{" + str(index) + "}", values[index])
        return locator