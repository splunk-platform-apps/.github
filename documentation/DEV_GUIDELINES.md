# Development Guidelines

This guide outlines the documentation requirements and setup for Splunk Platform Apps.

## Requirements

Your repository comes pre-configured with all necessary files and templates.

:point_right: **As a developer, your primary task is populating these templates with your app's content while maintaining the defined structure.**

### Responsabilities
:white_check_mark: Please DO:

1. Update `<path-to-your-app-src>/docs/readme.md` with your app's specific content following the provided template
2. Maintain accurate and complete documentation
3. Ensure all links are valid
4. Follow the established structure
5. Address any quality check failures

:x: Please DO NOT modify or remove:
- Docusaurus configuration files
- Documentation templates
- Pipeline configurations

## Getting Started

* Structure your code as per [below](#repository-structure)
* Add [documentation](#documentation) to your project by updating the `docs/readme.md` file provided in your repository
* Understand usage and troubleshooting of provided [automation pipelines](https://github.com/splunk-platform-apps/.github/blob/main/.github/CONTRIBUTING.md)
* Understand the [release process](https://github.com/splunk-platform-apps/.github/blob/main/.github/CONTRIBUTING.md#code-release)

### Repository Structure

```
.
├── README.md
├── CHANGELOG.md
├── docs
│   └── readme.md
├── package
|   ├── README.txt
│   ├── README
│   ├── LICENSES
|   |   └── LICENSE.txt
│   ├── app.manifest
│   ├── appserver
│   ├── bin
│   ├── default
│   ├── metadata
│   └── static
├── etc
├── website
│   └── docusaurus.config.ts
└── tests
    ├── conftest.py
    └── pytest.ini
```

* `README.md` to set expectations and give usage instructions
* `CHANGELOG.md` to keep track of all notable changes made as explained [here](https://github.com/splunk-platform-apps/.github/blob/main/.github/DEV_WORKFLOW.md#changelog)
* `docs/` contains main documentation
* `.gitignore` to ignore hidden or OS_ files
* `etc/` contains additional files such as images, configuration files, etc
* `website/` contain files required by [docusaurus](#documentation)
* `package/` contains Splunk App / Add-On Source Files
* `tests/` contains files for unit testing, e2e testing, mocks, postman collections, etc

:point_right: Files needed for local development, packaging and local execution such as for example `docker-compose.yml`, `Makefile`, `pyproject.toml` or `poetry.lock` shall be added in the root folder.

## Technical Notes

### Documentation

We use [Docusaurus](https://docusaurus.io/) to build and maintain documentation for community apps. Please be aware of the following structural setup:

- Your repository comes pre-configured with

   - Docusaurus configuration files
   - A **[README.md](./templates/root-README.md)** file located in the repository root, providing essential links about your app
   - A **[README.md](./templates/docs-readme.md)** file located in your repository `docs/` directory, containing detailed documentation about your app's features, configuration and usage

- To maintain consistency and reduce duplication across projects, the core structural elements of Docusaurus are centralized within the [boilerplate](./boilerplate/) directory. These do not need to be recreated in individual repositories. This centralized directory handles the following:

   - Basic theme setup
   - Navigation structure
   - Required templates

#### Deployment

Documentation is **automatically deployed to GitHub Pages** through the [`docs-deploy.yml`](https://github.com/splunk-platform-apps/.github/.github/workflows/reusable-docs-deploy.yml) pipeline. This pipeline will:

- Build the documentation from your `<path-to-your-app-src>/docs/` folder and from the centralized content
- Deploy to GitHub Pages
- Run on documentation changes in the default `main` branch

#### Quality Assessment

Documentation undergoes automated quality checks including:

- Markdown linting
- Link validation
- Structure verification
- Content completeness checks
