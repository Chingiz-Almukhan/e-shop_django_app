FROM python:3.9

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ['python', 'manage.py', 'migrate']

# CMD gunicorn -w 3 --chdir ./source quantum.wsgi --bind 0.0.0.0:8000
