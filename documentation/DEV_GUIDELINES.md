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

## Technical Notes

### Platform

We use [Docusaurus](https://docusaurus.io/) to build and maintain documentation for community apps. Your repository comes pre-configured with:

- Docusaurus configuration files
- Basic theme setup
- Navigation structure
- Required templates

The sample [boilerplate app](./boilerplate/) demonstrates a complete documentation setup.

#### Docusaurus Updates

Follow [instructions](https://docusaurus.io/docs/installation#updating-your-docusaurus-version) and more specific [notes](https://overreacted.io/npm-audit-broken-by-design/) on fixing dependencies vulnerabilites.

### Required Structure

All Splunk Platform Apps must maintain two key documentation files:

1. **Root README.md**
   - Located at the repository root
   - As defined in [README-template.md](./templates/root-README.md)
   - Provides essential links and high-level project information

2. **Documentation README**
   - Located at `<path-to-your-app-src>/docs/readme.md`
   - Must align with the structure defined in [docs-readme-template.md](./templates/docs-readme.md)
   - Contains detailed documentation about your app's features, configuration, and usage

### Deployment

Documentation is **automatically deployed to GitHub Pages** through the [`docs-deploy.yml`](https://github.com/splunk-platform-apps/.github/.github/workflows/reusable-docs-deploy.yml) pipeline. This pipeline will:

- Build the documentation from your `docs/` folder
- Deploy to GitHub Pages
- Run on documentation changes in the default `main` branch

### Quality Assessment

Documentation undergoes automated quality checks including:

- Markdown linting
- Link validation
- Structure verification
- Content completeness checks


