"""Build the public reading site from book/*.md. See WEBSITE.md."""
from pathlib import Path
import re, json, html
import markdown
ROOT=Path(__file__).resolve().parent
BASE='https://uestc1010.github.io/CAICP_Book/'
REPO='https://github.com/UESTC1010/CAICP_Book'
GA_MEASUREMENT_ID='G-4TK50WBGCC'
BING_SITE_VERIFICATION='1087DE7226FACD543D8A8AE81B738830'
TITLE='从零开始学人工智能：中学生 CAICP 学习指南'
PDF=REPO+'/releases/download/v0.9/CAICP_Book-v0.9.pdf'
files=[ROOT/'book/前言.md']+[next((ROOT/'book').glob(f'第{i}章_*.md')) for i in '一二三四五六七八']+[ROOT/'book/附录.md']
slugs=['preface']+[f'chapter-{i}' for i in range(1,9)]+['appendix']
titles=[p.read_text().splitlines()[0].lstrip('# ') for p in files]
descs=['为什么写这本书，以及怎样理解正在变化的人工智能。','从数据、算法与算力开始，认识人工智能能做什么，也理解它的局限。','变量、条件、循环、函数与程序调试，逐步写出能解决问题的 Python 程序。','逻辑、统计、方程、函数、向量和概率，为理解模型打下数学基础。','从枚举、查找和排序，到树、图与搜索，学习把问题变成可以执行的步骤。','认识学习任务、数据预处理、训练与评估，走过一个机器学习项目的基本过程。','从回归和分类，到神经网络、梯度下降与卷积，理解模型内部的工作方式。','使用 NumPy、Pandas、Matplotlib 和 scikit-learn，把知识落实到数据与程序中。','走近大模型、智能体与人工智能应用，讨论技术的发展及其影响。','大纲对应表、术语与符号、分级阅读路线，及 E、J、S 三套原创模拟题与解析。']
def esc(s):return html.escape(s,quote=True)
def header():return f'''<a class="skip" href="#main">跳到正文</a><header class="topbar"><a class="brand" href="./"><span class="brand-mark">AI</span><span>中学生 CAICP 学习指南</span></a><nav aria-label="主导航"><a href="./#contents">全书目录</a><a href="{PDF}">下载 PDF</a><a href="{REPO}">GitHub ↗</a></nav></header>'''
def footer():return f'''<footer class="footer"><span>陈峥 著 · 公开试读版 v0.9</span><span><a href="{REPO}/blob/main/LICENSE.md">正文与插图 CC BY-NC-SA 4.0</a> · <a href="{REPO}/issues">勘误与建议 ↗</a><br><a href="privacy.html">隐私与访问统计</a> · <button type="button" class="analytics-link" data-analytics-settings hidden>访问统计设置</button></span></footer><section id="analytics-choice" class="analytics-choice" aria-label="访问统计选择" hidden><p>允许使用 Cookie 统计访问量和热门章节吗？数据由 Google Analytics 处理，拒绝不影响阅读。<a href="privacy.html">了解详情</a></p><div><button type="button" data-analytics-choice="deny">不参与</button><button type="button" data-analytics-choice="allow">允许统计</button></div></section>'''
def page(title,desc,slug,body,reader=False):
 url=BASE+(slug+'.html' if slug else '')
 verification=f'<meta name="msvalidate.01" content="{BING_SITE_VERIFICATION}">' if not slug else ''
 schema={'@context':'https://schema.org','@type':'Book' if not slug else 'WebPage','name':title,'inLanguage':'zh-CN','url':url,'author':{'@type':'Person','name':'陈峥'},'description':desc}
 if not slug:schema.update({'bookFormat':'https://schema.org/EBook','image':BASE+'assets/cover.png','license':'https://creativecommons.org/licenses/by-nc-sa/4.0/','isAccessibleForFree':True})
 return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">{verification}<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><meta name="author" content="陈峥"><link rel="canonical" href="{url}"><link rel="icon" type="image/svg+xml" href="favicon.svg"><meta name="theme-color" content="#173c46"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="{'article' if reader else 'book'}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}assets/cover.png"><link rel="stylesheet" href="site.css"><script defer src="analytics.js" data-measurement-id="{GA_MEASUREMENT_ID}"></script><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>{'<script defer src="site.js"></script><script defer src="mathjax-tex-svg.js"></script>' if reader else ''}</head><body>{header()}{body}{footer()}</body></html>'''
