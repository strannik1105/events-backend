FROM python:3.11-slim

RUN apt update

COPY . .

RUN pip install -r requirements.txt

CMD python3 src/main.py