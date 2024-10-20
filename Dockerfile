#Dockerfile

FROM library/python:3.12.2-alpine

RUN apk update && apk upgrade && apk add --no-cache make g++ bash git openssh postgresql-dev curl

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ /usr/src/app

EXPOSE 80

ARG IS_CAPROVER_APP="True"
ARG AWS_STORAGE_BUCKET_NAME=${AWS_STORAGE_BUCKET_NAME}
ARG AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ARG AWS_S3_CUSTOM_DOMAIN=${AWS_S3_CUSTOM_DOMAIN}
ARG AWS_S3_ENDPOINT_URL=${AWS_S3_ENDPOINT_URL}
ARG AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

# Collect static files
RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]