import unittest

from hello import greet


class GreetTest(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_name(self):
        self.assertEqual(greet("OVHcloud"), "Hello, OVHcloud!")


if __name__ == "__main__":
    unittest.main()
