import stripe
from config import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

class PaymentProcessor:
    @staticmethod
    def process_payment(amount, token):
        try:
            charge = stripe.Charge.create(
                amount=int(amount * 100),  # Stripe uses cents
                currency="usd",
                source=token,
                description="Grocery purchase"
            )
            return True, "Payment successful!"
        except stripe.error.CardError as e:
            return False, f"Payment failed: {str(e)}"
        except Exception as e:
            return False, f"An error occurred: {str(e)}"