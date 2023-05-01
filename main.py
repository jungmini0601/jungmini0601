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
안녕하세요 주니어 백엔드 엔지니어 김정민입니다. 😁 <br>
다양한 의견속에서 배우는 것을 좋아하며 가능한 많은의견을 참고하기 위해 기술공유 커뮤니티에서 적극 활동하고 있습니다.<br>
처음부터 잘 되는 일은 없다고 생각하며 빠르게 발전하기 위해서 주변에 피드백을 요청드리는 것을 좋아합니다. <br>
경험을 통해 성장하는 방식을 지향하며 그와 동시에 이론적 성숙함을 챙기기 위해 꾸준히 독서를 하고 있습니다. <br>
가장 좋아하는 말은 **실전이 없으면 증명이 없고 증명이 없으면 신용이 없고 신용이 없으면 존경받을 수 없다**. 입니다. <br>
주변 사람들로부터 신뢰받는 것을 좋아하며 함께 했을 때 즐거웠던 사람으로 남고 싶습니다. <br>
저와 나누고 싶으신 이야기가 있으시다면 언제든지 편하게 메일 주셔요 감사합니다.<br>

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=jungmini0601&show_icons=true&theme=radical)<br>
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=kJungmin)](https://solved.ac/kJungmin/)<br><br>

<h3> 커뮤니티 <h3>

[위클리 아카데미](https://www.weekly.ac/) <br>
[saramdle](https://discord.gg/aupDwXxfnc) <br>
[Eric](https://discord.com/invite/7qNA6tG) <br>

<h3>✏️ 최근 블로그 글</h3> 

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
