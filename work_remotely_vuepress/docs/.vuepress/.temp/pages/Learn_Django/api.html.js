import comp from "F:/Work_Remotely/work_remotely_vuepress/docs/.vuepress/.temp/pages/Learn_Django/api.html.vue"
const data = JSON.parse("{\"path\":\"/Learn_Django/api.html\",\"title\":\"Django Page Api\",\"lang\":\"en-US\",\"frontmatter\":{},\"headers\":[{\"level\":2,\"title\":\"All\",\"slug\":\"all\",\"link\":\"#all\",\"children\":[]},{\"level\":2,\"title\":\"Single\",\"slug\":\"single\",\"link\":\"#single\",\"children\":[]}],\"git\":{},\"filePathRelative\":\"Learn_Django/api.md\"}")
export { comp, data }

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
