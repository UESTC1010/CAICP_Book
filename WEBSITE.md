# 图书网站维护

网站地址：https://uestc1010.github.io/CAICP_Book/

GitHub Pages 从 `main` 分支根目录发布。首页为 `index.html`；每章保留介绍与小节目录，每个正式小节有独立网页。章末小结与思考题合在同一页，附录按 A—G 分页。

## 更新正文

`book/` 中的 Markdown 是正文来源，修改后在仓库根目录执行：

```sh
python3 -m pip install -r requirements-site.txt
python3 build_site.py
```

将修改后的 Markdown、生成的 HTML 和 `sitemap.xml` 一起提交。仅修改 Markdown 不会自动更新网站正文。章节标题和文件名保持现有规则；如增删章节或改变网址结构，应同步调整生成脚本，并为已发布网址保留跳转。

`site.css` 管理排版，`site.js` 设置公式显示与手机目录。`mathjax-tex-svg.js` 为 MathJax 3.2.2 的本地发行文件，使用 Apache 2.0 许可，许可文本见 `MATHJAX-LICENSE.txt`。公式排版无需外部 CDN。书稿与插图许可仍以 `LICENSE.md` 为准。

## Google Search Console

使用网址前缀资源 `https://uestc1010.github.io/CAICP_Book/`。提交的站点地图为同网址下的 `sitemap.xml`，包括首页、章目录、小节正文、前言和附录。

`google1067b17d6c8eea9b.html` 是 Google 提供的网站所有权验证文件，须持续保留，不要改名或修改内容。它是公开验证文件，不是密码。重新生成网页不会覆盖该文件。

发布后可在 Search Console 中查看抓取、收录和搜索表现。提交站点地图和请求编入索引不代表已收录；实际状态以 Google 后续报告为准。
