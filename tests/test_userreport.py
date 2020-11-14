import datetime
import unittest

from assginment import Assignment
from timeunit import TimeUnit
from userreport import WorkItem, UserReport


class TestUserReport(unittest.TestCase):
    def test_create_work_item(self):
        test_assignment = Assignment("Test_assignment")
        test_time_unit = TimeUnit(datetime.date.today(), 8)
        work_item = WorkItem(test_assignment, test_time_unit)

        self.assertEqual(test_assignment, work_item.assignment)
        self.assertEqual(test_time_unit, work_item.timeunit)

    def test_create_user_report(self):
        test_item = WorkItem(Assignment("Test_assignment"), TimeUnit(datetime.date.today(), 8))
        test_report = UserReport([test_item])
        self.assertEqual(test_item, test_report.items[0])


if __name__ == '__main__':
    unittest.main()
