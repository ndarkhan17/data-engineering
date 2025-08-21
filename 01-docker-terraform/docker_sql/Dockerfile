FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY upload_data_to_postgres.py upload_data_to_postgres.py

ENTRYPOINT [ "python", "upload_data_to_postgres.py" ]