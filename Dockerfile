FROM python:3.9-slim

RUN pip install requests

ADD main.py /

WORKDIR /
