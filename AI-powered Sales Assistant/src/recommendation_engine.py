import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class RecommendationEngine:
    def __init__(self, n_clusters: int = 5):
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=n_clusters, n_init=10)

    def train(self, customer_data: np.ndarray) -> None:
        scaled_data = self.scaler.fit_transform(customer_data)
        self.kmeans.fit(scaled_data)

    def get_recommendations(self, customer_features: list) -> str:
        scaled_features = self.scaler.transform([customer_features])
        cluster = self.kmeans.predict(scaled_features)[0]
        return f"Recommendations for cluster {cluster}"
