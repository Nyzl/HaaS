FROM python:3.10-slim AS build

WORKDIR /home/app

RUN python -m venv /home/app/venv
ENV PATH="/home/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.10-slim@sha256:030ead045da5758362ae198e9025671f22490467312dbad9af6b29a6d6bc029b

RUN groupadd -g 999 app && \
    useradd -r -u 999 -g app app
USER 999
WORKDIR /home/app

COPY --chown=app:app --from=build /home/app/venv ./venv
COPY --chown=app:app haas/ haas/

ENV PATH="/home/app/venv/bin:$PATH"

CMD gunicorn haas:app
