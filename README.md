# PawHub

## Description
This project is a pet management application designed to help pet owners track their pets' basic information and health records, schedule appointments, and manage pet-related tasks.  
**Current Status:** The project is currently in production.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Known Issues](#known-issues)
- [Contact Information](#contact-information)

## Installation

### Prerequisites
- **Required Software:**
  - Python 3.12.3
  - Flask 3.0.3
  - pip (Python package installer)

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/IrynaPiatnochka/DogApp
   cd DogApp
   
2. Install the required packages:
  **Create a requirements.txt file with the following content:**
   ```bash
    amqp==5.2.0
    APScheduler==3.10.4
    bcrypt==4.2.0
    blinker==1.8.2
    cachelib==0.9.0
    cachetools==5.4.0
    certifi==2024.7.4
    charset-normalizer==3.3.2
    click==8.1.7
    Flask==3.0.3
    Flask-Caching==2.3.0
    Flask-Cors==4.0.1
    Flask-Mail==0.10.0
    Flask-Migrate==4.0.7
    Flask-SQLAlchemy==3.1.1
    marshmallow==3.21.3
    mysql-connector-python==9.0.0
    redis==5.0.8
    requests==2.32.3
    SQLAlchemy==2.0.32
   ```

3. Run:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your environment: Create a .env file in the project root directory and add your configuration settings:
   Example:
   ```bash
   DATABASE_URL=mysql://user:password@localhost/dbname
   SECRET_KEY=your_secret_key
   ```

## Usage

1. Run the application:
   ```bash
   flask run
   ```

2. Access the application: Open your web browser and navigate to http://localhost:5000 to access the application.

   Example Endpoints:
   
    GET /api/profile/profiles: Retrieve a list of pets with their profile information.
   
    POST /api/medical_record/profile/int:profile_id: Add a new medical record for a particular dog.
   
    PUT /api/event/int:event_id: Edit an event in a calendar.
   
   For more details on API usage, check the Swagger Documentation in static/swagger.yaml

## Features

1. Keep basic information like date of birth, breed, chip number, weight, etc. stored in one place.
2. Track pet health and vet appointments, and keep vaccination records. 
3. Schedule reminders for pet-related events/tasks like vet appointments, grooming, playdates, etc.
4. User-friendly interface for managing pets.

## Known Issues
  
  - Improving database storage and hosting.
  - Data migration.

## Contact Information

  Iryna Piatnochka - ivpiatnochka@gmail.com


