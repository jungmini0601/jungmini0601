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

이를 위해 위클리 아카데미라는 기술공유 커뮤니티에서  활동하며 의견을 교류하고 있습니다.

일을 시작할 때부터 모든 것이 순조롭게 이루어지는 일은 드물다고 생각합니다. 

그래서, **일하는 방식에 대한 피드백을 수시로 받아들이고 빠르게 발전하려고 노력**합니다. 

**경험과 이론을 통한 성장을 지향**합니다.

제가 지향하는 목표는 함께 일할 때 **즐거우며 신뢰받는 사람이 되는 것**입니다.

저와 나누고 싶으신 대화가 있으시다면 언제든지 메일주세요! 감사합니다.


![](https://github-profile-trophy.vercel.app/?username=jungmini0601&theme=flat&no-frame=true&margin-w=30)

<h3>  👨‍👨‍👦‍👦 커뮤니티 <h3>

[위클리 아카데미](https://www.weekly.ac/) <br>
[saramdle](https://discord.gg/aupDwXxfnc) <br>
[Eric](https://discord.com/invite/7qNA6tG) <br>

<h3>✏️ 최근 블로그 글</h3> 

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
