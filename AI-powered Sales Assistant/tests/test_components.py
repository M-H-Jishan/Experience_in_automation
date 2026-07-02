import numpy as np
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestLeadGenerator:
    def test_init(self):
        from src.lead_generator import LeadGenerator
        lg = LeadGenerator()
        assert lg.model is not None

    def test_train_and_generate(self):
        from src.lead_generator import LeadGenerator
        lg = LeadGenerator()
        data = pd.DataFrame({
            "age": [25, 30, 35, 40, 45, 50, 55, 60],
            "income": [50000 + i * 10000 for i in range(8)],
            "is_lead": [1, 0, 1, 0, 1, 0, 1, 0],
        })
        lg.train_model(data)
        result = lg.generate_leads(data.drop("is_lead", axis=1))
        assert isinstance(result, pd.DataFrame)


class TestRecommendationEngine:
    def test_init(self):
        from src.recommendation_engine import RecommendationEngine
        re = RecommendationEngine(n_clusters=3)
        assert re.kmeans.n_clusters == 3

    def test_train_and_predict(self):
        from src.recommendation_engine import RecommendationEngine
        re = RecommendationEngine(n_clusters=3)
        data = np.random.rand(20, 3)
        re.train(data)
        result = re.get_recommendations([0.5, 0.5, 0.5])
        assert "cluster" in result


class TestEmailAutomation:
    def test_init(self):
        from src.email_automation import EmailAutomation
        ea = EmailAutomation("test@test.com", "pass")
        assert ea.email == "test@test.com"

    def test_generate_email(self):
        from src.email_automation import EmailAutomation
        ea = EmailAutomation("test@test.com", "pass")
        msg = ea.generate_email("recipient@test.com", "Subject", "Body")
        assert msg["Subject"] == "Subject"


class TestSalesAssistant:
    def test_init(self):
        from src.sales_assistant import SalesAssistant
        sa = SalesAssistant(None, None, None, None)
        assert sa.lead_gen is None
