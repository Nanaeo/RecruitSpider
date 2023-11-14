import requests
import json

# 存在 XSRF 检查 需要获取cookies等等信息 故使用session
session = requests.session()
session.get(f"https://talent.cainiao.com/socialList")
RequestJson = '{"pageIndex":1,"pageSize":9999,"regions":"","subCategories":"97,403,404,405,406,112,113,114,115,444,802,' \
              '130,133,135,136,137,407,408,409,410,411,511,702,703,704,747,764,769,798,811","key":""}'
HeaderJson = {"Content-Type": "application/json", "x-xsrf-token": session.cookies.get("XSRF-TOKEN")}
# 社会招聘 校园招聘使用统一系统参考AliSys
ResultJson = json.loads(
    session.post("https://talent.cainiao.com/api/position/search/social", headers=HeaderJson,
                 data=RequestJson).text)
# 提出Datas
ResultDatas = ResultJson["data"]["list"]
for index in range(0, len(ResultDatas)):
    Name = ResultDatas[index]["name"]  # 职务
    Requirement = ResultDatas[index]["requirement"]  # 要求
    Department = ResultDatas[index]["department"]  # 公司
    # PositionUrl = ResultDatas[index]["positionUrl"]  # 详细Post地址
    print(index, Name, Requirement, Department)
    print("\n")
