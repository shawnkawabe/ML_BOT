FROM python:3.7.5
ENV IA 1
RUN mkdir /ML_ROBOT
WORKDIR /ML_ROBOT
ADD requirements.txt /ML_ROBOT/
RUN pip install -r requirements.txt
ADD . /ML_ROBOT/