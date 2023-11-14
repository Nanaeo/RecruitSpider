import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


def search_baidu(page):
    InJs = 'return await (await fetch("https://talent.baidu.com/httservice/getPostListNew", {"headers": {"accept": ' \
           '"application/json, text/plain, */*","accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",' \
           '"content-type": "application/x-www-form-urlencoded;charset=UTF-8",},"body": ' \
           '"recruitType=SOCIAL&pageSize=20&keyWord=&curPage=' + str(page) + '&projectType=","method": "POST",' \
                                                                        '"credentials": ' \
                                                                        '"include"})).text();'
    RetJs = driver.execute_script(InJs)
    return RetJs


# 百度存在Cookie验证 懒得分析
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://talent.baidu.com/jobs/social-list?search=")
# 等待页面加载
sleep(5)
# 执行JS请求
ResultJson = json.loads(search_baidu(1))
total = int(ResultJson["data"]["total"])
NeedIndex = int((total - total % 20) / 20 + 1)
for PageIndex in range(1, NeedIndex):
    ResultJson = json.loads(search_baidu(PageIndex))
    PageData = ResultJson["data"]["list"]
    for DataIndex in range(0, 19):
        Name = PageData[DataIndex]["name"]  # 职位名
        ServiceCondition = PageData[DataIndex]["serviceCondition"]  # 职位条件
        WorkContent = PageData[DataIndex]["workContent"]  # 工作内容
        PostType = PageData[DataIndex]["postType"]  # 工作内容
        print(Name, ServiceCondition, WorkContent, PostType)
sleep(20)
