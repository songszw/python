import urllib.request
import re
import os
import urllib.error

# 创建存放图片目录
path = os.getcwd()
new_path = os.path.join(path, 'ns_vidio')
if not os.path.exists(new_path):
    os.mkdir(new_path)

def open_url(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read()

    return html

def get_p_addrs(url):
    html = open_url(url).decode('utf-8', 'ignore')
    p = r'<div\sclass="threadlist_title pull_left j_th_tit ">\s+<a href="/p/(.*?)" title="'
    page_addrs = re.findall(p, html)

    return page_addrs

def find_img(url):
    html =open_url(url).decode('utf-8', 'ignore')
    q = r'<img class="BDE_Image".*?="([^"]+\.jpg)"'
    img_addrs = re.findall(q, html)
    if img_addrs != []:
        print('此次链接爬取中，共获得%d张图片' % len(img_addrs))
    else:
        print('# -*- 楼主很懒，没有留下任何图片')
    return img_addrs

def find_mp4(url):
    html = open_url(url).decode('utf-8', 'ignore')
    p = r'src="([^"]+\.mp4)"'
    mp4_addrs = re.findall(p, html)
    if mp4_addrs != []:
        print('此次链接爬取中，共获得%d个视频' % len(mp4_addrs))
    else:
        print('# -*- 楼主很懒，没有留下任何视频')
    return mp4_addrs

def save_img(img_addrs):
    os.chdir(new_path)
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb')as f:
            img = open_url(each)
            f.write(img)

def save_mp4(mp4_addrs):
    os.chdir(new_path)
    for each in mp4_addrs:
        filename = each.split('/')[-1]
        urllib.request.urlretrieve(each, filename)

x = 1 #定义了一个全局变量

def downloading(pages):
    url = 'http://tieba.baidu.com/f?kw=%E5%A5%B3%E7%A5%9E&ie=utf-8'
    for i in range(int(pages)):
        try:
            page_url = url + '&amp;pn=' + str(i * 50)
            page_addrs = get_p_addrs(page_url)
            print('# -*- ------正在爬取第%d页，获得共%d个链接------ -*- #' % (i+1, len(page_addrs)))
            for each in page_addrs:
                new_page_url = 'http://tieba.baidu.com/p/' + each + '?see_lz=1'
                global x # 通过global方法，引入全局变量
                print('# -*- ------正在爬取第%d个链接------ -*- #' % x)
                print(new_page_url)
                x += 1
                img_addrs = find_img(new_page_url)
                save_img(img_addrs)
                mp4_addrs = find_mp4(new_page_url)
                save_mp4(mp4_addrs)
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print(e.code)
                continue
            elif hasattr(e, 'reason'):
                print(e.reason)
                continue
            print('出现异常跳到下一页！！')

if __name__ == '__main__':
    pages = input('请输入最大页码：')
    downloading(pages)
