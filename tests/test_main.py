import unittest
import seaborn_command.main


class TestMain(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     # procedures before tests are started. This code block is executed only once
    #     pass

    # @classmethod
    # def tearDownClass(cls):
    #     # procedures after tests are finished. This code block is executed only once
    #     pass

    # def setUp(self):
    #     # procedures before every tests are started. This code block is executed every time
    #     pass

    # def tearDown(self):
    #     # procedures after every tests are finished. This code block is executed every time
    #     pass

    def test_parse_seaborn_args(self):
        expected = {"hue": "species"}
        actual = seaborn_command.main.parse_seaborn_args(["--hue", "species"])
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
