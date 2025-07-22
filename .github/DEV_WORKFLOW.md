# Intro for Developers
When contributing to a new project, sometimes getting your development environment set-up just right can be tedious. This document will describe one (or more) ways to get your environment configured. This document describes the ways in which developers have their workstations configured.

**NOTE: This is not a guide on _how_ to develop Splunk apps or add-on (you can find that [here](https://dev.splunk.com/enterprise/docs/developapps), rather it represents how you might configure your workstation to allow for rapid code->deploy->test cycle.**

### Local Development with Visual Studio Code and Docker
We recommend using the official [Splunk Platform Apps Docker image](https://github.com/splunk/splunk-platform-apps/blob/main/0.Initialization/Splunk-Platform-Apps-Docker) for development. This image, based on the official [Docker hub Splunk image](https://hub.docker.com/r/splunk/splunk/), comes with a complete, pre-configured Splunk environment optimized for app development. 

Please follow [setup guidelines](https://github.com/splunk/splunk-platform-apps/blob/main/0.Initialization/Splunk-Platform-Apps-Docker/DEV_GUIDELINES.md) for more details about configuring this image.

### Documentation Expectations
All Splunk Platform Apps must maintain comprehensive documentation following the established guidelines. Please refer to our [documentation guidelines](https://github.com/splunk/splunk-platform-apps/blob/main/0.Initialization/documentation/DEV_GUIDELINES.md) to learn more about:

- Required structure and files
- Content expectations and templates
- Automated quality checks and deployment process

Developers are responsible for maintaining accurate and complete documentation while following the pre-configured templates and structure.
