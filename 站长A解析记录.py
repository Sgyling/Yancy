import json

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def query_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?lang=zh-CN"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.exceptions.RequestException as e:
        print("出现了请求错误:", e)
        return ""
# 创建空列表
data_list = []
while True:
    try:
        # 获取用户输入
        print()
        print(
            '\033[91m' + '* * * * * 杨CC温馨提示您:不需要带HTTP://或HTTPS://只输入域名就可以了呢~ * * * * *\n\b * * * * *注意：如果输入有误会呈现上次的地址,第一次输入有误会报错！！ * * * * *' + '\033[0m')

        key1 = input('请输入要解析的域名(例如：jd.com，q退出): ')
        if key1 != 'q':
            # 构造要发送的数据
            data = {'host': key1, 'ip': '', 'type': 'a'}

            # 发送POST请求
            url = 'https://tool.chinaz.com/nslookup'
            response = requests.post(url, data=data)

            # 获取HTML响应内容
            if response.status_code == 200:
                html_content = response.text

                # 使用BeautifulSoup解析HTML
                soup = BeautifulSoup(html_content, 'html.parser')

                # 提取所有指定数据
                desired_data_list = [element.text for element in soup.find_all('span', attrs={'class': 'mr10'})]

                # 将提取的数据添加到列表中
                data_list.extend(desired_data_list)

                result = []
                outputa = ""
                # 打印提取的数据
                # 打印提取的数据
                for i, data in tqdm(enumerate(desired_data_list), desc='查询进度', total=len(desired_data_list)):
                    outputa += query_ip_info(data)
                    response = requests.get(f"http://ip-api.com/json/{data}?lang=zh-CN")
                    # 检查请求是否成功
                    # response.raise_for_status()
                    # 检查响应状态码
                    if response.status_code == 200:
                        # 请求成功，打印响应内容
                        # print(response.text)
                        json_str = '[' + outputa.replace('}{', '},{') + ']'
                        data = json.loads(json_str)
                        results = []
                        for item in data:
                            result = {
                                'country': item['country'],
                                'regionName': item['regionName'],
                                'city': item['city'],
                                'isp': item['isp'],
                                'query': item['query']
                            }
                            results.append(result)

                # 打印结果
                for result in results:
                    print('----------------')
                    print('IP:', result['query'])
                    print('地址:', result['country'], result['regionName'], result['city'])
                    print('运营商:', result['isp'])
                    print("")

            else:
                print('请求失败:', response.status_code)
                break

        else:
            print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ')
            print('                 _____                    _____          *')
            print('                /\    \                  /\    \         *')
            print('               /::\    \                /::\    \        *')
            print('              /::::\    \              /::::\    \       *')
            print('             /::::::\    \            /::::::\    \      *')
            print('            /:::/\:::\    \          /:::/\:::\    \     *')
            print('           /:::/  \:::\    \        /:::/  \:::\    \    *')
            print('          /:::/    \:::\    \      /:::/    \:::\    \   *')
            print('         /:::/    / \:::\    \    /:::/    / \:::\    \  *')
            print('        /:::/    /   \:::\    \  /:::/    /   \:::\    \ *')
            print('       /:::/____/     \:::\____\/:::/____/     \:::\____\*')
            print('       \:::\    \      \::/    /\:::\    \      \::/    /*')
            print('        \:::\    \      \/____/  \:::\    \      \/____/ *')
            print('         \:::\    \               \:::\    \             *')
            print('          \:::\    \               \:::\    \            *')
            print('           \:::\    \               \:::\    \           *')
            print('            \:::\    \               \:::\    \          *')
            print('             \:::\    \               \:::\    \         *')
            print('              \:::\____\               \:::\____\        *')
            print('               \::/    /                \::/    /        *')
            print('                \/____/                  \/____/         *')
            print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')

            break
    except EOFError as e:
        print("发生了错误，重新输入一下",e)
