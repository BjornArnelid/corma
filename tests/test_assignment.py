import unittest

from assginment import Task, Assignment


class TestTask(Task):
    pass


class TestAssignment(unittest.TestCase):
    def test_new_assignment(self):
        assignment = Assignment("TestAssignment", "Assignment description")
        self.assertEqual("TestAssignment", assignment.identifier)
        self.assertEqual("Assignment description", assignment.description)
        self.assertEqual([], assignment.export_actions)

    def test_assignment_refuse_identifier_space(self):
        with self.assertRaises(ValueError):
            Assignment("Test Assignment")


if __name__ == '__main__':
    unittest.main()
