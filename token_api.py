import requests


def get_arcgis_token_post(username, password, server_url):
    # 构建token请求的URL
    token_url = f"{server_url}/generateToken"

    # 构建token请求的参数
    params = {
        'f': 'json',  # 指定返回数据的格式为JSON
    }

    # 构建token请求的数据，包括用户名和密码
    data = {
        'username': username,
        'password': password,
        'f': 'json',
        'client': 'HTTP referer',
        'referer': '',
        'expiration': 512640
    }

    try:
        # 发送token请求
        response = requests.post(token_url, params=params, data=data)
        response_data = response.json()

        # 提取token
        if 'token' in response_data:
            return response_data['token']
        else:
            print("未能成功获取token。请检查用户名和密码是否正确。")
            return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None


# 替换以下变量值为你的用户名、密码和服务器URL
your_username = 'lvnong'
your_password = 'gongda@888'
your_server_url = "https://gis.airohit.com/arcgis/tokens"
your_referer = "https://agro.airoteach.cn"

# 获取并打印token
token = get_arcgis_token_post(your_username, your_password, your_server_url)
if token:
    print(f"成功获取到token: {token}")
else:
    print("获取token失败。")
