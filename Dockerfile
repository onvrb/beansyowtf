FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

VOLUME [ "/data" ]

CMD [ "python3", "-u", "run.py"]
