from .import app
from flask import render_template

import requests

@app.route('/')
@app.route('/index')
def index():
    title = 'Home'
    user = {'username': 'Guanjie'}
    return render_template('index.html', title=title, user=user)


@app.route('/translator')
def translator():
    # 鉴权信息
    api_url = "https://power-api.yingdao.com/oapi/power/v1/rest/flow/3965abc3-1d6a-4e8d-b689-ef94c81ada8e/execute"
    headers = {
        'Authorization': 'Bearer AP_0K3LLi2R25WeoDXQ',
        'Content-Type': 'application/json'
    }

    # 待翻译的文本
    text_2_translated = ("Poetry comes with an exhaustive dependency resolver,"
                         " which will always find a solution if it exists.")

    # 调用影刀 AI Power 的 AI 工作流
    try:
        response = requests.post(api_url, headers=headers, json={"input":{"input_text_0":text_2_translated}})
        return response.json()['data']['result']['output_text_0']
    except Exception as e:
        print(type(e))
        return e
