import unittest

from user import User


class TestUser(unittest.TestCase):
    def test_new_user(self):
        user = User("User Name")
        self.assertEqual(user.name, "User Name")

    # def test_add_assignment(self):
    #     user = User("User Name")
    #     assignment =
    #     user.add_assignment()


if __name__ == '__main__':
    unittest.main()
