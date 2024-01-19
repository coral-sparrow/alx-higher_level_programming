import unittest

class TestSuccess(unittest.TestCase):
    def always_pass(self):
        self.assertTrue(True)
