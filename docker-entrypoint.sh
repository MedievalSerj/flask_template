#!/bin/sh

# default worker user and group ids
worker_uid=$(id -u worker)
worker_gid=$(id -g worker)

if [ -z "$SKIP_PIP" ]; then
  printf 'Updating requirements...\n'
  pip install --user --no-cache-dir --requirement ./requirements.txt
fi

exec su-exec $worker_uid:$worker_gid "$@"
