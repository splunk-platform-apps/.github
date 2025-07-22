#!/bin/bash

# Arguments
RULESET_FILE=$1

# Keep track of calculated score
TOTAL_SCORE=0

BASEDIR=$(dirname $0)
cd $BASEDIR

# Function to determine the script type based on the shebang line
check_shebang() {
    local script_file="$1"
    local shebang

    # Read the first line (shebang) of the script
    shebang=$(head -n 1 "$script_file")

    if [[ "$shebang" == "#!"* ]]; then
        if [[ "$shebang" == *"/bin/sh"* || "$shebang" == *"/bin/bash"* ]]; then
            echo "shell"
        elif [[ "$shebang" == *"/usr/bin/python"* || "$shebang" == *"/usr/bin/env python"* ]]; then
            echo "python"
        else
            echo "unknown"
        fi
    else
        echo "no_shebang"
    fi
}

# Loop through each rule in the YAML file
for rule in $(yq e '.rules | keys | .[]' "$RULESET_FILE"); do
  # Get the rule's details
  rule_name=$(yq e ".rules[$rule].name" "$RULESET_FILE")
  score=$(yq e ".rules[$rule].score" "$RULESET_FILE")
  script_path=$(yq e ".rules[$rule].path" "$RULESET_FILE")
  mandatory=$(yq e ".rules[$rule].mandatory" "$RULESET_FILE")

  echo "Processing rule: $rule_name"

  # Check if the script exists
  if [ ! -f "$script_path" ]; then
    echo "Error - Script '$script_path' not found!"
    if [ "$mandatory" == "true" ]; then
      echo "Mandatory rule $rule_name failed due to missing script!"
      exit 1
    fi
    continue  # Skip to the next rule if the script doesn't exist
  fi

  # Check script type
  # Call the function to check the shebang and capture the result
  result=$(check_shebang "$script_path")
  # Determine the type based on the function result
  case "$result" in
      shell)
          echo "$script_path is a shell script"
          # Execute the script
          echo "Executing script: $script_path"
          if sh "$script_path"; then
            echo "Script $script_path executed successfully"
            TOTAL_SCORE=$((TOTAL_SCORE + score))  # Sum the score if execution is successful
          else
            echo "Script $script_path failed"
            if [ "$mandatory" == "true" ]; then
              echo "Mandatory rule $rule_name failed!"
              exit 1
            fi
          fi
          ;;
      python)
          echo "$script_path is a Python script"
          # Execute the Python script and capture both the output and the error
          OUTPUT=$(python3 "$script_path" 2>&1)

          # Capture the exit status of the Python script
          EXIT_STATUS=$?

          # Check if the command was successful
          if [ $EXIT_STATUS -eq 0 ]; then
              echo "Script $script_path executed successfully - $OUTPUT"
              TOTAL_SCORE=$((TOTAL_SCORE + score))  # Sum the score if execution is successful
          else
              echo "Script $script_path returned an error while executing - $OUTPUT"
              if [ "$mandatory" == "true" ]; then
                echo "Mandatory rule $rule_name failed!"
                exit 1
              fi
          fi
          ;;
      unknown)
          echo "$script_path is of an unknown type"
          ;;
      no_shebang)
          echo "$script_path does not have a shebang and has an unknown type"
          ;;
  esac

done

# Set output variable for GitHub Actions
echo "score=${TOTAL_SCORE}" >> $GITHUB_OUTPUT
