FROM python:3

COPY ./build /app
WORKDIR /app

RUN . ./py_env/bin/activate
RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
