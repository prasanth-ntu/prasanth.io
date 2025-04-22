import { Octokit } from 'octokit'
import { useEffect, useState } from 'react'
import ReactMarkdown from 'react-markdown'
import { QuartzComponentConstructor, QuartzComponentProps } from './types'

// Initialize Octokit without token for public repos
const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN, // Will fall back to unauthenticated for public repos if token not present
})

function GitHubReadmeContent({ owner, repo }: { owner: string; repo: string }) {
  const [readmeContent, setReadmeContent] = useState<string>('')
  const [error, setError] = useState<string | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    const fetchReadme = async () => {
      try {
        setIsLoading(true)
        const response = await octokit.rest.repos.getReadme({
          owner,
          repo,
          mediaType: {
            format: 'raw',
          },
        })

        if (response.data) {
          setReadmeContent(response.data as string)
          setError(null)
        }
      } catch (err) {
        console.error('Error fetching README:', err)
        setError('Failed to fetch README content. Please check the repository URL.')
      } finally {
        setIsLoading(false)
      }
    }

    if (owner && repo) {
      fetchReadme()
    }
  }, [owner, repo])

  if (isLoading) {
    return <div className="github-readme-loading">Loading README...</div>
  }

  if (error) {
    return <div className="github-readme-error">{error}</div>
  }

  return (
    <div className="github-readme">
      <div className="github-readme-header">
        <a href={`https://github.com/${owner}/${repo}`} target="_blank" rel="noopener noreferrer">
          View on GitHub
        </a>
      </div>
      <div className="github-readme-content">
        <ReactMarkdown>{readmeContent}</ReactMarkdown>
      </div>
    </div>
  )
}

export default (() => {
  function GitHubReadme(props: QuartzComponentProps) {
    const attrs = props.fileData.frontmatter
    const owner = attrs?.github_owner as string
    const repo = attrs?.github_repo as string

    if (!owner || !repo) {
      return (
        <div className="github-readme-error">
          Please provide github_owner and github_repo in frontmatter
        </div>
      )
    }

    return <GitHubReadmeContent owner={owner} repo={repo} />
  }

  GitHubReadme.css = `
    .github-readme {
      padding: 1rem;
      background-color: var(--light);
      border-radius: 8px;
      margin: 1rem 0;
      border: 1px solid var(--lightgray);
    }
    
    .github-readme-header {
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--lightgray);
    }
    
    .github-readme-header a {
      color: var(--secondary);
      text-decoration: none;
      font-weight: 500;
    }
    
    .github-readme-header a:hover {
      text-decoration: underline;
    }
    
    .github-readme-content {
      overflow-x: auto;
    }
    
    .github-readme-error {
      color: var(--red);
      padding: 1rem;
      border: 1px solid var(--red);
      border-radius: 8px;
      margin: 1rem 0;
    }
    
    .github-readme-loading {
      padding: 1rem;
      color: var(--gray);
      text-align: center;
      border: 1px solid var(--lightgray);
      border-radius: 8px;
      margin: 1rem 0;
    }
  `

  return GitHubReadme
}) satisfies QuartzComponentConstructor 