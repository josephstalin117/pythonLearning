import requests
import re
import zhon


def parser_html(html):
    items = re.findall(ur'<p>.*</p>', html.content)
    content = ""
    for i in items:
        print re.sub(ur"[%s]+" % u'\u0020-\u007f\u2000-\u206f\u3000-\u303f\uff00-uffef', "", i.decode("utf-8"))
        content += i.decode('utf-8')[3:-4]
    return content

if __name__ == '__main__':
    text = requests.get('http://china.huanqiu.com/article/2017-08/11108469.html?from=bdwz')
    content = parser_html(text)
    print content
