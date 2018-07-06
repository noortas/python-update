FROM python:2.7

RUN apt-get update && apt-get install -y python-dev default-libmysqlclient-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY update.py .

CMD /usr/local/bin/python update.py
