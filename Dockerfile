# build stage
FROM python:3.12-slim as builder

WORKDIR /app

COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root


# runtime stage
FROM python:3.12-slim as runtime

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

CMD ["poetry", "run", "task", "start"]
