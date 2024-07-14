from .models import Session, Product

class DatabaseManager:
    def __init__(self):
        self.session = Session()

    def get_all_products(self):
        return self.session.query(Product).all()

    def get_product(self, name):
        return self.session.query(Product).filter_by(name=name).first()

    def update_stock(self, name, quantity):
        product = self.get_product(name)
        if product:
            product.stock -= quantity
            self.session.commit()
            return True
        return False

    def add_product(self, name, price, stock):
        product = Product(name=name, price=price, stock=stock)
        self.session.add(product)
        self.session.commit()

    def close(self):
        self.session.close()