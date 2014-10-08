__author__ = 'adm'
from datetime import *
import time


class TimeCounter:
    def get_zero_year(self, seconds):
        current_year = datetime.now().year
        one_year_in_seconds = 365*24*60*60
        years_passed = int(seconds / one_year_in_seconds)
        zero_year = current_year - years_passed
        return zero_year

    def my_get_zero_year(self, seconds_from_zero):
        return (datetime.now() - timedelta(seconds=seconds_from_zero)).year

counter = TimeCounter()
seconds = time.time()
zero_year = counter.get_zero_year(seconds)
print(zero_year)




