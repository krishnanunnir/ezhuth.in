FROM python:3.7
ENV PYTHONBUFFERED 1
RUN mkdir /knodev
WORKDIR /knodev
ADD . /knodev/
RUN pip install -r requirements.txt