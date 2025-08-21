import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'boilerplate', // TODO: Replace with the actual app name
  tagline: 'This is a boilerplate app to showcase docusaurus usage for documenting Splunk Apps and Add-Ons', // TODO: Replace with the actual app description
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://splunk-platform-apps.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'splunk-platform-apps',
  projectName: 'splunk-platform-apps.github.io',
  trailingSlash: false,
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts'
        },
        theme: {
          customCss: ['./src/css/custom.css', './src/css/fonts.css']
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docs-readme-template.png',
    navbar: {
      title: 'boilerplate', // TODO: Replace with the actual app name
      logo: {
        alt: 'Splunk Logo',
        src: 'img/logo.svg',
        srcDark: 'img/logo-dark.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Documentation',
        },
        {
          href: 'https://github.com/splunk-platform-apps/boilerplate', // TODO: Replace with the actual GitHub link
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Documentation',
              to: 'docs',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/splunk-platform-apps/boilerplate', // TODO: Replace with the actual GitHub link
            },
            {
              label: 'Community Slack',
              href: 'https://splunk-usergroups.slack.com/app_redirect?channel=appdev'
            }
          ],
        },
        {
          title: 'More',
          items: [
            {label: 'Legal', href: 'https://www.splunk.com/en_us/legal.html'},
            {label: 'Patents', href: 'https://www.splunk.com/en_us/legal/patents.html'},
            {label: 'Privacy', href: 'https://www.splunk.com/en_us/legal/privacy-policy.html?301=/en_us/legal/privacy/privacy-policy.html'}
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Splunk LLC All rights reserved.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
