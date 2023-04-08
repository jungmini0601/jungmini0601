import feedparser

somjang_blog_rss_url = "https://jungmini-laboratory.tistory.com/rss"
rss_feed = feedparser.parse(somjang_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """
프로그래밍을 수련하는 김정민입니다. 😁 <br>
가장 좋아하는 말은 **실전 없으면 증명이 없고 증명이 없으면 신용이 없고 신용이 없으면 존경받을 수 없다** 입니다 <br>
자동화 기술, 좋은 성능, 변경 하기 쉬운 코드 작성에 관심이 많고 실험중 입니다. 😍🧪 <br>
🔥몰입력 있는 성격🔥을 가지고 있으며 실력을 올리기 위해서 꾸준히 노력하고 있습니다. <br>

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=jungmini0601&show_icons=true&theme=radical)<br>
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=kJungmin)](https://solved.ac/kJungmin/)<br><br>
<h3>✏️ 최근 블로그 글</h3> 

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
