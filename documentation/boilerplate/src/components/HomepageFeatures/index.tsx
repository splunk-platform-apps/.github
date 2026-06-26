import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import Link from '@docusaurus/Link';

const FeatureList = [
  {
    title: 'Getting Started',
    to: '/docs',
    Svg: require('@site/static/img/rocket.svg').default,
    description: (
      <>Everything you need to  get up and running.</>
    ),
  },
  {
    title: 'Releases',
    to: '/docs',
    Svg: require('@site/static/img/megaphone.svg').default,
    description: (
      <>View the version history and detailed changelog.</>
    ),
  },
  {
    title: 'Usage',
    to: '/docs',
    Svg: require('@site/static/img/lightbulb.svg').default,
    description: (
      <>Learn how to set up and maximize this app.</>
    ),
  },
  {
    title: 'Compatibility',
    to: '/docs',
    Svg: require('@site/static/img/checkmark.svg').default,
    description: (
      <>Supported Splunk products, versions, platform requirements.</>
    ),
  },
];

function Feature({ title, Svg, description, to }) {
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
