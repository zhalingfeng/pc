import urllib
import urllib.request
from lxml import etree
import requests


# 请求
def post_task_id():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    url = 'http://www.gdzwfw.gov.cn/portal/api/v2/item-event/getAuditItemDetailCur'
    params = {
        'TASK_CODE': '12440100741854396C3442014055017'
    }
    res = requests.post(url, params=params, headers=headers)
    return res.json()


# 提取事项名称
def get_task_info(res):
    info = res['AUDIT_ITEM']
    data = {
        'matter_name': info['CATANAME'],
        'dept_name': info['DEPT_NAME']
    }
    return data


print(get_task_info(post_task_id()))
