
# Overview
[Vale](https://vale.sh/) is an open-source, command-line tool used for linting and enforcing writing style guides in documentation, including Markdown files like README.md. It allows you to define custom rules and check your text for issues related to clarity, tone, and grammar.

It is leveraged in our workflows to evaluate the provided apps and add-ons documentation.

## `SplunkCommunity`
Identifies a custom ruleset for Splunk. In reference to [Vale styles](https://vale.sh/docs/topics/styles/).

**More rules can be added depending on defined needs.**
Check the [Package hub](https://vale.sh/hub/) for inspiration on what it can be done and what's available from Microsoft or Google.

## Usage
Add the `styles` folder into our app repos to properly execute CI workflows such as `docs-linting.yml` and `quality-assessment-ta.yml`

## Learn more
* [Enable/disable rules via `.vale.ini`](https://vale.sh/docs/topics/config/#basedonstyles)
    > `.vale.ini` configuration file is created in the workflow
* [Install other packages](https://vale.sh/docs/topics/packages/#structure-and-hosting)
* [Vale Studio](https://studio.vale.sh/) for testing rules
* [Shared Available Rules](https://vale.sh/explorer/)
* [Vale CLI](https://vale.sh/manual/)