FROM python:3.5

RUN pip install flask
ADD run.py /sw/run.py

WORKDIR /sw

CMD python /sw/run.py
