#!/bin/sh

# Execute the tests
pytest app/tests

# Wait for the database and cache to be up
wait-for-it.sh -t 30 db:5432 -- echo "PostgreSQL is up"
wait-for-it.sh -t 30 cache:6379 -- echo "Redis is up"

# Run the application if the tests pass
if [ $? -eq 0 ]
then
  echo "Tests successful, starting the container..."
  python3 -m flask --app main.py --debug run --host=0.0.0.0
else
  echo "Tests failed, container won't start."
  exit 1
fi