import { htmlToJsx } from "../../util/jsx"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../types"

const Content: QuartzComponent = ({ fileData, tree }: QuartzComponentProps) => {
  const { speaker, source } = fileData.frontmatter ?? {}
  const content = htmlToJsx(fileData.filePath!, tree)
  const classes: string[] = fileData.frontmatter?.cssclasses ?? []
  const classString = ["popover-hint", ...classes].join(" ")
  return <article class={classString}>
    <div class="article-header">
    {speaker && (
      <div class="frontmatter">
        <div class="speaker">{speaker}</div>
        {source && (
  <div class="source">
    {/* Extract URL and text from markdown-style link */}
    {source.match(/\[(.*?)\]\((.*?)\)/) ? (
      source.split(',').map((link, i) => {
        const [_, text, url] = link.trim().match(/\[(.*?)\]\((.*?)\)/) || [];
        return (
          <>
            <a href={url} target="_blank" rel="noopener noreferrer">
              {text}
            </a>
            {i < source.split(',').length - 1 && ', '}
          </>
        );
      })
    ) : (
      <a href={source} target="_blank" rel="noopener noreferrer">
        {source}
      </a>
    )}
  </div>
)}
      </div>
    )}
  </div>
    {content}</article>
}

export default (() => Content) satisfies QuartzComponentConstructor