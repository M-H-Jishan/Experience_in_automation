import logging
import os
import sys

from dotenv import load_dotenv

from src import LeadGenerator, EmailAutomation, RecommendationEngine, SalesAssistant

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def main():
    logger.info("AI-powered Sales Assistant starting...")

    email_user = os.getenv("EMAIL_USER", "")
    email_password = os.getenv("EMAIL_PASSWORD", "")

    lead_gen = LeadGenerator()
    email_automation = EmailAutomation(email_user, email_password)
    recommendation_engine = RecommendationEngine()

    logger.info("Components initialized. Ready for lead processing.")
    logger.info("Note: Load training data and call process_leads() to begin.")


if __name__ == "__main__":
    main()
