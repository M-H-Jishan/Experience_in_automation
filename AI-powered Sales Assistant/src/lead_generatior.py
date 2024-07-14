import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class LeadGenerator:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train_model(self, data):
        # Assuming 'data' is a pandas DataFrame with features and a 'is_lead' column
        X = data.drop('is_lead', axis=1)
        y = data['is_lead']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)

    def generate_leads(self, potential_leads):
        # 'potential_leads' should be a DataFrame with the same features as the training data
        lead_probabilities = self.model.predict_proba(potential_leads)[:, 1]
        return potential_leads[lead_probabilities > 0.7]  # Adjust threshold as needed

# Usage
lead_gen = LeadGenerator()
lead_gen.train_model(historical_data)
new_leads = lead_gen.generate_leads(potential_leads_data)