# Split long chapters at second-level headings. Keep chapter introductions as landing pages.
entries=[]
chapter_sections={}
for path,slug,title,desc in zip(files,slugs,titles,descs):
 source='\n'.join(path.read_text(encoding='utf-8').splitlines()[1:]).replace('../assets/','assets/')
 pieces=re.split(r'^## (.+)$',source,flags=re.M)
 sections=[]
 for j in range(1,len(pieces),2):
  label=pieces[j].strip(); text=pieces[j+1]
  if label=='想一想' and sections and sections[-1]['slug'].endswith('-review'):
   sections[-1]['text']+='\n## 想一想\n'+text
   continue
  if label=='本章小结': suffix='review'; label='本章小结与想一想'
  elif slug=='appendix':suffix=label.split()[0].lower()
  else:suffix=label.split()[0].replace('.','-')
  section_slug=slug+'-'+suffix if slug=='appendix' or suffix=='review' else 'section-'+suffix
  sections.append(dict(slug=section_slug,title=label,text=text,chapter=slug,desc=label+'。'+desc,landing=False))
 chapter_sections[slug]=sections
 intro=pieces[0]
 if sections:
  intro+='\n<div class="chapter-contents"><p class="section-label">本章目录</p>'+''.join('<a href="'+e['slug']+'.html">'+esc(e['title'])+' <span>→</span></a>' for e in sections)+'</div>\n'
 entries.append(dict(slug=slug,title=title,text=intro,chapter=slug,desc=desc,landing=True))
 entries.extend(sections)
for idx,entry in enumerate(entries):
 slug,title,desc=entry['slug'],entry['title'],entry['desc']
 md=markdown.Markdown(extensions=['tables','fenced_code','toc','pymdownx.arithmatex'],extension_configs={'toc':{'toc_depth':'2-3','permalink':False},'pymdownx.arithmatex':{'generic':True}})
 content=md.convert(entry['text'])
 content=re.sub(r'<table>(.*?)</table>',r'<div class="table-scroll" tabindex="0" role="region" aria-label="数据表格"><table>\1</table></div>',content,flags=re.S)
 content=re.sub(r'<p>(<img [^>]+>)</p>\s*<p>(图\s*[^<]+)</p>',r'<figure>\1<figcaption>\2</figcaption></figure>',content)
 content=content.replace('<img ','<img loading="lazy" decoding="async" ')
 chapterlist=''.join(f'<a href="{s}.html"'+(' aria-current="page"' if s==entry['chapter'] else '')+f'>{esc(t)}</a>' for s,t in zip(slugs,titles))
 sectionlist=''.join('<a href="'+e['slug']+'.html"'+(' aria-current="page"' if e['slug']==slug else '')+'>'+esc(e['title'])+'</a>' for e in chapter_sections[entry['chapter']])
 chapteridx=slugs.index(entry['chapter'])
 sectionnav='<details class="section-nav" open><summary>本章小节</summary><nav aria-label="小节目录">'+sectionlist+'</nav></details>' if sectionlist else ''
 prev=f'<a href="{entries[idx-1]["slug"]}.html"><small>上一篇</small>{entries[idx-1]["title"]}</a>' if idx else '<a href="./"><small>返回</small>图书首页</a>'
 nxt=f'<a href="{entries[idx+1]["slug"]}.html"><small>下一篇</small>{entries[idx+1]["title"]} →</a>' if idx<len(entries)-1 else '<a href="./#contents"><small>读完之后</small>返回全书目录 →</a>'
 crumb='<a href="./">图书首页</a>' if entry['landing'] else '<a href="'+entry['chapter']+'.html">'+titles[chapteridx]+'</a>'
 body=f'''<div class="reader-layout"><aside class="sidebar"><details class="book-nav" open><summary>全书目录</summary><nav aria-label="章节目录">{chapterlist}</nav></details>{sectionnav}</aside><main id="main" class="reading"><div class="reading-meta">{crumb}<span>v0.9</span></div><article><h1>{title}</h1>{content}</article><nav class="pager" aria-label="前后篇目">{prev}{nxt}</nav><p class="reader-note">发现错误或有没讲清楚的地方？欢迎<a href="{REPO}/issues">提交勘误与建议</a>。请注明章节及原文。</p></main></div><a class="back-top" href="#main" aria-label="返回正文顶部">↑</a>'''
 (ROOT/(slug+'.html')).write_text(page(title+'｜'+TITLE,desc,slug,body,True),encoding='utf-8')
