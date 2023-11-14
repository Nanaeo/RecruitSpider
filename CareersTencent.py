import requests
import json

# 参数详情 请参考页面 https://careers.tencent.com/search.html
# pageSize默认为10 这里填 9999 以便单APi输出全部 categoryId为筛选类型
MainUrl = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1699923962889&countryId=&cityId=&bgIds" \
          "=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006,40002001,40002002,40003001," \
          "40003002,40003003,40004,40005001,40005002,40006,40007,40008,40009,40010,40011&parentCategoryId=&attrId=1," \
          "2,3,5&keyword=&pageIndex=1&pageSize=9999&language=zh-cn&area=cn"
# 直接json解析
ResultJSON = json.loads(requests.get(MainUrl).text)
# 提出Posts
ResultPosts = ResultJSON["Data"]["Posts"]
for index in range(0, int(ResultJSON["Data"]["Count"]) - 1):
    RecruitPostName = ResultPosts[index]["RecruitPostName"]  # 职位
    Responsibility = ResultPosts[index]["Responsibility"]  # 能力
    RequireWorkYearsName = ResultPosts[index]["RequireWorkYearsName"]  # 工作经验需求
    CountryName = ResultPosts[index]["CountryName"]  # 国家
    LocationName = ResultPosts[index]["LocationName"]  # 地域
    LastUpdateTime = ResultPosts[index]["LocationName"]  # 招聘更新时间
    PostURL = ResultPosts[index]["PostURL"]  # 招聘详情地址
    # 数据未入库
    print(index, RecruitPostName, Responsibility, RequireWorkYearsName, CountryName, LocationName, LastUpdateTime,
          PostURL)
