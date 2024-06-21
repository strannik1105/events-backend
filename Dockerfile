FROM python:3.11-slim as python_image

RUN apt update

COPY ./requirements.txt .

RUN pip install -r requirements.txt


FROM python_image

COPY . .

CMD python3 src/main.py