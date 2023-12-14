FROM python:3.9
LABEL authors="cookie-hankie"

WORKDIR /app

# Use a wildcard to ensure that a requirements.txt file is not required.
COPY requirements.txt* ./

# Install the Python dependencies defined in requirements.txt, if it exists.
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy the current directory contents into the container at /app.
COPY . .

# Create a user in a group with no permissions to any files not explicitly granted
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser

# Switch to the new user
USER appuser

# Command to run the Uvicorn server. This will start your FastAPI application.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
