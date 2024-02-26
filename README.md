# API Documentation

## Endpoints

### /requirements/
Returns the contents of requirements.txt.

### /users/generate
Returns 100 random people with names and email addresses. Utilizes Faker. An optional query parameter regulates the number of people, defaulting to 100.

### /mean/
Returns the average height and weight (in cm, kg) from hw.csv. Uses only the standard library for this endpoint.

### /space/
Returns the number of astronauts in space. Utilizes http://api.open-notify.org/astros.json and https://pypi.org/project/requests/ for this task.
