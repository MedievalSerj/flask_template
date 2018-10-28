#!/bin/sh

# default worker user and group ids
worker_uid=$(id -u worker)
worker_gid=$(id -g worker)

case $ENV in
  development )
    # get mounted directory owner user and group ids
    worker_uid=$(stat -c %u .)
    worker_gid=$(stat -c %g .)

    if [ -z "$SKIP_PIP" ]; then
      printf 'Updating requirements...\n'
      pip install --user --no-cache-dir --requirement ./requirements.txt
    fi
esac

# run db migrations
alembic upgrade head

exec su-exec $worker_uid:$worker_gid "$@"
