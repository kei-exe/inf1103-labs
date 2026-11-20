FROM python:3.11-slim 

WORKDIR /app/OOP

COPY OOP/ .

RUN pip install --no-cache-dir pytest

CMD ["python", "main.py"]