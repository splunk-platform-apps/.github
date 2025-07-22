#!/bin/bash


JSON_KEY_TO_CHECK="meta._uccVersion"

# Function to check if a JSON file contains a specific key
check_json_key() {
    local json_file=$1
    local key=$2
    if jq -e ".${key}" "$json_file" &> /dev/null; then
        echo "Key '${key}' found in ${json_file}."
    else
        echo "Key '${key}' NOT found in ${json_file}."
        return 1  # Return failure if the key is not found
    fi
}

# Find the JSON file in the repository
JSON_FILE=$(find $GITHUB_WORKSPACE/ -name "globalConfig.json" -print -quit)

if [ -z "$JSON_FILE" ]; then
    echo "globalConfig.json file not found in the repository."
    exit 1
fi

# Check for the specific key in the JSON file
check_json_key "$JSON_FILE" "$JSON_KEY_TO_CHECK"
if [ $? -ne 0 ]; then
    echo "The specified key '${JSON_KEY_TO_CHECK}' was not found in ${JSON_FILE}. Exiting."
    exit 1
fi

UCC_VERSION=$(jq -r ".${JSON_KEY_TO_CHECK}" "$JSON_FILE")
# Set value into json file for further usage
echo "{\"UCC_VERSION\": \"$UCC_VERSION\"}" > dev1.1.json
