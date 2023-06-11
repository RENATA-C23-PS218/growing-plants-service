# Use the official Python base image
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install virtualenv
COPY growing-plant-service /app/growing-plant-service

RUN /bin/bash -c "source venv/bin/activate"
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ENV GOOGLE_APPLICATION_CREDENTIALS /app/service-account-key.json

# CMD ["python", "task.py"]
