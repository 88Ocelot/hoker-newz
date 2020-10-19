FROM python:3.8-alpine
ARG PROJECT_DIR
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev && \
    apk add postgresql-dev
COPY requirements.txt .

RUN mkdir ${PROJECT_DIR} && cd ${PROJECT_DIR}
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt
#RUN pythom ${PROJECT_DIR}
#COPY hoker_newz/static/ ${PROJECT_DIR}hoker_newz/static/
RUN apk del .build-deps