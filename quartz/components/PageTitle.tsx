import { pathToRoot } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import { i18n } from "../i18n"

const PageTitle: QuartzComponent = ({ fileData, cfg, displayClass }: QuartzComponentProps) => {
  const title = cfg?.pageTitle ?? i18n(cfg.locale).propertyDefaults.title
  const baseDir = pathToRoot(fileData.slug!)
  return (
    <h2 class={classNames(displayClass, "page-title")}>
      <a href={baseDir}>
        <span class="desktop-only">{title}</span>
        <span class="mobile-only">TP</span>
      </a>
    </h2>
  )
}

PageTitle.css = `
.page-title {
  font-size: 1.75rem;
  margin: 0;
  font-family: var(--titleFont);
}

.desktop-only {
  display: initial;
  @media (max-width: 800px) {
    display: none;
  }
}

.mobile-only {
  display: none;
  @media (max-width: 800px) {
    display: initial;
  }
}
`

export default (() => PageTitle) satisfies QuartzComponentConstructor
