import base64
import requests
from Crypto.Cipher import AES as _AES
# 使用前安装依赖
# pip install requests
# pip install  pycryptodome
# 心动网络 貌似与知乎一样的系统 因为我还没断点 就触发了之前的断点 如下json格式
# https://hr.xd.cn/api/outer/ats-jc-apply/website/jobs
# {"limit":15,"offset":0,"zhinengId":"54006","siteId":25045,"orgId":"xd","site":"social","needStat":true}
def aes_decrypt(content: str, key=None, IV=None):
    cipher = _AES.new(key, _AES.MODE_CBC, IV)
    content = base64.b64decode(content)
    return (cipher.decrypt(content).decode('utf-8')).replace('\n', '')


headers = {"content-type": "application/json"}
postData = '{"limit":15,"offset":0,"siteId":3819,"orgId":"zhihu","site":"social","needStat":true}'
retDate = requests.post("https://app.mokahr.com/api/outer/ats-jc-apply/website/jobs", data=postData,
                        headers=headers).json()
base64Data = retDate["data"]
necromancer = retDate["necromancer"]

AES_KEY = necromancer.encode('utf-8')
AES_IV = "de7c21ed8d6f50fe".encode('utf-8')

dec_data = aes_decrypt(base64Data, AES_KEY, AES_IV)
# 128 CBC MODE 
print(dec_data)
#dec_data并不能直接解析json 因为后面存在填充数据 需要先行去掉尾部填充数据
