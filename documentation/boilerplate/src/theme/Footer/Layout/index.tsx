import React, {type ReactNode} from 'react';
import clsx from 'clsx';
import {ThemeClassNames} from '@docusaurus/theme-common';
import type {Props} from '@theme/Footer/Layout';

export default function FooterLayout({
  style,
  links,
  logo,
  copyright,
}: Props): ReactNode {
  return (
    <footer
      className={clsx(ThemeClassNames.layout.footer.container, 'footer', {
        'footer--dark': style === 'dark',
      })}>
      <div className="container footer__two-cols">
        <div className="footer__col-left">
          {logo && <div className="footer__logo-wrapper">{logo}</div>}
          {copyright && (
            <div className="footer__copyright-wrapper">{copyright}</div>
          )}
        </div>
        <div className="footer__col-right">{links}</div>
      </div>
      {/* <div className="container container-fluid">
        {links}
        {(logo || copyright) && (
          <div className="footer__bottom text--center">
            {logo && <div className="margin-bottom--sm">{logo}</div>}
            {copyright}
          </div>
        )}
      </div> */}
    </footer>
  );
}
