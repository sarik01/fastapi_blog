FROM python:3.9.7

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim
#RUN apk add postgresql-client build-base postgresql-dev

RUN pip install --upgrade pip

COPY requirements.txt /temp/requirements.txt
COPY . /fastapi_blog
WORKDIR /fastapi_blog

# Perebroska portov chtobi bil dostup iz osnovnoy operac sistemi
#EXPOSE 8000

RUN pip install -r /temp/requirements.txt
RUN pip install typing-extensions --upgrade

# sozdat uzera bez parola
RUN adduser --disabled-password service-user

RUN chown -R service-user:service-user /fastapi_blog && chmod 755 /fastapi_blog

# polzovatel pod kotorim vse commandi konteynera budut zapuskatsa
USER service-user

#CMD ["gunicorn", "--bind", ":5000", "--workers", "3", "wsgi:application"]