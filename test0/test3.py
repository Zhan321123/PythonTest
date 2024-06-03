import numpy as np
from pandas import Timestamp
from lib.excel import *

A = SingleSheetExcelReader('water/A.xlsx', header=0)
B = SingleSheetExcelReader('water/B.xlsx', header=0)

