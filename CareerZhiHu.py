import base64
import requests
from Crypto.Cipher import AES as _AES


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
