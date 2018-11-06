FROM python:3.7

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV UPSTREAM=''

CMD python init.py ${UPSTREAM}

