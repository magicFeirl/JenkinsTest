FROM python3.8

WORKDIR /code
COPY requirements.txt .
RUN pip install requirements.txt
COPY . /code
RUN uvicorn main:app --port=7878 --host=0.0.0.0