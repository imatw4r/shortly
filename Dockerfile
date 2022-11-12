FROM python:3.10-slim-bullseye AS build

WORKDIR /tmp

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN pip install poetry \
    && poetry export -f requirements.txt --output requirements.txt --without-hashes --with dev

FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="${PYTHONPATH}:/app"

WORKDIR /app

COPY --from=build /tmp/requirements.txt .

RUN apt-get update \
  && apt-get -y install libpq-dev gcc

RUN pip install --no-cache-dir --upgrade -r requirements.txt \
  && rm requirements.txt

COPY shortly shortly
COPY tests tests
COPY scripts scripts

ENTRYPOINT ["bash", "./scripts/entrypoint.sh"]
