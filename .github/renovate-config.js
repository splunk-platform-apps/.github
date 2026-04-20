module.exports = {
    platform: 'github',
    // Author must match the one opening PRs -> Use github app name
    username: 'renovate4splunk-platform-apps[bot]',
    gitAuthor: 'renovate4splunk-platform-apps <renovate4splunk-platform-apps[bot]@users.noreply.github.com>',

    // Organization setup
    autodiscover: true,
    autodiscoverFilter: [
        'splunk-platform-apps/*',
        '!splunk-platform-apps/splunkcommunity-vale'
    ],

    // Require some config
    // -> repos without a config will be skipped after onboarding PR
    requireConfig: 'optional',

    // pre-commit functionality is in beta testing
    // -> opt-in to test it
    "pre-commit": {
        "enabled": true
    },

    // Managers
    enabledManagers: [
        'github-actions',
        // 'docker',
        'npm',
        "pre-commit",
        'regex'
    ],

    // Global settings
    dependencyDashboard: false,
    dependencyDashboardTitle: '🔄 Dependency Updates Dashboard',

    // Commit messages
    semanticCommits: 'enabled',
    commitMessagePrefix: 'chore(deps):',

    // PR settings
    prConcurrentLimit: 10,
    prHourlyLimit: 0, // No limit
    branchConcurrentLimit: 20,

    // To reduce PR rebases
    rebaseWhen: 'behind-base-branch',

    // Branch cleanup and recreation settings
    branchPrefix: 'renovate/',

    // Labels
    labels: ['dependency-update', 'renovate', 'automerge-enabled' ],

    // Assignees/Reviewers
    reviewersFromCodeOwners: true,

    // Allow the following setting only for testing purposes
    // recreateClosed: true,

    regexManagers: [
        {
            description: 'Detect Docker images in GitHub Actions matrix with renovate comments',
            managerFilePatterns: [
                '/^\\.github/workflows/.+\\.ya?ml$/'
            ],
            matchStrings: [
                "-\\s+\"(?<currentValue>[^\"]+)\"\\s+#\\s+renovate:\\s+datasource=(?<datasource>\\S+)\\s+depName=(?<depName>\\S+)"
            ],
            // depNameTemplate: '{{depName}}',
            versioningTemplate: 'docker'
        }
    ],

    // Package rules
    // !! Evaluated **in order**: later rules override earlier ones for overlapping matches !!
    packageRules: [
        {
            description: "Auto-update 9.3.x patches only",
            matchDatasources: [ "docker" ],
            matchPackageNames: [ "splunk/splunk" ],
            matchCurrentVersion: "/^9\\.3\\./",
            allowedVersions: "9.3.x",
            automerge: true,
            automergeType: "pr",
            platformAutomerge: true,
            minimumReleaseAge: "3 days",  // Wait for stability
            groupName: "Splunk 9.3.x Patches"
        },
        {
            description: "Auto-update 9.4.x patches only",
            matchDatasources: [ "docker" ],
            matchPackageNames: [ "splunk/splunk" ],
            matchCurrentVersion: "/^9\\.4\\./",
            matchUpdateTypes: [ "patch" ],
            automerge: true,
            automergeType: "pr",
            platformAutomerge: true,
            minimumReleaseAge: "3 days",
            groupName: "Splunk 9.4.x Patches"
        },
        {
            description: "Notify 9.4.x minor/major updates availability",
            matchDatasources: [ "docker" ],
            matchPackageNames: [ "splunk/splunk" ],
            matchCurrentVersion: "/^9\\.4\\./",
            matchUpdateTypes: [ "minor", "major" ],
            minimumReleaseAge: "3 days",
            labels: [ 'dependency-update', 'renovate', 'needs-review' ],
            groupName: "Splunk 9.4.x Major/Minor Available"
        },
        // GitHub Actions specific
        {
            description: "Update all public GitHub Actions",
            matchManagers: ["github-actions"],
            groupName: "Public GitHub actions",
            // Ensures to get PRs for major updates (v4 -> v5)
            separateMajorMinor: true,
            excludePackagePatterns: ["^splunk-platform-apps/"],
            labels: ['dependency-update', 'renovate', 'needs-review'],
            minimumReleaseAge: "3 days"
        },
        {
            description: "Update internal reusable workflows",
            matchManagers: ["github-actions"],
            matchPackagePatterns: ["^splunk-platform-apps/"],
            groupName: "Internal Reusable Workflows",
            versioning: "docker",
            automerge: true,
            automergeType: "pr",
            platformAutomerge: true,
            minimumReleaseAge: "3 days"
        },
        // All npm dependencies (from package.json)
        {
            matchManagers: ["npm"],
            description: "Update all npm dependencies",
            groupName: "all npm dependencies",
            matchUpdateTypes: ["minor", "major"],
            automerge: true,
            automergeType: "pr",
            platformAutomerge: true,
            minimumReleaseAge: "3 days"
        },
        // Docusaurus specific
        {
            extends: [ "monorepo:docusaurus" ],
            description: "Update docusaurus and its dependencies",
            groupName: "docusaurus monorepo",
            matchUpdateTypes: [ "minor", "major" ],
            automerge: true,
            automergeType: "pr",
            platformAutomerge: true,
            minimumReleaseAge: "3 days"
        },
        // pre-commit hooks updates
        {
            matchManagers: ["pre-commit"],
            groupName: "Update pre-commit hooks",
            automerge: true,
            automergeType: "pr",
            platformAutomerge: true,
            minimumReleaseAge: "3 days"
        }
    ]
};