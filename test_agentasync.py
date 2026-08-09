# test_agentasync.py
"""
Tests for AgentAsync module.
"""

import unittest
from agentasync import AgentAsync

class TestAgentAsync(unittest.TestCase):
    """Test cases for AgentAsync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentAsync()
        self.assertIsInstance(instance, AgentAsync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentAsync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
