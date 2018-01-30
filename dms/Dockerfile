FROM python:3
ENV PYTHONUNBUFFERED 1

# Passed in from docker-compose file
ARG mode

RUN mkdir /code
WORKDIR /code
ADD requirements/*.txt /code/requirements/
RUN pip --version
RUN pip install -r requirements/$mode.txt
ADD . /code/
