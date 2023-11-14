import requests
import json


def search(sysdomain, subcate):
    # 存在 XSRF 检查 需要获取cookies等等信息 故使用session
    session = requests.session()
    session.get(f"https://{sysdomain}/off-campus/position-list?lang=zh")
    # 不清楚是否验证cookies所以顺便带上
    XSRF_TOKEN = session.cookies.get("XSRF-TOKEN")
    # pageSize默认10 9999撑开
    RequestJson = '{"channel":"group_official_site","language":"zh","batchId":"","categories":"","deptCodes":[],' \
                  '"key":"",' \
                  '"pageIndex":1,"pageSize":9999,"regions":"","subCategories":"{' + subcate + '}"}'
    Header = {"Content-Type": "application/json"}
    ResultJson = json.loads(
        session.post(f"https://{sysdomain}/position/search?_csrf=" + XSRF_TOKEN, headers=Header,
                     data=RequestJson).text)

    # 提出Datas
    ResultDatas = ResultJson["content"]["datas"]
    for index in range(0, len(ResultDatas)):
        Name = ResultDatas[index]["name"]  # 职务
        Requirement = ResultDatas[index]["requirement"]  # 要求
        Department = ResultDatas[index]["department"]  # 公司
        # PositionUrl = ResultDatas[index]["positionUrl"]  # 详细Post地址
        print(index, Name, Requirement, Department)
        print("\n")


# ALI 所有招聘网同一个系统 为空使用默认参数
domain = {"jobs.cainiao.com": "", "talent.ele.me": "", "talent.amap.com": "",
          "careers.aliyun.com": "133,135,136,137,407,408,409,410,411,511,"
                                "702,703,704,747,764,769,798,811,403,404,"
                                "405,406,108,474,475,476,477,478,479,480,"
                                "481,482,483,484,529,757,758,759,763,834,"
                                "846,847,113,114,115,444,802,446,447,"
                                "448", "talent.taotian.com": "",
          "aidc-jobs.alibaba.com": "", "jobs.alibaba-dme.com": ""}
# v值为筛选参数
for k, v in domain.items():
    search(k, v)
