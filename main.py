import feedparser

somjang_blog_rss_url = "https://jungmini-laboratory.tistory.com/rss"
rss_feed = feedparser.parse(somjang_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """
<h1>🙋자기소개!</h1>

제가 가진 시각과 방법론 뿐만 아니라, **다른 분들이 가지고 있는 경험과 지식도 적극 수용하며 항상 배우고자 노력 합니다.**

**경험과 이론, 피드백을 통한 성장을 지향**합니다.

제가 가진 기술과 지식을 통해 주변에 도움을 주는 것을 좋아합니다.

제가 지향하는 목표는 함께 일할 때 **즐거우며 신뢰받는 사람이 되는 것**입니다.

![](https://github-profile-trophy.vercel.app/?username=jungmini0601&theme=flat&no-frame=true&margin-w=30)

<h3>  👨‍👨‍👦‍👦 커뮤니티 & 📚 Study<h3>

[위클리 아카데미](https://www.weekly.ac/) <br>
[소시민 스터디](https://oval-licorice-979.notion.site/4fc65451bf244a138a93f930ecaaee38?v=8ec49eefb77f44f5a5faef7b15213ac0) <br>

<h3>✏️ 최근 블로그 글</h3> 

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
