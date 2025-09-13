FROM python:3.13.3-alpine3.22

WORKDIR /code

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -U -r requirements.txt

COPY ./ ./

ENTRYPOINT ["python3", "main.py"]


