import json
import requests


def baiduSearch(page):
    retData = requests.post(
        "https://talent.baidu.com/httservice/getPostListNew?recruitType=SOCIAL&pageSize=20&keyWord=&curPage=" + str(
            page) + "&projectType=",
        headers={"Referer": "https://talent.baidu.com/jobs/social-list"})
    return retData.text


ResultJson = json.loads(baiduSearch(1))
# 初次请求
total = int(ResultJson["data"]["total"])
NeedIndex = int((total - total % 20) / 20 + 1)
# 计算翻页数

for PageIndex in range(1, NeedIndex):
    ResultJson = json.loads(baiduSearch(PageIndex))
    PageData = ResultJson["data"]["list"]
    for DataIndex in range(0, 19):
        Name = PageData[DataIndex]["name"]  # 职位名
        ServiceCondition = PageData[DataIndex]["serviceCondition"]  # 职位条件
        WorkContent = PageData[DataIndex]["workContent"]  # 工作内容
        PostType = PageData[DataIndex]["postType"]  # 工作内容
        print(Name, ServiceCondition, WorkContent, PostType)
