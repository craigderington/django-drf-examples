FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
EXPOSE 80
RUN cd /code/drfexample
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8888