FROM python:3.8-alpine
ARG PROJECT_DIR
ENV PROJECT_DIR ${PROJECT_DIR}
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev && \
    apk add postgresql-dev
COPY . ${PROJECT_DIR}/
RUN python -m pip install --upgrade pip && \
    pip install -r ${PROJECT_DIR}/requirements.txt
RUN apk del .build-deps