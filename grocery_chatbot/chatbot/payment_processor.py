import os
from typing import Tuple

import stripe
from config import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


class PaymentProcessor:
    @staticmethod
    def process_payment(amount: float, token: str) -> Tuple[bool, str]:
        if not STRIPE_API_KEY:
            return False, "STRIPE_API_KEY is not set"
        try:
            stripe.Charge.create(
                amount=int(amount * 100),
                currency="usd",
                source=token,
                description="Grocery purchase",
            )
            return True, "Payment successful!"
        except stripe.error.CardError as e:
            return False, f"Payment failed: {e}"
        except Exception as e:
            return False, f"An error occurred: {e}"
