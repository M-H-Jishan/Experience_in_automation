import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


class LeadGenerator:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train_model(self, data: pd.DataFrame) -> None:
        X = data.drop("is_lead", axis=1)
        y = data["is_lead"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)

    def generate_leads(self, potential_leads: pd.DataFrame, threshold: float = 0.7) -> pd.DataFrame:
        lead_probabilities = self.model.predict_proba(potential_leads)[:, 1]
        return potential_leads[lead_probabilities > threshold]
