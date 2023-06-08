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

이것 저것 다양한 프로그램 만드는 것을 좋아합니다.

가장 존경하는 인물은 최배달 선생님입니다.

가장 좋아하는 말은 실전이 없으면 증명이 없고, 증명이 없으면 신용이 없고, 신용이 없으면 존경받을 수 없다입니다.

기본기를 가장 중요시하며, 최근에는 다양한 데이터 처리 기법에 대해서 학습 하고있습니다!

![](https://github-profile-trophy.vercel.app/?username=jungmini0601&theme=flat&no-frame=true&margin-w=30)

![Leetcode Stats](https://leetcard.jacoblin.cool/jungmini0601)

<h3>  👨‍👨‍👦‍👦 커뮤니티 & 📚 Study<h3>

[위클리 아카데미](https://www.weekly.ac/) <br>
[소시민 스터디](https://oval-licorice-979.notion.site/4fc65451bf244a138a93f930ecaaee38?v=8ec49eefb77f44f5a5faef7b15213ac0) <br>

<h3>✏️ 최근 블로그 글</h3> 

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
