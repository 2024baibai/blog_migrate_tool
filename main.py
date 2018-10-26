#-*- coding=utf-8 -*-
import requests
import re
from dateutil.parser import parse
from config import *
from wp_method import *

wp = WPDB(site=SITE, user=SITE_USER, passwd=SITE_PASSWD)
# wp.create_post(title='测试',content='ojbk',tag=['test','ojbk'],category=['test'],thumnnail_path='https://farm4.staticflickr.com/3701/11891185725_f79a9ae876_b.jpg')

class GP():
    def __init__(self,page_url):
        self.xml_url=page_url+'/sitemal.xml'

    def main(self):
        r=requests.get(self.xml_url)
        cont=r.text
        posts=re.findall('<loc>(.*?)</loc>[\w\W]*?<lastmod>(.*?)</lastmod>',cont)
        for url,post_time in posts:
            info=self.GetPostInfo(url)
            title=info['title']
            context=info['context']
            cate=info['cate']
            time=self.transform_date(post_time)
            print(u'publish new posts:{}'.format(title))
            wp.create_post(title=title,content=context,post_format='0',category=cate)
            pid=wp.GetIdByTitle(title)
            if pid:
                wp.AlterTime(pid,time)

    def GetPostInfo(self,url):
        r=requests.get(url)
        cont=r.text
        context=re.findall('<article class="article-content markdown-body">([\w\W]*?)</article>',cont)[0]
        title=re.findall('<h1 class="collection-header">(.*?)</h1>',cont)[0]
        cate=re.findall('<a href="http.*?/categories/#(.*?)"',cont)
        cate=re.findall('<a href="http.*?/categories/#(.*?)"',cont)
        return dict(title=title,context=context,cate=cate)

    def transform_date(self,t):
        date=parse(t)
        return date.strftime('%Y-%m-%d %H:%M:%S')


if __name__=='__main__':
    g=GP()
    g.main()
