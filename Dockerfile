FROM python:3.12.2

ENV DB_HOST='localhost'
ENV DB_PORT=5432
ENV DB_NAME='flask_restapi'
ENV DB_USER='flask_restapi'
ENV DB_PASSWORD='flask_restapi_pass'

ENV CACHE_HOST='localhost'
ENV CACHE_PORT=6379
ENV CACHE_DB=0
ENV CACHE_DECODE_RESPONSES=True

ENV COUNTRIES_SOURCE="https://cloford.com/resources/codes/index.htm"
ENV ASTRONOMERS_SOURCE="https://en.wikipedia.org/wiki/List_of_astronomers"

WORKDIR /opt/app

COPY . .
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

RUN pip install --no-cache-dir -r requirements.txt

VOLUME /data_store
EXPOSE 5000

CMD ["start.sh"]