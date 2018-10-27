FROM python:3.7.0-alpine

# setup custom python packages base directory
# it is required to use pip with --user flag
ENV PYTHONUSERBASE '/pip-cache'
ENV PATH "$PYTHONUSERBASE/bin:$PATH"
ENV PYTHONUNBUFFERED 1

# setup working directory
ENV WORKER_APP_DIR='/app' \
    PATH="$PATH:/app" \
    PYTHONPATH=$PYTHONPATH:$WORKER_APP_DIR

WORKDIR /app

# setup group/user
RUN set -ex \
    && addgroup -g '1000' -S 'worker' \
    && adduser -u '1000' -G 'worker' -S -s '/bin/false' -h '/app' 'worker'

# dependencies to build from source code
RUN apk --no-cache add build-base \
    postgresql-dev \
    su-exec

ADD . .

RUN pip install --user --no-cache-dir -r requirements.txt

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["gunicorn", "--config", "./gunicorn_config.py", "flask_template.instance:app"]
