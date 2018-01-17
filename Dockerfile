FROM python:3.6

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
ADD . /usr/src/app/
RUN pip install -r requirements.txt

EXPOSE 9090
CMD ["python", "app.py"]