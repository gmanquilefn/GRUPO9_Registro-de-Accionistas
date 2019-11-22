FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /regAccionistas
WORKDIR /regAccionistas
ADD requirements.txt /regAccionistas/
RUN pip install -r requirements.txt

ADD . /regAccionistas/
CMD python manage.py makemigrations
CMD python manage.py migrate
