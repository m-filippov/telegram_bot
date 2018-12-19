FROM python:2.7-alpine3.7
RUN pip install pyTelegramBotAPI
COPY ./BOT.py /BOT.py