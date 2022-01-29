#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "template1" <<-EOSQL
  CREATE USER vacancy_dev WITH PASSWORD 'developer';
  CREATE DATABASE vacancy_dev;
  GRANT ALL PRIVILEGES ON DATABASE vacancy_dev TO vacancy_dev;
  \connect vacancy_dev vacancy_dev
EOSQL