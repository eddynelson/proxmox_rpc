import unittest
import os
import sys

sys.path.append('.')
from bin.server import ProxmoxServerRPC

class TestProxmoxServerRPC(unittest.TestCase):
    def setUp(self):
        self._password = '010203'
        self.methods = ProxmoxServerRPC()

    def test_login(self):
        result = self.methods.login(self._password)

        expect = { "message": "Login success!!"  }
        self.assertEqual(result, expect)
        

if __name__ == '__main__':
    unittest.main()