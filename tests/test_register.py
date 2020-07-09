import unittest

from input import WorkItem


class TestRegisterTime(unittest.TestCase):
    def test_create_item(self):
        register_name = "register name"
        action = UnitTestAction()

        work_item = WorkItem(register_name, [action])

        self.assertEqual(work_item.name, register_name)
        self.assertIn(action, work_item.actions)


class UnitTestAction(object):
    pass


if __name__ == '__main__':
    unittest.main()
