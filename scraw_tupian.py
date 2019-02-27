#!/usr/local/bin/python3
#coding:utf-8
# @Time    : 2019/1/24 14:20
# @Author  : 潘劲
# @FileName: scraw_tupian.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests
import os

# url='http://699pic.com/sousuo-218808-13-1.html'
# def get_page(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#     }
#     html = requests.get(url, headers,verify=False)
#     return html.content
#
# def parse_page(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     images = soup.find_all(class_="lazy")
#
# def download_img():
# 	base_url = 'http://699pic.com/sousuo-218808-13-{}.html'
# 	_img = output(base_url.format(num)
#     for i in images:
#         try:
#         jpg_url=i["data-original"]#获取图片地址
#         title=i["title"]#获取图片名称
#         print(title)
#         print(jpg_url)
#         print("")
#         #保存图片
#         with open(os.getcwd()+"\\jpg\\"+title+'.jpg', "wb") as f:
#             f.write(requests.get(jpg_url).content)
#     except:
#         pass
#
#
# def main(url):
#     for i in range(14):
#         urls = url +str(i)
#         print(urls)
#         html = get_page(urls)
#         parse_page(html)
#
#
#
#
# if __name__ == '__main__':
#     main()
#



r= requests.get("http://699pic.com/sousuo-218808-13-1.html")
tupian=r.content
soup = BeautifulSoup(tupian,"html.parser")
#找出所有的标签
images = soup.find_all(class_="lazy")
# print(images)#返回list
for i in images:
    try:
        jpg_url=i["data-original"]#获取图片地址
        title=i["title"]#获取图片名称
        print(title)
        print(jpg_url)
        print("")
        #保存图片
        with open(os.getcwd()+"\\jpg\\"+title+'.jpg', "wb") as f:
            f.write(requests.get(jpg_url).content)
    except:
        pass




