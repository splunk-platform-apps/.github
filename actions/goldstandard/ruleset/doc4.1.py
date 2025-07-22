#!/usr/bin/env python3
import os
import sys
import json
from collections import Counter

variable_name = "REPORT_PATH"


if __name__ == "__main__":
    if not variable_name in os.environ:
        print(f"{variable_name} does not exist. Evaluation fails.")
        sys.exit(1)

    # Read the file
    filepath = os.getenv(variable_name)
    try:
        with open(filepath) as f:
            data = json.load(f)
            # print(f"JSON data loaded successfully: {data}")

            # Evaluate the file
            # Current criteria:
            # - No errors
            report = {}
            for doc, results in data.items():
                severity_counter = Counter(
                    result.get("Severity")
                    for result in results
                    if result.get("Severity") is not None
                )
                report[doc] = dict(severity_counter)

            print(f"Linting reported the following results {report}")

            filtered_objects = [key for key, counts in report.items() if "error" in counts]
            if filtered_objects:
                print(f"Errors detected in doc files: {filtered_objects}")
                sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {filepath}")
        sys.exit(1)
