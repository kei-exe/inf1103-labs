FROM python:3.11-slim 
WORKDIR /app/OOP
COPY . .
CMD ["python", "main.py"]