from pony.orm import Optional

from nutrients import Nutrients


class OptimalRangeAge(Nutrients):
    """docstring for Lot"""
    crop = Optional("Crop")
