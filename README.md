# Splunk Platform Apps
Welcome to Developer Relations at Splunk, our goal and objective is to make it very easy for developers to contribute, develop, and make an impact!

This repository contains onboarding documents, the community health files, workflows and resources to set you app for development, contributions or anything you'd like to do with the Splunk open-source community.

## Getting Started

Please see the `.github` folder for the following docs:

 - [Contributing guide](.github/CONTRIBUTING.md)
 - [PR template](.github/pull_request_template.md)
 - [Issue templates](.github/ISSUE_TEMPLATE)

The `workflow-templates` folder contains the [GitHub Action](https://docs.github.com/en/actions)
workflow files for the common CI workflows used by our app repos.

The `documentation` folder contains information and an example of usage to easily deploy and possibly customize documentation styling of our app repos.

The `actions` folder contains the GitHub actions available for usage into CI workflows used by our app repos:

- :construction: [Gold Standard Assessment](./actions/goldstandard/README.md)
- :construction: [Splunk App Detector](./actions/splunk-apps-detector/README.md)

## Splunk install test versions

The shared install workflow uses Splunk 10.0.1 and 9.3.0 by default. Apps can set
`splunk_versions` to a JSON array of exact `splunk/splunk` image tags that match
their supported Enterprise versions. For example, a Python 3.13-only app can use:

```yaml
jobs:
  install-test:
    uses: splunk-platform-apps/.github/.github/workflows/reusable-test-ta-install.yml@v1
    with:
      addon_name: jellyfisher
      splunk_versions: '["10.6.1.1"]'
```

The example requires a workflow ref that includes the `splunk_versions` input.
The workflow checks package installation and registration. Use an app's own
smoke tests to verify that its commands or inputs work on those versions.

## Admin Operations

See [ADMIN.md](.github/ADMIN.md) for instructions on tagging and approving new repository requests.

## Support
Did we miss anything?

- Reach out to us via submitting an issue
- Office hours - Held periodically

Contribution is not limited to software developers, since there are other ways you can help. For example, contributing towards documentation, translation, and support. Join the Splunk community to see how you can help.

[Splunk Community](https://docs.splunk.com/Documentation/Community/current/community/AboutCommunity)
