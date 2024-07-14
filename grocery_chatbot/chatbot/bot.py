from .nlp_processor import NLPProcessor
from .dialogue_manager import DialogueManager
from .payment_processor import PaymentProcessor
from database.db_manager import DatabaseManager

class GroceryStoreChatbot:
    def __init__(self):
        self.nlp = NLPProcessor()
        self.dialogue = DialogueManager()
        self.payment = PaymentProcessor()
        self.db = DatabaseManager()
        self.cart = {}

    def greet(self):
        self.dialogue.greet()
        return "Welcome to our online grocery store! How can I help you today?"

    def handle_inquiry(self, user_input):
        intent, item, quantity = self.nlp.process_input(user_input)
        
        if "price" in user_input or "cost" in user_input:
            product = self.db.get_product(item)
            if product:
                return f"The price of {item} is ${product.price:.2f}."
            else:
                return "I'm sorry, I couldn't find that item. Can you please specify which item you're asking about?"
        elif "available" in user_input or "in stock" in user_input:
            product = self.db.get_product(item)
            if product:
                return f"We have {product.stock} {item}(s) in stock."
            else:
                return "I'm sorry, I couldn't find that item. Can you please specify which item you're asking about?"
        elif "hours" in user_input or "open" in user_input:
            return "Our online store is open 24/7 for your convenience!"
        elif "delivery" in user_input:
            return "We offer free delivery for orders over $50, otherwise there's a $5 delivery fee."
        else:
            return "I'm not sure about that. Can you please rephrase your question?"

    def add_to_cart(self, item, quantity):
        product = self.db.get_product(item)
        if product:
            if product.stock >= quantity:
                if item in self.cart:
                    self.cart[item] += quantity
                else:
                    self.cart[item] = quantity
                return f"Added {quantity} {item} to your cart."
            else:
                return f"Sorry, we only have {product.stock} {item}(s) in stock."
        else:
            return f"Sorry, we don't have {item} in our inventory."

    def view_cart(self):
        if not self.cart:
            return "Your cart is empty."
        cart_contents = "Here's what's in your cart:\n"
        total = 0
        for item, quantity in self.cart.items():
            product = self.db.get_product(item)
            subtotal = product.price * quantity
            cart_contents += f"{quantity} x {item}: ${subtotal:.2f}\n"
            total += subtotal
        cart_contents += f"Total: ${total:.2f}"
        return cart_contents

    def checkout(self, payment_token):
        if not self.cart:
            return "Your cart is empty. Please add items before checking out."
        total = sum(self.db.get_product(item).price * quantity for item, quantity in self.cart.items())
        success, message = self.payment.process_payment(total, payment_token)
        if success:
            for item, quantity in self.cart.items():
                self.db.update_stock(item, quantity)
            self.cart.clear()
            return f"Thank you for your order! {message} Your items will be delivered soon."
        else:
            return message

    def respond(self, user_input):
        current_state = self.dialogue.get_state()
        
        if current_state == 'greeting':
            return self.greet()
        elif current_state == 'inquiring':
            response = self.handle_inquiry(user_input)
            if "add to cart" in user_input.lower():
                self.dialogue.shop()
            return response
        elif current_state == 'shopping':
            intent, item, quantity = self.nlp.process_input(user_input)
            if intent == "add":
                return self.add_to_cart(item, quantity)
            elif "view cart" in user_input.lower():
                return self.view_cart()
            elif "checkout" in user_input.lower():
                self.dialogue.finish()
                return "Please provide your payment token to complete the checkout."
            else:
                return "I'm sorry, I didn't understand that. You can add items to your cart, view your cart, or proceed to checkout."
        elif current_state == 'checkout':
            # Assume the user input is the payment token
            response = self.checkout(user_input)
            self.dialogue.reset()
            return response