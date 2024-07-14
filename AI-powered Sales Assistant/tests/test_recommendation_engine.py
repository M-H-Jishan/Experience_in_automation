import unittest
import numpy as np
from src.recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.recommendation_engine = RecommendationEngine(n_clusters=3)
        self.sample_data = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [2, 3, 4],
            [5, 6, 7],
            [8, 9, 10]
        ])

    def test_train(self):
        self.recommendation_engine.train(self.sample_data)
        self.assertIsNotNone(self.recommendation_engine.kmeans.cluster_centers_)

    def test_get_recommendations(self):
        self.recommendation_engine.train(self.sample_data)
        new_customer = [3, 4, 5]
        recommendation = self.recommendation_engine.get_recommendations(new_customer)
        self.assertIsInstance(recommendation, str)
        self.assertTrue(recommendation.startswith("Recommendations for cluster"))

if __name__ == '__main__':
    unittest.main()