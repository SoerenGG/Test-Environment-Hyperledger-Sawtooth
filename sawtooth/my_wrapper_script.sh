#!/bin/bash

# Start the first process
sawtooth-validator -vv \
      --endpoint tcp://validator:8800 \
      --bind component:tcp://eth0:4004 \
      --bind network:tcp://eth0:8800 \
      --bind consensus:tcp://eth0:5050 \
      &
# ./my_first_process -D
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start the validator service: $status"
  exit $status
fi

sleep 5

# Start the second process
devmode-engine-rust -vv --connect tcp://validator:5050 &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start the devmode-egine-rust: $status"
  exit $status
fi

# Start the third process
sawtooth-rest-api -vv --connect tcp://validator:4004 &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start the rest-api: $status"
  exit $status
fi

# Start the fourth process
settings-tp -vv --connect tcp://validator:4004 &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start the settings-tp: $status"
  exit $status
fi


# Naive check runs checks once a minute to see if either of the processes exited.
# This illustrates part of the heavy lifting you need to do if you want to run
# more than one service in a container. The container exits with an error
# if it detects that either of the processes has exited.
# Otherwise it loops forever, waking up every 60 seconds

while sleep 60; do
  ps aux |grep sawtooth-validator |grep -q -v grep
  PROCESS_1_STATUS=$?
  ps aux |grep devmode-engine-rust |grep -q -v grep
  PROCESS_2_STATUS=$?
  ps aux |grep sawtooth-rest-api |grep -q -v grep
  PROCESS_3_STATUS=$?
  ps aux |grep settings-tp |grep -q -v grep
  PROCESS_4_STATUS=$?
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 -o $PROCESS_3_STATUS -ne 0 -o $PROCESS_4_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    exit 1
  fi
done

