# Interactive Quiz Application

This is a Django-based quiz application that allows users to take quizzes, store their scores, and manage quiz questions. The app includes a RESTful API for retrieving quiz data and user scores with authentication using JSON Web Tokens (JWT). Only read operations are allowed through the API. 

This project is also made in partial fulfilment of ALX Software Engineering course completion.

## Features
- **User Authentication**: User login and authentication for the app & API.
- **Quiz Management**: Create and store quizzes with multiple options per question.
- **Score Tracking**: Track and display user scores.
- **API**: Provides read-only access to quizzes and user scores via a RESTful API.

## Models
- **User**: Extends Django's `AbstractUser` to manage user accounts.
- **Score**: Stores the quiz scores of users.
- **Quiz**: Represents quiz questions, answers, and metadata (topic, difficulty).
- **Option**: Represents answer options for each quiz question.

## API Endpoints
- **/api/users/**: Retrieve a list of users with their associated scores.
- **/api/quizzes/**: Retrieve a list of quizzes with their options.

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.8+
- Django 4.x
- Django REST Framework

## Required Python Packages
Install the following packages via `pip`:
```bash
pip install django djangorestframework
```

## Setup Instructions

Follow these steps below to set up and run the quiz application:

1. **Clone the repository**:
   ```bash
   git clone git@github.com:TheKingsident/interactive-quiz.git
   cd interactive-quiz
   ```

2. **Set up a virtual environment (optional, but recommended, strongly advised)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Make database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (to access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Open your browser and go to `http://127.0.0.1:8000/` to view the app.
   - The admin panel is available at `http://127.0.0.1:8000/admin/`.

## API Usage
Once the app is running, you can interact with the API using tools like Postman or `curl`.

1. **Get an access token**:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/users/   -d "username=<your_username>&password=<your_password>"
   ```

2. **Access users and quizzes** (add the token to the Authorization header):
   ```bash
   curl -H "Authorization: Bearer <your_token>" http://127.0.0.1:8000/api/users/
   curl -H "Authorization: Bearer <your_token>" http://127.0.0.1:8000/api/quizzes/
   ```

## Project Structure
- `models.py`: Contains the `User`, `Score`, `Quiz`, and `Option` models.
- `api_views.py`: Contains the API views for the quiz and user models.
- `urls.py`: Defines the URL routes, including the API routes.
- `views.py`: Handles the app's non-API views.

## License
This project is licensed under the [MIT License](LICENSE).
