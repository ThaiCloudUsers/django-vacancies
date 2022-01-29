FROM python:3.9

RUN apt-get update && apt-get install -y libpq-dev postgresql-client
RUN mkdir -p /app
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . ./app
CMD ["sleep", "1d"]
