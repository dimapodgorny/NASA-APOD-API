NOTE: I HAVE NOT TESTED THIS PROJECT ON ANY OTHER DEVICES, SO IT IS VERY POSSIBLE IT ONLY WORKS FOR ME AND NO ONE ELSE. IF YOU FIND OR EXPERIENCE ANY ISSUES PLEASE TELL ME

# NASA APOD API Viewer using Django
A simple web application built with Django that fetches and displays the Astronomy Picture of the Day (APOD) from NASA's official API. Users can view today's picture or select a specific date to explore past images.

### Feautures
- **Today's Picture**: View the most recent Astronomy Picture of the Day.
 
- **Date Selection:** Use a date picker to fetch and display an image from any previous date.
 
- **Secure API Handling**: API keys are managed securely using environment variables and are not exposed in the source code.
 
- **Robust Form Handling**: Implements the Post/Redirect/Get (PRG) pattern to prevent form resubmission on page reload.

- **Error Display**: Gracefully handles and displays errors from the API (e.g., if an image for a specific date is not found).

### Technology Stack
- **Backend**: Python with the Django Framework
- **Frontend**: HTML5, CSS3
- **API**: ```https://api.nasa.gov/planetary/apod```
- **Configuration**: ```python-decouple``` for managing environment variables


## Setup and Installation

### Prerequisites
- Python 3.8+ (probably works but only tested on ) - https://www.python.org/downloads/
- Pip package manager
- A NASA API key - https://api.nasa.gov/#signUp

1. Clone the Repository
```bash
git clone https://your-repository-url.com/
cd your-project-directory/
```

2. Create and Activate a Virtual Environment
- On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
- On Windows:
```bash
python3 -m venv venv
.\venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
Configuration
1. Set Up the Environment File
This project uses a `.env` file to store sensitive information like your API key.

Create a file named `.env` in the root directory of the project.

Add your NASA API key to the `.env` file:
```python
# .env
SECRET_KEY="your-django-secret-key-here"
NASA_API_KEY="your-nasa-api-key-here"
```

2. Set Up the Database
Run the Django `migrate` command to create the necessary database tables (including the `django_session` table)
```bash
python manage.py migrate
```

## Usage
once the setup and configurations are complete you can run the development server
```bash
python manage.py runserver
```
Then finally open your browser and search `http://127.0.0.1:8000/`
