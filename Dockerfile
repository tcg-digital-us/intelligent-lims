FROM python:3

COPY ./build /build
COPY ./scripts/init_venv.py /scripts/init_venv.py
WORKDIR /build

RUN python ../scripts/init_venv.py
RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
