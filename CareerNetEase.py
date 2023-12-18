import requests

session = requests.Session()
headersData = {"content-type": "application/json;charset=UTF-8"}
# pageSize为数据量
retData = session.post("https://hr.163.com/api/hr163/position/queryPage", data='{"currentPage":1,"pageSize":9999}',headers=headersData).text
print(retData)
