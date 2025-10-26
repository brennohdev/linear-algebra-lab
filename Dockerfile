FROM python:3.14-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.7.1 

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get remove -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY ./src ./src

RUN poetry install --no-dev


FROM python:3.14-slim as production

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system app && adduser --system --group app

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY --from=builder /app/src ./src

ENV PYTHONPATH="/app/src"

RUN chown -R app:app /app

USER app

EXPOSE 8000

CMD ["uvicorn", "src.core_studies.interface.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
