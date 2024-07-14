from lead_generator import LeadGenerator
from email_automation import EmailAutomation
from meeting_scheduler import MeetingScheduler
from recommendation_engine import RecommendationEngine
from sales_assistant import SalesAssistant
import yaml
import pandas as pd
from datetime import datetime, timedelta

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    
    lead_gen = LeadGenerator()
    email_automation = EmailAutomation(config['email']['address'], config['email']['password'])
    meeting_scheduler = MeetingScheduler(config['calendar']['credentials_file'])
    recommendation_engine = RecommendationEngine(n_clusters=config['recommendation']['n_clusters'])
    
    sales_assistant = SalesAssistant(lead_gen, email_automation, meeting_scheduler, recommendation_engine)
    
    # Load and preprocess data
    print("Loading and preprocessing data...")
    historical_data = pd.read_csv('data/raw/historical_leads.csv')
    potential_leads_data = pd.read_csv('data/raw/potential_leads.csv')
    
    # Train the lead generation model
    print("Training lead generation model...")
    lead_gen.train_model(historical_data)
    
    # Generate new leads
    print("Generating new leads...")
    new_leads = sales_assistant.process_leads(potential_leads_data)
    print(f"Generated {len(new_leads)} new leads.")
    
    # Train the recommendation engine
    print("Training recommendation engine...")
    customer_data = pd.read_csv('data/raw/customer_data.csv')
    recommendation_engine.train(customer_data)
    
    # Process each new lead
    for lead in new_leads:
        print(f"\nProcessing lead: {lead['email']}")
        
        # Get personalized recommendations
        recommendations = recommendation_engine.get_recommendations(lead)
        print(f"Generated recommendations: {recommendations}")
        
        # Send follow-up email
        email_body = f"Dear {lead['name']},\n\nBased on our analysis, we recommend: {recommendations}\n\nWould you like to schedule a call to discuss further?\n\nBest regards,\nYour Sales Team"
        email_automation.send_email(lead['email'], 'Personalized Recommendations', email_body)
        print(f"Sent follow-up email to {lead['email']}")
        
        # Schedule a follow-up call (1 week from now)
        start_time = datetime.now() + timedelta(days=7)
        end_time = start_time + timedelta(hours=1)
        meeting = sales_assistant.schedule_follow_up(lead['email'], start_time, end_time)
        print(f"Scheduled follow-up call: {meeting['id']}")
    
    print("\nSales assistant process completed successfully!")

if __name__ == "__main__":
    main()
    
if __name__ == "__main__":
    main()