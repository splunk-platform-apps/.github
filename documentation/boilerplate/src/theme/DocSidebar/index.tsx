import React, {type ReactNode} from 'react';
import DocSidebar from '@theme-original/DocSidebar';
import type DocSidebarType from '@theme/DocSidebar';
import type {WrapperProps} from '@docusaurus/types';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

type Props = WrapperProps<typeof DocSidebarType>;

export default function DocSidebarWrapper(props: Props): ReactNode {
  const { siteConfig } = useDocusaurusContext();
  return (
    <>
      <div className="sidebar__repo-name">{siteConfig.projectName?.replaceAll("_", " ")}</div>
      <DocSidebar {...props} />
    </>
  );
}
