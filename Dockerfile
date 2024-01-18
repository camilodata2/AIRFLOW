FROM apache/airflow:2.8.0

COPY requirements.txt ./requirements.txt


RUN pip install --upgrade pip && pip install -r requirements.txt


