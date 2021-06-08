FROM python:latest

RUN apt-get update && apt-get install -y vim
RUN pip install --upgrade pip --no-cache-dir --

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY data_injection.py /root/
COPY connect_db.py /root/
COPY create_table.py  /root/
COPY insert_data.py  /root/

COPY docker-entrypoint.sh /
RUN chmod +x ./docker-entrypoint.sh
RUN ./docker-entrypoint.sh
