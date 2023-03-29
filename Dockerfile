FROM python:3

COPY ./build /app
WORKDIR /app

RUN . ./env/bin/activate
RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
