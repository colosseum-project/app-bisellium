FROM python:3.12-alpine
ENV APP_HOME="/opt/bisellium" \
    FLASK_APP=bisellium \
    FLASK_ENV=production \
    PROMETHEUS_MULTIPROC_DIR="/var/cache/prometheus_metrics"

WORKDIR "${APP_HOME}"

# create application directories
RUN mkdir -p \
    "${APP_HOME}" \
    "${PROMETHEUS_MULTIPROC_DIR}"

# install dependencies
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps build-base linux-headers && \
    apk add --no-cache jpeg-dev zlib-dev && \
    pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install --no-cache-dir gunicorn && \
    apk del .build-deps

# copy application files
COPY . .

# create application user and set permissions
RUN adduser \
    --disabled-password \
    --home "${APP_HOME}" \
    --uid 1001 \
    --gecos "" \
    --shell /bin/sh \
    bisellium
RUN chown -R 1001:1001 \
    "${APP_HOME}" \
    "${PROMETHEUS_MULTIPROC_DIR}"
USER bisellium

# run production-ready application :)
EXPOSE 8080
CMD [ "gunicorn", "-w 4", "-b 0.0.0.0:8080", "bisellium:create_app()"]
