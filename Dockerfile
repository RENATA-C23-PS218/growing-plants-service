FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
RUN cp src/service-account/template-key.json src/service-account/key.json
CMD ["flask", "--app", "main", "run", "-h", "0.0.0.0"]
