# Community, Developer, and Splunk Supported Apps

>TODO verify this content

You may have noticed that Splunk Apps can be community, developer, or Splunk-supported. This document explains what each level of support means.

App Tests  | Community Supported | Developer Supported
------------- | ------------- | ------------- |
Quality Tests | * | *
Compile Tests | * | *
Security Review | * | *
Linting | * | *
Code Review | * | *
Content Review |  | *
Full Functionality Testing | | Developer Dependent
Regular Regression Testing | | Developer Dependent

***

## Community Supported App Testing

### Quality Tests
Checks for various code issues without executing the code

### Compile Tests
Checks that the app successfully installs on a Splunk instance

### Security Review
Security checks are performed. The security review ensures no malicious code, libraries, or other content is published through the app listings

### Linting
Enforces common Python code standards using standard tools

### Code Review
The team conducts a code review.

### Content Review
The team conducts a content review.  Common checks include:

* Would this update break existing user workflows?
* Is this update something that all users of the app can take advantage of?
* Does the update leverage an officially supported API on the partner product?
* Does this update expose functionality that is excessively difficult to use or understand?


## Developer Supported App Testing
The developer-supported apps should cover all tests done for community-supported apps. However, additional testing is typically done at the developer's discretion, and how they perform their testing may vary. Often developer supported apps will include their own version of full-functionality testing, regular regression testing, and more.
