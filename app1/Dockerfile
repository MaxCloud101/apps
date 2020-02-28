FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y python-pip python-dev

RUN  mkdir /app
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py 

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]