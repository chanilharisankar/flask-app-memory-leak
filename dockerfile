FROM python:3.7-alpine
RUN apk add curl
RUN mkdir /app
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY app.py /app
WORKDIR /app
EXPOSE 5000
ENV FLASK_ENV=development
CMD flask run --host=0.0.0.0