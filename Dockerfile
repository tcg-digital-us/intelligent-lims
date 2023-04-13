FROM python:3

COPY src /app/src
COPY scripts/init_venv.py /app/scripts/init_venv.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN python scripts/init_venv.py
RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]
