import { QuartzTransformerPlugin } from "../types"
import { PluggableList } from "unified"
import { Root } from "hast"
import { visit } from "unist-util-visit"
import { execSync } from "child_process"
import path from "path"
import fs from "fs"

export interface Options {
  enableAutoGeneration: boolean
  slideDirectories: string[]
}

const defaultOptions: Options = {
  enableAutoGeneration: true,
  slideDirectories: ["paige-ai-report", "presentations"]
}

export const SlideshowGenerator: QuartzTransformerPlugin<Partial<Options> | undefined> = (userOpts) => {
  const opts = { ...defaultOptions, ...userOpts }
  
  return {
    name: "SlideshowGenerator",
    markdownPlugins() {
      return []
    },
    htmlPlugins(): PluggableList {
      return [
        () => {
          return (tree: Root, file) => {
            if (!opts.enableAutoGeneration) return

            // Check if this is a slideshow directory
            const filePath = file.path
            if (!filePath) return

            const isSlideDirectory = opts.slideDirectories.some(dir => 
              filePath.includes(dir) && filePath.includes("/slides/")
            )

            if (isSlideDirectory) {
              // Find the parent directory containing build-slideshow.js
              const pathParts = filePath.split("/")
              let buildScriptPath = ""
              
              for (let i = pathParts.length - 1; i >= 0; i--) {
                const testPath = pathParts.slice(0, i + 1).join("/")
                const scriptPath = path.join(testPath, "build-slideshow.js")
                
                if (fs.existsSync(scriptPath)) {
                  buildScriptPath = testPath
                  break
                }
              }

              if (buildScriptPath) {
                try {
                  console.log(`🔨 Auto-generating slideshow for ${buildScriptPath}`)
                  execSync("node build-slideshow.js", { 
                    cwd: buildScriptPath,
                    stdio: "inherit"
                  })
                  console.log(`✅ Slideshow generated successfully`)
                } catch (error) {
                  console.error(`❌ Error generating slideshow:`, error)
                }
              }
            }
          }
        }
      ]
    }
  }
} 