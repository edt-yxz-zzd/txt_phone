/**
 * @Copyright Copyright © 2020
 * @Createdon 2020-7-28
 * @Author Panda_YueTao
 * @Version 1.5.0
 * @Title 妈叔出品-LaTeX公式编辑器配置
 */

const Environment = "release";

const Config = {
  development: {
    Version: "开发版" + new Date().getTime()+"yue",
    MainCSS: "style.css",
    MainJS: "main.js",
    Boot_OSS: "..",
    API_Mathpix: "http://localhost:5000/api/mathpix/posttomathpix",
    Hostname: "192.168.1.105",
  },
  development_compress: {
    Version: "开发压缩版" + new Date().getTime(),
    MainCSS: "style.css",
    MainJS: "main.bundle.min.js",
    Boot_OSS: "..",
    API_Mathpix: "https://www.latexlive.com:5001/api/mathpix/posttomathpix",
    Hostname: "192.168.1.105",
  },
  debug: {
    Version: "调试版" + new Date().getTime(),
    MainCSS: "style.min.css",
    MainJS: "main.bundle.min.js",
    Boot_OSS: "https://latexlive-resourse-devlop.oss-cn-beijing.aliyuncs.com",
    API_Mathpix: "https://www.latexlive.com:5001/api/mathpix/posttomathpix",
    Hostname: "www.latexlive.com:5002",
  },
  release: {
    Version: "1.5.2",
    MainCSS: "style.min.css",
    MainJS: "main.bundle.min.js",
    Boot_OSS: "https://latexlive-resourse.oss-cn-beijing.aliyuncs.com",
    API_Mathpix: "https://www.latexlive.com:5001/api/mathpix/posttomathpix",
    Hostname: "www.latexlive.com",
  },
};
