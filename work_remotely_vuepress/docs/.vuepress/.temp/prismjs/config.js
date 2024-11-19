import "F:/Work_Remotely/work_remotely_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/styles/base.css"
import "F:/Work_Remotely/work_remotely_vuepress/node_modules/@vuepress/plugin-prismjs/lib/client/styles/nord.css"
import "F:/Work_Remotely/work_remotely_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/styles/line-numbers.css"
import "F:/Work_Remotely/work_remotely_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/styles/notation-highlight.css"
import "F:/Work_Remotely/work_remotely_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/styles/collapsed-lines.css"
import { setupCollapsedLines } from "F:/Work_Remotely/work_remotely_vuepress/node_modules/@vuepress/highlighter-helper/lib/client/composables/collapsedLines.js"

export default {
  setup() {
    setupCollapsedLines()
  }
}
