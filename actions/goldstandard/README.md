# Action for Gold Standard Assessment
This action aims automatically assessing your Splunk Add-on compliance with the so called Gold Standard. A score will be returned as response to its project evaluation.

The purpose of the standard is defining best practices that lay the foundation for successful Splunk Technology Add-on (TA) development. By complying with it, your TA aligns with Splunk's highest standards, enhances compatibility and facilitates long-term maintainability.

:construction: **This is a WIP and content may change** :construction:

## Usage
Use the action within your own Github worflows as shown below
```yaml
- name: Assess Gold Standard compatibility
  id: goldstandard
  uses: ./.github/actions/goldstandard
  with:
    appinspect-failures: 0,2
    report-path: /path/to/docs-linting-report.json

- name: Debug results
  run: |
    echo "TA scored ${{ steps.goldstandard.outputs.score }} points."
    echo "Minimum acceptable is ${{ steps.goldstandard.outputs.min-score }}"
```

### Inputs

| Name | Description | Mandatory | Default |
|:---:|---|:---:|:---:|
| `appinspect-failures` | The amount of failures detected by AppInspect. Format: `<cli_failures,api_failures>` (e.g. 0,2) | Y | -1,-1 |
| `report-path` | Path to the documentation linting report | N | N/A |

Documentation linting report example:

```json
{
    "docs/readme.md": [
        {
            "Action": {
                "Name": "",
                "Params": null
            },
            "Span": [
                1,
                5
            ],
            "Check": "Microsoft.We",
            "Description": "",
            "Link": "https://docs.microsoft.com/en-us/style-guide/grammar/person#avoid-first-person-plural",
            "Message": "Try to avoid using first-person plural like 'Let's'.",
            "Severity": "warning",
            "Match": "Let's",
            "Line": 4
        },
        {
            "Action": {
                "Name": "",
                "Params": null
            },
            "Span": [
                1,
                19
            ],
            "Check": "docs.EmptySections",
            "Description": "",
            "Link": "",
            "Message": "The section '## Getting Started #' appears to be empty. Please add content.",
            "Severity": "error",
            "Match": "## Getting Started\n#",
            "Line": 10
        }
    ]
}
```

### Outputs

| Name | Description |
|:---:|---|
| `score` | The score given to the TA |
| `min-score` | Minimum score accepted for Gold Standard compatibility |

## Contributing
TODO


## References
* [Splunk Gold Standard](https://splunk.atlassian.net/wiki/spaces/PROD/pages/1078297761617/Technology+Add-ons+Gold+Standard)
