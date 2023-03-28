FROM python:3

COPY . /app
WORKDIR /app

RUN . ./env/bin/activate
RUN pip install -r requirements.txt

CMD ["python", "./batch_release.py"]
