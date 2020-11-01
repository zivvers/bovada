FROM python:3.8-slim

# upgrade pip

RUN pip install -U pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
