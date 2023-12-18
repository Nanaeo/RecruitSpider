import requests

session = requests.Session()
csrf = session.post(f"https://jobs.bytedance.com/api/v1/csrf/token").json()["data"]["token"]
print(csrf)
headersArray = {"x-csrf-token": csrf}
# limit为数目 适当调大
postData = '{"keyword":"","limit":999,"offset":0,"job_category_id_list":[],"tag_id_list":[],"location_code_list":[],"subject_id_list":[],"recruitment_id_list":[],"portal_type":2,"job_function_id_list":[],"portal_entrance":1}'
retData = session.post("https://jobs.bytedance.com/api/v1/search/job/posts",data=postData,headers=headersArray).text
print(retData)
# 数据未处理
