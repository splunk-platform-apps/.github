#!/bin/bash

REPO="splunk/addonfactory-ucc-generator"
UCC_VERSION=$(jq -r '.UCC_VERSION' "dev1.1.json")

if [ -z "$UCC_VERSION" ]; then
  echo "Error: UCC_VERSION variable is not set"
  exit 1
fi

# Define the minimum accepted version
TARGET_VERSION=$(curl -s "https://api.github.com/repos/$REPO/releases?per_page=6" |
  jq -r '.[].tag_name  |
  ltrimstr("v")' |
  sort -V |
  head -n 1)

# Function to compare two semantic versions
verge() {
  # Usage: verge v1 v2
  # Returns 0 if v1 >= v2, 1 otherwise
  echo "Comparing versions: $1 and $2"
  sorted_versions=$(printf "%s\n%s" "$1" "$2" | sort -V)
  largest_version=$(printf "%s\n" "$sorted_versions" | tail -n 1)
  [ "$1" = "$largest_version" ]
}

# Check if the current version is recent enough
if verge "$UCC_VERSION" "$TARGET_VERSION"; then
  echo "Version $UCC_VERSION is recent enough."
else
  echo "Version $UCC_VERSION is not recent enough. Minimum required version is $TARGET_VERSION."
  exit 1
fi