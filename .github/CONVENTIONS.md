# Conventions in use by `splunk-platform-apps` repositories

## Code and Style
We would ask that you adhere to the following guidelines when developing your App to ensure consistency without our platform.

### Python
Projects using Python will be expected to standardize to [PEP8](https://peps.python.org/pep-0008/). Code will be automatically linted using [ruff](https://docs.astral.sh/ruff/). It is an _extremely_ good idea to lint your code with the provided [configuration](https://github.com/splunk-platform-apps/.github/tree/main/actions/lint/ruff.toml) before committing your code.

## Commit Messages
[Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages provides a standardized format that makes the commit history more readable and enables automated generation of changelogs.

The basic structure is:

<type>[optional scope]: <description>
[optional body]
[optional footer(s)]

Common types include:
- feat: A new feature
- fix: A bug fix
- docs: Documentation changes
- style: Changes that don't affect code functionality (formatting, etc.)
- refactor: Code changes that neither fix bugs nor add features
- test: Adding or modifying tests
- chore: Changes to build process or auxiliary tools

It's recommended to follow this convention when contributing to the repositories.

## App Naming Convention
Apps should follow the [Splunkbase naming guidelines](https://dev.splunk.com/enterprise/docs/releaseapps/splunkbase/namingguidelines/). Further details for Splunk naming conventions can be found [here](https://lantern.splunk.com/Splunk_Success_Framework/Data_Management/Naming_conventions).

An example repository which meets these conventions can be found in the [splunkcommunity\_ta](https://github.com/splunk-platform-apps/splunkcommunity_ta_ucc)

## Renovate (Automated Dependency Updates)
Renovate is configured to automatically manage dependency updates across all repositories in this organization.

### How It Works
- Renovate runs on a schedule via GitHub Actions
- It scans all repositories for outdated dependencies
- PRs are automatically created with updates

### Supported Managers
- GitHub Actions
- Splunk Docker images
- npm (`package.json`)
- Pre-commit hooks (`.pre-commit-config.yaml`)

### Configuration
- **Global config**: `.github/renovate-config.js` (applies to all repos)
- **Repo-level overrides**: `.github/renovate.json` (added in each repo in need for specific settings)

:point_right: More about [configuration options](https://docs.renovatebot.com/configuration-options/)

### Automerge
- PRs with `automerge: true` will auto-merge via GitHub's platform automerge
- Branch protection rules and reviewer approval are still required
- Reviewers are assigned even on automerge PRs (`assignAutomerge: true`)
