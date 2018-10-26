# 博客迁移到wordpress工具

Abbey最近想要将博客迁移到wordpress，但是网上找了一圈，都没有找到github pages迁移到wordpress的工具，搜出来的都是wordpress迁移到github pages的文章！

现在wordpress那么不受待见了吗？

Anyway，既然找不到工具，那只能自己写脚本来迁移啦！

-----------
## 迁移前提&说明：
1. 你的github pages有**开启sitemap功能**！
2. 可以**远程连接到你的wordpress数据库**！
3. 因为每个人的github pages模板都不一样，因此拿到本脚本需要自己手动修改`main.py`的`GetPostInfo`方法，**修改正则表达式提取内容、标题、分类**等

## 迁移教程：
1. 安装依赖
```
pip install -r requirements.txt
```
2. 修改配置
修改`config.py`的配置内容：
    - ####wordpress相关设置
        - WP_HOST ：wordpress数据库ip
        - WP_PORT ：MySQL端口，默认3306
        - WP_USER ：wordpress数据库用户名
        - WP_PASSWD：wordpress数据库密码
        - WP_DB：wordpress数据库
        - SITE：wordpress网站地址
        - SITE_USER：wordpress网站管理员用户名
        - SITE_PASSWD：wordpress网站管理员密码

    - ####github pages相关设置
        - github_pages_url：老博客网址

3. 运行：
```
python main.py
```

运行效果图：

![](http://wx4.sinaimg.cn/large/0060lm7Tly1fwltqq2w23j30i80drgnj.jpg)
