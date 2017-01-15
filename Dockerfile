FROM python:latest
EXPOSE 8000
RUN apt-get update
RUN apt-get -y install binutils libproj-dev gdal-bin
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/