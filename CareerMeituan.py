import requests
import json

# pageSize默认为10 这里填 9999 
MainUrl = "https://zhaopin.meituan.com/api/official/job/getJobList"
postData = '{"page":{"pageNo":1,"pageSize":9999},"jobShareType":"1","keywords":""}'
headers = {"content-type": "application/json"}
# 直接json解析
ResultJSON = json.loads(requests.post(MainUrl, data=postData,headers=headers).text)
# 提出Posts
ResultPosts = ResultJSON["data"]["list"]
for index in range(0, len(ResultPosts)):
    RecruitPostName = ResultPosts[index]["name"]  # 职位
    Responsibility = ResultPosts[index]["jobDuty"]  # 能力
    highLight = ResultPosts[index]["highLight"]  # 工作经验需求
    # department = ResultPosts[index]["department"][0]["name"]  # 有的没写
    print(index, RecruitPostName, Responsibility, highLight, )
