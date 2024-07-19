#!/bin/bash
# wait-for-it.sh

host="$1"
shift
until nc -z "$host" 3306; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 3
done
>&2 echo "MySQL is up - executing command"
exec "$@"
