FROM python:3.8

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . .

EXPOSE 5000

CMD python ./run.py