rows=''
for i in range(1,9):
 name=titles[i].split(' ',1)[1]
 rows+=f'<a class="chapter-row" href="{slugs[i]}.html"><span class="chapter-number">{i:02d}</span><div><h3>{name}</h3><p>{descs[i]}</p></div><span class="row-arrow" aria-hidden="true">↗</span></a>'
body=f'''<main id="main"><section class="hero wrap"><div class="hero-copy"><p class="eyebrow">一本写给中学生的人工智能入门书</p><h1>从零开始<br>学人工智能<span>中学生 CAICP 学习指南</span></h1><p class="hero-desc">从第一行 Python，到理解机器怎样学习。<br>把人工智能的基础知识，一步一步讲清楚。</p><p class="author">陈峥 著</p><div class="hero-actions"><a class="button primary" href="chapter-1.html">开始阅读 <span>→</span></a><a class="button secondary" href="{PDF}">下载完整 PDF <span>↓</span></a></div><p class="edition">公开试读版 v0.9 · 免费阅读 · PDF 289 页</p></div><div class="cover-scene"><div class="cover-halo"></div><img class="book-cover" src="assets/cover.png" alt="《从零开始学人工智能：中学生 CAICP 学习指南》封面" fetchpriority="high"><span class="cover-caption">从基础出发，走近人工智能。</span></div></section><section class="intro wrap"><p class="section-label">关于这本书</p><div><h2>从“会使用”，走向“能理解”。</h2><p>人工智能已经进入日常生活。它怎样识别图片，怎样从数据中发现规律，又为什么会给出错误的答案？理解这些问题，需要一点编程、一点数学，也需要把零散的知识连起来。</p><p>这本书起于给初一孩子辅导 CAICP 时的一个困难：有大纲和样题，却缺少适合中学生从头学习的配套教材。全书从基础概念讲起，逐步介绍算法、机器学习与常见模型，配有插图、Python 示例和章末思考题，供学生自学，也供家长与老师参考。</p><a class="text-link" href="preface.html">读一读前言 →</a></div></section><section id="contents" class="contents wrap"><div class="section-heading"><div><p class="section-label">全书目录</p><h2>八章，循序展开。</h2></div><p>可以从第一章读起，也可以回到需要的地方。</p></div><div class="chapter-list">{rows}</div><a class="appendix-row" href="appendix.html"><span>附录</span><div><h3>查阅、练习与回顾</h3><p>大纲对应表 · 术语与符号 · 分级阅读路线 · E / J / S 原创模拟题及解析</p></div><span aria-hidden="true">↗</span></a></section><section class="resources wrap"><div><p class="section-label">配套资料</p><h2>边读，边动手。</h2><p>示例代码按章节整理。完整书稿和插图源文件也已公开，欢迎一起修订。</p></div><div class="resource-links"><a href="{REPO}/tree/main/code"><span>Python 示例代码<small>查看程序与运行说明</small></span>↗</a><a href="{REPO}/releases/tag/v0.9"><span>完整 PDF 与可编辑源文件<small>下载本版书稿和配套资料</small></span>↗</a><a href="{REPO}/issues"><span>勘误与建议<small>帮助这本书把知识讲得更清楚</small></span>↗</a></div></section><section class="about wrap"><p><strong>关于作者</strong>　陈峥，电子科技大学信息与软件工程学院副教授，长期从事人工智能与自然语言处理相关课程教学。</p><p>CAICP 是 IOAI（国际人工智能奥林匹克）中国区面向中小学生开展的人工智能能力认证活动。本书依据编写时的 2025 年资料独立编写，并非官方指定教材；认证要求以官方最新公布为准。</p><p>正文、原创插图及模拟题允许在署名、注明修改并遵守相同许可的前提下非商业分享与改编；独立示例代码与随附示例数据采用 MIT 许可。<a href="{REPO}/blob/main/LICENSE.md">查看使用许可</a>。</p></section></main>'''
(ROOT/'index.html').write_text(page(TITLE+'｜免费在线阅读', '陈峥著，面向中学生的 CAICP 人工智能学习指南。免费在线阅读全书八章，学习 Python、数学基础、算法、机器学习与神经网络，下载完整 PDF 和示例代码。','',body),encoding='utf-8')
privacy_body='''<main id="main" class="privacy-page wrap"><article><p class="eyebrow">网站说明</p><h1>隐私与访问统计</h1><p>这个网站由陈峥维护，提供《从零开始学人工智能：中学生 CAICP 学习指南》的免费在线阅读。我们使用 Google Analytics 4（GA4）了解有多少人访问、哪些章节被阅读，以及 PDF 下载链接的点击情况，用于改进本书和网站。</p><h2>统计什么时候开启？</h2><p>只有在点击“允许统计”后，网站才会加载 Google 的统计脚本。选择“不参与”或暂时不作选择，都可以照常阅读和下载。本网站不使用这些数据投放广告，不开启 Google 信号或广告个性化。</p><h2>会记录什么？</h2><p>开启后，Google Analytics 会使用 Cookie 区分浏览器，记录浏览的页面、停留与滚动情况、链接点击，以及来源网站、设备类型和大致地区等信息。统计数据会发送给 Google 处理。我们不会向统计服务提供姓名、邮箱、手机号，也不设置个人账号标识；网页地址和来源地址中的查询参数、片段信息会在初始页面统计中移除。这不等于完全匿名。</p><p>有关 Google 如何处理这些数据，请阅读<a href="https://policies.google.com/technologies/partner-sites?hl=zh-CN">Google 对合作网站和应用数据的说明</a>及<a href="https://policies.google.com/privacy?hl=zh-CN">Google 隐私权政策</a>。</p><h2>怎样改变选择？</h2><p>可随时使用页脚的“访问统计设置”改变选择。关闭后，本浏览器停止发送后续统计，并删除本网站设置的统计 Cookie；已经发送给 Google 的数据不会因此自动撤回。选择保存在当前浏览器中，最长记忆 180 天。更换设备、清理浏览器数据或选择到期后，需要重新选择。</p><p id="analytics-status" role="status">未开启 JavaScript 时，本网站不会加载访问统计。</p><p><button type="button" class="button secondary" data-analytics-settings hidden>修改统计选择</button></p><p>未满 14 周岁的读者，请与家长一起决定是否开启统计。不确定时，选择“不参与”即可。</p><h2>网站托管与联系</h2><p>网站由 GitHub Pages 托管。即使不参与 Google Analytics 统计，访问页面时仍需向 GitHub 发送网络请求，相关处理适用<a href="https://docs.github.com/zh/site-policy/privacy-policies/github-general-privacy-statement">GitHub 隐私声明</a>。如对本网站的统计有疑问，可联系作者：<a href="mailto:zchen@uestc.edu.cn">zchen@uestc.edu.cn</a>。</p><p class="privacy-date">更新日期：2026 年 9 月 30 日</p></article></main>'''
(ROOT/'privacy.html').write_text(page('隐私与访问统计｜'+TITLE,'了解本网站如何使用 Google Analytics，以及如何选择或关闭访问统计。','privacy',privacy_body),encoding='utf-8')
urls=[BASE]+[BASE+e['slug']+'.html' for e in entries]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls)+'</urlset>\n')
(ROOT/'404.html').write_text(page('页面未找到｜'+TITLE,'返回图书首页或全书目录。','404','<main id="main" class="wrap error-page"><p class="eyebrow">404</p><h1>这一页暂时找不到了。</h1><p>可以回到首页，继续阅读。</p><a class="button primary" href="'+BASE+'">返回图书首页 →</a></main>'))
print(f'Built {len(entries)+1} pages, sitemap and 404 page.')
