import unittest
import pandas as pd
from src.lead_generator import LeadGenerator

class TestLeadGenerator(unittest.TestCase):
    def setUp(self):
        self.lead_gen = LeadGenerator()
        
        # Create sample data
        self.sample_data = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [5, 4, 3, 2, 1],
            'is_lead': [1, 0, 1, 0, 1]
        })
        
        self.potential_leads = pd.DataFrame({
            'feature1': [2, 4, 6],
            'feature2': [4, 2, 0]
        })

    def test_train_model(self):
        self.lead_gen.train_model(self.sample_data)
        self.assertIsNotNone(self.lead_gen.model)

    def test_generate_leads(self):
        self.lead_gen.train_model(self.sample_data)
        new_leads = self.lead_gen.generate_leads(self.potential_leads)
        self.assertIsInstance(new_leads, pd.DataFrame)
        self.assertTrue(len(new_leads) <= len(self.potential_leads))

if __name__ == '__main__':
    unittest.main()