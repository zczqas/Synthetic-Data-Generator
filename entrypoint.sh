#!/bin/bash


host="$DATABASE_HOST"
port="$DATABASE_PORT"

echo "Starting entrypoint.sh"
if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! pg_isready -h "$host" -p "$port" -q -t 1; do
      sleep 1
    done

    echo "PostgresSQL started"
fi


# alembic upgrade head

exec "$@"
