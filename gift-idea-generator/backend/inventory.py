def search_products(category: str, gift_name: str, budget: float) -> list[dict]:
    return [
        {"name": f"{category} Product 1", "price": min(29.99, budget), "url": f"/product1-{category.lower()}"},
        {"name": f"{category} Product 2", "price": min(39.99, budget), "url": f"/product2-{category.lower()}"},
        {"name": f"{category} Product 3", "price": min(49.99, budget), "url": f"/product3-{category.lower()}"},
    ]
