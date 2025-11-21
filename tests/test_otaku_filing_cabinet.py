import unittest
import subprocess
import re
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import otaku_filing_cabinet

# lambda function to make feedback messages easier to read
common_msg = lambda msg, expected, actual: f"{msg}\nExpected: {expected}\nActual: {actual}"

clean_spaces = lambda string: re.sub(r"\s+", "", string)

class TestOtakuFilingCabinet(unittest.TestCase):
    def test_