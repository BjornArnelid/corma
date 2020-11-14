import datetime
import unittest

from timeunit import TimeUnit


class TestTimeUnit(unittest.TestCase):
    def test_create_time_unit(self):
        date = datetime.date(2020, 12, 12)
        time_unit = TimeUnit(date, 8)
        self.assertEqual(date, time_unit.date)
        self.assertEqual(8, time_unit.hours)


if __name__ == '__main__':
    unittest.main()
