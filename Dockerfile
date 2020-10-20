FROM python:3.8-alpine
ARG PROJECT_DIR
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev && \
    apk add postgresql-dev
COPY . .

#RUN mkdir ${PROJECT_DIR} && cd ${PROJECT_DIR}
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt
RUN apk del .build-deps