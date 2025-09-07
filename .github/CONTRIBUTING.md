# Contributing to Splunk Platform Apps

Thank you for considering spending your time contributing. Whether you're interested in bug-hunting, documentation, or creating entirely new apps, this document will help and guide you through the process.

If you've stumbled upon the site but don't know who or what we are, please check out the links below:
- [Splunk!](https://www.splunk.com/)
- [Splunk Developer Program](https://dev.splunk.com/)
- Info on [Splunk Apps and Add-ons](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/9.3/meet-splunk-apps/apps-and-add-ons)

---

## First Steps
Make sure you have a [GitHub Account](https://www.github.com)
- Make sure you know how Git works.
    - [Git Book](https://git-scm.com/book/en/v2)
    - [Git Handbook](https://guides.github.com/introduction/git-handbook/)
    - [GitHub Git Guide](https://help.github.com/en/articles/git-and-github-learning-resources)
    - [Git Workflow](https://guides.github.com/introduction/flow/)
    - [Git Visualization](http://git-school.github.io/visualizing-git/) -> Super cool!

## Project Details
To successfully contribute, you should spend a little time familiarizing yourself with the following key topics.

- [Coding & Conventions](./CONVENTIONS.md) - How we expect to see code formatted and apps named
- [Various Types of Apps](./TYPES_OF_SUPPORT.md) - Definitions and differences
- [Typical developer workflow](./DEV_WORKFLOW.md) - Configuring your dev environment


# High Level Contribution Overview
## Contributing Bug-fixes
If you've found a bug and wish to fix it, the first thing to do is

1. [Fork](https://guides.github.com/activities/forking/) the app repo that you
are looking to contribute to.
1. Install [pre-commit](https://pre-commit.com/#install) on your system, if not already installed, and then run `pre-commit install` while inside the app repo. _Note: This step is not required, but **strongly** recommended! It will allow you to catch issues before even pushing any code._
1. Create a branch.
1. Make your changes on your branch.
1. Thoroughly test your changes. See the [Automated Checks](#automated-checks) section for information about basic automated checks we provide for all apps.
1. Open a [pull request](https://help.github.com/articles/using-pull-requests/) to the `main` branch of the app repo, giving edit access to the maintainers of the repo. Please ensure your pull request adheres to the guidelines mentioned in [PULL REQUEST TEMPLATE](.github/pull_request_template.md).

:point_right: **Important Notes** :point_left:

1. Please check the **`Allow edits and access to secrets by maintainers`** box during your PR submission so that a developer can aid in the PR process.

1. **One issue per branch**. We will **not** accept any Pull Requests that affect more than one App or addresses more than one Issue at a time.

## Contributing New Apps

If you've created a brand new App and wish to contribute it, the steps to do so are as follows.

1. Create a new [issue](https://github.com/splunk-platform-apps/.github/issues/new?assignees=&labels=&template=new_repo_request.md&title=) in our `.github` repo to request a new repository to be created for your app.
1. [Fork](https://guides.github.com/activities/forking/) the project.
1. Install [pre-commit](https://pre-commit.com/#install) on your system, if not already installed, and then run `pre-commit install` while inside the app repo.

    :point_right: This step is not required, but **strongly** recommended! It will allow you to catch issues before even pushing any code.

1. Create a branch (following our [Conventions](.github/CONVENTIONS.md)).
1. Push your app code to the branch you created.
1. **Thoroughly** test your code for the new App. See the [Automated Checks](#automated-checks) section for information about basic automated checks we provide for all apps.
1. Perform a [pull request](https://help.github.com/articles/using-pull-requests/) to the `main` branch of the app repo. Please ensure your pull request adheres to the guidelines mentioned in [PULL REQUEST TEMPLATE](.github/pull_request_template.md).


## Automated Checks
By default we provide various automated checks you can leverage to test your changes automatically. These checks will be run whenever you push new commits to your pull request branch. The overall pass/fail result will appear as a green checkmark or red "x" to the right of commit in the pull request page. To view the detailed report you can do **ANY** of the following:

- Click the checkmark or "x" and then click the "Details" link. **OR**
- Click the "Checks" tab at the top of the pull request. **OR**
- Click the "Details" link next to the list of checks that shows up at the bottom of the pull request. If the tests passed, this list will be hidden, so you will first need to click the "Show all checks" link.

The checks performed are the following:

(Pre-commit checks that can be run with a commit locally or with `pre-commit run --all-files`)

- **Code Quality Checks**:
  - Python linting and formatting with [Ruff](https://astral.sh/ruff)
  - Security scanning with [semgrep](https://semgrep.dev/index.html)
  - Shell linting and formatting with [ShellCheck](https://www.shellcheck.net/)
- **General Checks**:
  - Merge conflict detection
  - End-of-file fixing
  - Trailing whitespace cleanup
  - JSON and YAML validation
  - Prevent giant files from being committed
- **Splunk-specific Checks**:
  - Documentation building
  - App dependency packaging
  - Release notes validation

Additionally, our CI/CD pipeline runs these checks on each pull request:

- **Pre-commit Checks**:
  - Listed above
- **Build**: Creates app package
- **Sanity Tests**: Validates app functionality for the Splunk Cloud environment via AppInspect CLI
- **Quality Assessment**: Verifies Gold Standard compatibility and checks [documentation quality](https://github.com/splunk-platform-apps/.github/blob/main/documentation/DEV_GUIDELINES.md#quality-assessment)

Other OOB pipelines focus on the [documentation deployment](https://github.com/splunk-platform-apps/.github/blob/main/documentation/DEV_GUIDELINES.md#deployment) and the [Add-On release](#code-release).

## Code Release
On each tag push, the following checks will be executed before releasing a new version of the Add-On:

- **Build**: Creates app package
- **Sanity Tests**: Validates app functionality for the Splunk Cloud environment via AppInspect CLI
- **Release Notes Validation**: Checks whether the `CHANGELOG.md` file has been populated with latest info - [guidelines](https://github.com/splunk-platform-apps/.github/blob/main/.github/DEV_WORKFLOW.md#changelog)

## Code Owners
To ensure code that lives in the repositories is not abandoned, all Splunk Apps and Add-Ons added are required to have a code owner. A code owner is responsible for the Splunk App / Add-On hosted within a repository.
This status is identified in the CODEOWNERS file. That responsibility includes maintaining the app, triaging and responding to issues, reviewing pull requests and releasing the app itself as described [below](#responsibilities).

### Requirements

To become a code owner, you will need to have **good working knowledge of the code you are sponsoring and any project that that code instruments or is based on**.

### Responsibilities

As a code owner you will be responsible for the following:

- You will be expected to review any Pull Requests or Issues created that relate to this app.
- You will be responsible for the stability and versioning compliance of the app.
- You will be expected to provide and keep the documentation of the app up to date.
- You will be responsible for releasing new versions of the app.


### How to become a Code Owner

Code ownership **must** be specified when a new repository is requested by opening [an Issue](https://github.com/splunk-platform-apps/.github/issues/new?template=component_request.yaml).

Multiple code owners can be specified as individual GitHub users.

### Removing / Transferring Code Ownership

Code owners are expected to remove their ownership if they cannot fulfill their responsibilities anymore. To do so, open [an Issue](https://github.com/splunk-platform-apps/.github/issues/new?title=Edit+Code+Ownership&body=Please+transfer+ownership+of+repo+add_repo_name+to+add_new_user) requesting to either:
- Transfer the code ownership to given user(s),
- Remove the code ownership.

Do not forget to provide the name of the repository the request is referring to.

:point_right: When a repository has no remaining code owners, the repository will be archived by the organization administrators.

:point_right: It is at the discretion of the organization administrators to decide if a repository shall be archived in case of inactivity greater than 1 year, during which time there are active Issues or Pull Requests to address.

## Legal Notice
By submitting a Contribution to this Work, You agree that Your Contribution is made subject to the primary license in the Apache 2.0 license (found [here](https://www.apache.org/licenses/LICENSE-2.0.txt)). In addition, You represent that: (i) You are the copyright owner of the Contribution or (ii) You have the requisite rights to make the Contribution.

### Definitions:

“You” shall mean: (i) yourself if you are making a Contribution on your own behalf; or (ii) your company, if you are making a Contribution on behalf of your company. If you are making a Contribution on behalf of your company, you represent that you have the requisite authority to do so.

"Contribution" shall mean any original work of authorship, including any modifications or additions to an existing work, that is intentionally submitted by You for inclusion in, or documentation of, this project/repository. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication submitted for inclusion in this project/repository, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the maintainers of the project/repository.

“Work” shall mean the collective software, content, and documentation in this project/repository.
