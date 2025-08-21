# Distribution Guidelines

This document will provide an overview of the changes to be applied to Docusaurus assets each time a new repository is created to host a new project or Splunk Platform App.

## Configuration Edits

### Package Information
Modify `package.json` to reflect the targeted project:

```json:my-website-tutorial/package.json
{
  "name": "your-project-name", // TODO: Replace with the actual app name
  "version": "1.0.0", // TODO: Replace with the actual app version
  "private": true,
  // ... rest remains the same
}
```

### Site Settings
Update the `./boilerplate/docusaurus.config.ts` with project information:

```typescript
const app_name: string = '<ADD HERE YOUR APP NAME>';
// e.g. Docusaurus Boilerplate
const repo_name: string = '<ADD HERE YOUR REPO NAME>';
// e.g. boilerplate
const app_descr:string = '<ADD HERE APP DESCRIPTION>';
// e.g. This is a boilerplate app to showcase docusaurus usage for documenting Splunk Apps and Add-Ons
```

## Docusaurus Website Edits

### Homepage
Structure is given by default by adding files such as `./boilerplate/src/components/HomepageFeatures/index.tsx` to the repository to be distributed.

:point_right: Changes to this page may be done in the future prior approval.

### Documentation
At the moment each Splunk Platform App will be asked to provide basic documentation via `<path-to-your-app-src>/docs/readme.md`. This may be re-structured in the future.

:point_right: No changes to be done: `docs/readme-template.md` will be renamed to `docs/readme.md` and added to the repository to be distributed to the requestor.

### Styling
Project styling is given by default by adding themes files such as `./boilerplate/src/css/custom.css` to the repository to be distributed.

:point_right: At the moment, styling is in line with official Splunk branding.

## Other Edits
Before distributing a repository to the requestor, please also make sure:

- `templates/root-README.md`
  - Saved to `<new-repo>/README.md`
  - Edited to report the proper App Name as title