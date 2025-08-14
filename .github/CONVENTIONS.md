# Conventions in use by `splunk-platform-apps` repositories

## Code and Style
We would ask that you adhere to the following guidelines when developing your App to ensure consistency without our platform.

### Python
Projects using Python will be expected to standardize to [PEP8](https://peps.python.org/pep-0008/). Code will be automatically linted using [ruff](https://docs.astral.sh/ruff/). It is an _extremely_ good idea to lint your code with the provided [configuration](https://github.com/splunk-platform-apps/.github/tree/main/actions/lint/ruff.toml) before committing your code.

## App Naming Convention
Apps should follow the [Splunkbase naming guidelines](https://dev.splunk.com/enterprise/docs/releaseapps/splunkbase/namingguidelines/). Further details for Splunk naming conventions can be found [here](https://lantern.splunk.com/Splunk_Success_Framework/Data_Management/Naming_conventions).

> TODO: Link to a TA/app that has been uploaded to the repo

## Architecture
An overview of the expected repository structure.

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
└── tests
    ├── conftest.py
    └── pytest.ini
```

* `README` to set expectations and give usage instructions
* `CHANGELOG` keeps track of all notable changes made to the app (e.g. bug fixes, new features, etc)
* `docs` contains main documentation
* `.gitignore` to ignore hidden or OS_ files
* `etc/` contains additional files such as images, configuration files, etc
* `package/` contains Splunk App / Add-on Source Files
* `tests/` contains files for unit testing, e2e testing, mocks, postman collections, etc

:point_right: Files needed for local development, packaging and local execution such as for example `docker-compose.yml`, `Makefile`, `pyproject.toml` or `poetry.lock` shall be added in the root folder.
