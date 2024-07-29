FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

COPY . /app/
COPY requirements.txt /app/

RUN apk add python3-dev py3-pip build-base \
                          gcc \
                          libc-dev \
                          libffi-dev 
RUN cd MedikeaAIBackend

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY ./entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]   