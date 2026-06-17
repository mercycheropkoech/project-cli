import unittest
from datetime import datetime
from models.project import Project

class TestProject(unittest.TestCase):
    
    def test_project_creation(self):
        p = Project("Test", "Desc", "2026-01-01", 1)
        self.assertEqual(p.title, "Test")
        self.assertEqual(p.user_id, 1)
        self.assertIsInstance(p.due_date, datetime)
    
    def test_invalid_date(self):
        
        with self.assertRaises(ValueError):
            Project("Test", "Desc", "not-a-date", 1)
    
    def test_is_overdue(self):
        
        past = Project("Old", "Desc", "2020-01-01", 1)
        self.assertTrue(past.is_overdue)

if __name__ == "__main__":
    unittest.main()