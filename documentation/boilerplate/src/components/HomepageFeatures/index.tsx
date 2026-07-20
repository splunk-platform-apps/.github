import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { useAllDocsData } from '@docusaurus/plugin-content-docs/client';
import Link from '@docusaurus/Link';


const FeatureList = [
  {
    title: 'Getting Started',
    keyword: 'getting_started',
    to: '/docs',
    Svg: require('@site/static/img/rocket.svg').default,
    description: (
      <>Everything you need to  get up and running.</>
    ),
  },
  {
    title: 'Releases',
    keyword: 'releases',
    to: '/docs',
    Svg: require('@site/static/img/megaphone.svg').default,
    description: (
      <>View the version history and detailed changelog.</>
    ),
  },
  {
    title: 'Usage',
    keyword: ['usage', 'configuration'],
    to: '/docs',
    Svg: require('@site/static/img/lightbulb.svg').default,
    description: (
      <>Learn how to set up and maximize this app.</>
    ),
  },
  {
    title: 'Compatibility',
    to: '/docs',
    keyword: 'versions-supported',
    Svg: require('@site/static/img/checkmark.svg').default,
    description: (
      <>Supported Splunk products, versions, platform requirements.</>
    ),
  },
];

function getCardLink(to, searchText, allDocsData){
  // remove dashes, underscores, spaces from strings
  const normalize = (str) =>
    (str ?? '').toLowerCase().replace(/[-_\s]/g, '');

  // keywords could be a single string OR an array — normalize to an array
  const keywords = Array.isArray(searchText) ? searchText : [searchText];
  const targets = keywords
    .map(normalize)
    .filter((t) => t.length > 0); // drop empties so we don't match everything

  const allDocs = Object.values(allDocsData).flatMap((plugin) =>
    Object.values(plugin.versions).flatMap((v) => v.docs)
  );

  // Find match on id (case-insensitive to be safe: readme / README)
  const defaultDoc = allDocs.find(
    (doc) => doc.id?.toLowerCase() === 'readme'
  );

  // Find match on path (keywords part of it)
  const introDoc = targets.length === 0 ? undefined : allDocs.find((doc) => {
        const docPath = normalize(doc.path);
        return targets.some((t) => docPath.includes(t));
      }
    );
  const anchorSource = Array.isArray(searchText) ? searchText[0] : searchText;
  const anchor = (anchorSource ?? '').replaceAll('_', '-');

  // Fallback is always /docs basically
  return introDoc
    ? `${introDoc.path}#${anchor}`
    : (defaultDoc ? `${defaultDoc.path}#${anchor}` : to);
}

function Feature({ title, Svg, description, to, keyword }) {
  const allDocsData = useAllDocsData();
  const { siteConfig } = useDocusaurusContext();
  const { organizationName, projectName } = siteConfig;
  const releasesUrl = `https://github.com/${organizationName}/${projectName}/releases`;

  // Assigning links to each card
  to = getCardLink(to, keyword, allDocsData);

  if (title == 'Releases') {
    to = releasesUrl;
  }

  return (
    <div className={clsx('col col--6', styles.featureItem)}>
      <Link to={to} className={styles.card}>
        <div className="text--center">
          <Svg className={styles.featureSvg} role="img" />
        </div>
        <div className="text--center padding-horiz--md">
          <Heading as="h3">{title}</Heading>
          <p>{description}</p>
        </div>
      </Link >
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <svg width="0" height="0" style={{ position: 'absolute' }} aria-hidden="true">
        <defs>
          <linearGradient id="featureGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="5%" style={{ stopColor: 'var(--feature-splk-color-1)' }} />
            <stop offset="40%" style={{ stopColor: 'var(--feature-splk-color-2)' }} />
            <stop offset="85%" style={{ stopColor: 'var(--feature-splk-color-3)' }} />
          </linearGradient>
        </defs>
      </svg>

      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
