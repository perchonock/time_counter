from unittest import TestCase
from zero_time import *

__author__ = 'adm'


class TestTimeCounter(TestCase):
    def test_get_current_zero_year(self):
        year_counter = TimeCounter()
        year = year_counter.get_zero_year(0)
        self.assertTrue(year == 2014, "Your method sucks")

    def test_get_previous_zero_year(self):
        year_counter = TimeCounter()
        one_year_in_seconds = 365*24*60*60
        year = year_counter.get_zero_year(one_year_in_seconds)
        self.assertTrue(year == 2013, "Your method sucks")

    def test_get_previous_zero_year3(self):
        year_counter = TimeCounter()
        one_year_in_seconds = 360*24*60*60
        year = year_counter.get_zero_year(one_year_in_seconds)
        self.assertTrue(year == 2013, "Your method sucks")

    def test_get_current_zero_year2(self):
        year_counter = TimeCounter()
        year = year_counter.my_get_zero_year(0)
        self.assertTrue(year == 2014, "Your method sucks")

    def test_get_previous_zero_year2(self):
        year_counter = TimeCounter()
        one_year_in_seconds = 365*24*60*60
        year = year_counter.my_get_zero_year(one_year_in_seconds)
        self.assertTrue(year == 2013, "Your method sucks")

    def test_get_previous_zero_year32(self):
        year_counter = TimeCounter()
        one_year_in_seconds = 360*24*60*60
        year = year_counter.my_get_zero_year(one_year_in_seconds)
        self.assertTrue(year == 2013, "Your method sucks")

    def test_magic(self):
        year_counter = TimeCounter()
        for sec in range(1, 360*24*60):
            rsec = sec*60*20
            my_year = year_counter.my_get_zero_year(rsec)
            year = year_counter.get_zero_year(rsec)
            self.assertTrue(year == my_year, "Sec " + str(rsec) + " hren")



