"""Unit tests for User model."""
import unittest
from models.user import User, Person

class TestUser(unittest.TestCase):
    
    def test_user_creation(self):
        """User should initialize with name, email, and auto ID."""
        user = User("Alex", "alex@test.com")
        self.assertEqual(user.name, "Alex")
        self.assertEqual(user.email, "alex@test.com")
        self.assertEqual(user.id, 1)
        self.assertEqual(user.projects, [])
    
    def test_email_validation(self):
        """Invalid email should raise ValueError."""
        with self.assertRaises(ValueError):
            User("Bob", "invalid-email")
    
    def test_inheritance(self):
        """User should inherit from Person."""
        user = User("Alex", "alex@test.com")
        self.assertIsInstance(user, Person)
    
    def test_to_dict(self):
        """to_dict should return JSON-serializable dict."""
        user = User("Alex", "alex@test.com")
        result = user.to_dict()
        self.assertEqual(result["name"], "Alex")
        self.assertIn("project_ids", result)

if __name__ == "__main__":
    unittest.main()