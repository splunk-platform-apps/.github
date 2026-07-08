# Admin Operations

## Approving New Repository Requests

Repository requests are tracked via issues in the `.github` repository. Only [admins](https://github.com/orgs/splunk-platform-apps/teams/admins) are authorized to approve such requests.

### Steps to Approve a New Repository Request

1. **Review the Request**
   - Open the issue requesting the new repository.
   - Verify that the request includes required information.

2. **Confirm Approval Criteria**
   - Ensure the request follows organization guidelines and conventions as outlined in [CONVENTIONS.md](./CONVENTIONS.md).
   - Check for duplicate or conflicting repository names.

   > Since the repository name is often matching the app ID please check it is also unique among apps published in Splunkbase! :construction:

3. **Approve the Request**
   - Add label `approved` to the issue.

4. **Create the Repository**
   - Automation in place will create the repository and notify the requestor by providing a link to the repository in a comment.

   :link: [Repository bootstrap](https://splunk.atlassian.net/wiki/spaces/FO/pages/1079127965716/Workflows+and+Technology)

## Tagging Workflows

Only [admins](https://github.com/orgs/splunk-platform-apps/teams/admins) are authorized to create tags.

**Steps:**
1. Ensure all workflow changes are merged into the `main` branch.
2. Create a new tag on the `main` branch replacing the `x` opportunely.

     ```
     git checkout main
     git pull
     git tag -a v1.x.x <commit-sha> -m "v1.x.x add here your message"
     git push origin tag v1.x.x
     ```

3. Confirm the tag appears in the repository.

### Creating a Major Tag Pointing to the Latest Patch Tag

To create a tag `v1` that points to the same commit as `v1.x.x` (e.g. `v1.0.0`):

```bash
# Identify the commit SHA that 1.x.x points to
# or copy it from the GitHub Web Interface
git rev-parse v1.x.x
# Create the 1 tag at that same commit
git tag v1 <commit-sha>
git push origin v1
```

By creating such a tag and updating it as soon as a latest patch or minor tag is available, consumers can:

- reference workflows by major tag only: `.github/workflows/reusable.yml@v1`
- be sure it will be using the most recent workflows

**Updating a Major Tag Pointing to the Latest Tag**

To update tag `v1` to point to a new patch tag `v1.x.y` (e.g. `v1.0.1`):

```bash
# Checkout the latest release version
git checkout v1.x.y
# Force-create the tag locally. Moves the tag 1 to your current commit
git tag -fa v1 -m "Update version v1 to point to v1.x.y"
# Force-push the tag to github
git push origin v1 --force
```
