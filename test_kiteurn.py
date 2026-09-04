# test_kiteurn.py
"""
Tests for KiteUrn module.
"""

import unittest
from kiteurn import KiteUrn

class TestKiteUrn(unittest.TestCase):
    """Test cases for KiteUrn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KiteUrn()
        self.assertIsInstance(instance, KiteUrn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KiteUrn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
