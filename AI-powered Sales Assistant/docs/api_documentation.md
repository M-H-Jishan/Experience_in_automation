# AI-Powered Sales Assistant API Documentation

## Table of Contents

1. [LeadGenerator](#leadgenerator)
2. [EmailAutomation](#emailautomation)
3. [MeetingScheduler](#meetingscheduler)
4. [RecommendationEngine](#recommendationengine)
5. [SalesAssistant](#salesassistant)

## LeadGenerator

The `LeadGenerator` class is responsible for training a machine learning model to identify potential leads and generate new leads based on input data.

### Methods

#### `__init__(self)`

Constructor for the LeadGenerator class.

- **Returns:** None

#### `train_model(self, data: pd.DataFrame) -> None`

Trains the lead generation model using historical data.

- **Parameters:**
  - `data` (pd.DataFrame): A DataFrame containing historical lead data. It should have features columns and an 'is_lead' column indicating whether each entry became a lead.
- **Returns:** None

#### `generate_leads(self, potential_leads: pd.DataFrame) -> pd.DataFrame`

Generates new leads from a set of potential leads using the trained model.

- **Parameters:**
  - `potential_leads` (pd.DataFrame): A DataFrame containing potential lead data with the same feature columns used in training.
- **Returns:**
  - pd.DataFrame: A DataFrame containing the generated leads (a subset of the input data).

## EmailAutomation

The `EmailAutomation` class handles the generation and sending of automated emails.

### Methods

#### `__init__(self, email: str, password: str)`

Constructor for the EmailAutomation class.

- **Parameters:**
  - `email` (str): The email address to send emails from.
  - `password` (str): The password for the email account.
- **Returns:** None

#### `generate_email(self, recipient: str, subject: str, body: str) -> MIMEMultipart`

Generates an email message.

- **Parameters:**
  - `recipient` (str): The recipient's email address.
  - `subject` (str): The subject of the email.
  - `body` (str): The body content of the email.
- **Returns:**
  - MIMEMultipart: An email message object.

#### `send_email(self, recipient: str, subject: str, body: str) -> None`

Sends an email to the specified recipient.

- **Parameters:**
  - `recipient` (str): The recipient's email address.
  - `subject` (str): The subject of the email.
  - `body` (str): The body content of the email.
- **Returns:** None

## MeetingScheduler

The `MeetingScheduler` class integrates with Google Calendar API to schedule meetings.

### Methods

#### `__init__(self, credentials: Credentials)`

Constructor for the MeetingScheduler class.

- **Parameters:**
  - `credentials` (Credentials): Google API credentials object.
- **Returns:** None

#### `schedule_meeting(self, summary: str, start_time: datetime, end_time: datetime, attendees: List[str]) -> dict`

Schedules a meeting on Google Calendar.

- **Parameters:**
  - `summary` (str): The title or summary of the meeting.
  - `start_time` (datetime): The start time of the meeting.
  - `end_time` (datetime): The end time of the meeting.
  - `attendees` (List[str]): A list of attendee email addresses.
- **Returns:**
  - dict: A dictionary containing the created event details.

## RecommendationEngine

The `RecommendationEngine` class uses machine learning to generate personalized recommendations for customers.

### Methods

#### `__init__(self, n_clusters: int = 5)`

Constructor for the RecommendationEngine class.

- **Parameters:**
  - `n_clusters` (int, optional): The number of clusters to use in the K-means algorithm. Defaults to 5.
- **Returns:** None

#### `train(self, customer_data: np.ndarray) -> None`

Trains the recommendation model using customer data.

- **Parameters:**
  - `customer_data` (np.ndarray): An array of customer feature data.
- **Returns:** None

#### `get_recommendations(self, customer_features: List[float]) -> str`

Generates personalized recommendations for a customer.

- **Parameters:**
  - `customer_features` (List[float]): A list of feature values for the customer.
- **Returns:**
  - str: A string containing personalized recommendations.

## SalesAssistant

The `SalesAssistant` class integrates all components to provide a comprehensive sales assistance solution.

### Methods

#### `__init__(self, lead_gen: LeadGenerator, email_automation: EmailAutomation, meeting_scheduler: MeetingScheduler, recommendation_engine: RecommendationEngine)`

Constructor for the SalesAssistant class.

- **Parameters:**
  - `lead_gen` (LeadGenerator): An instance of the LeadGenerator class.
  - `email_automation` (EmailAutomation): An instance of the EmailAutomation class.
  - `meeting_scheduler` (MeetingScheduler): An instance of the MeetingScheduler class.
  - `recommendation_engine` (RecommendationEngine): An instance of the RecommendationEngine class.
- **Returns:** None

#### `process_leads(self, potential_leads: pd.DataFrame) -> pd.DataFrame`

Processes potential leads by generating new leads, creating personalized recommendations, and sending follow-up emails.

- **Parameters:**
  - `potential_leads` (pd.DataFrame): A DataFrame containing potential lead data.
- **Returns:**
  - pd.DataFrame: A DataFrame containing the processed leads.

#### `schedule_follow_up(self, lead_email: str, start_time: datetime, end_time: datetime) -> dict`

Schedules a follow-up meeting with a lead.

- **Parameters:**
  - `lead_email` (str): The email address of the lead.
  - `start_time` (datetime): The proposed start time for the meeting.
  - `end_time` (datetime): The proposed end time for the meeting.
- **Returns:**
  - dict: A dictionary containing the scheduled meeting details.