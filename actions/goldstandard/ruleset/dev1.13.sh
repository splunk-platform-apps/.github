#!/bin/bash

# Check if the environment variable is set
if [ -z "$APPINSPECT_FAILURES" ]; then
  echo "Error: APPINSPECT_FAILURES environment variable is not set."
  exit 1
fi

# Failures will come from AppInspect CLI and API executions.
# APPINSPECT_FAILURES=<CLI_failures>,<API_failures>
# Split the variable to analyse both
CLI_FAILURES=${APPINSPECT_FAILURES%,*}
API_FAILURES=${APPINSPECT_FAILURES#*,}

# Check if failures = 0
if [ $CLI_FAILURES -ne 0 ]; then
  echo "Warning: AppInspect CLI failed!"
  exit 1
fi

if [ $API_FAILURES -ne 0 ]; then
  echo "Warning: AppInspect API failed!"
  exit 1
fi

echo "AppInspect was successful! Yay!"
