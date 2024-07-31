def search_products(category, gift_name, budget):
    # This is a placeholder. You need to implement the actual search logic
    # based on your inventory system and database.
    return [
        {"name": f"{category} Product 1", "price": min(29.99, budget), "url": f"/product1-{category.lower()}"},
        {"name": f"{category} Product 2", "price": min(39.99, budget), "url": f"/product2-{category.lower()}"},
        {"name": f"{category} Product 3", "price": min(49.99, budget), "url": f"/product3-{category.lower()}"},
    ]