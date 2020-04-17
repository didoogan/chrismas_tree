FROM python:3.8-alpine

WORKDIR /app

RUN apk update && apk add --no-cache python3-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=wsgi:app

EXPOSE 5000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "wsgi:app"]

