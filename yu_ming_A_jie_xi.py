import urllib.parse
import json
import requests

def query_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?lang=zh-CN"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.exceptions.RequestException as e:
        print("出现了请求错误:", e)
        return ""

def get_domain_info(domain):

    try:
        params = urllib.parse.urlencode({'key': 'bff0f426d5d50e886b5462ca17317736', 'domain': domain})
        headers = {'Content-type': 'application/x-www-form-urlencoded'}

        response = requests.post('https://apis.tianapi.com/domain/index?', params=params, headers=headers)
        if response.status_code == 200:
            dict_data = response.json()

            zhuangtai_ma = str(dict_data['code'])
            print("状态码=" + zhuangtai_ma)

            if zhuangtai_ma == "200":
                print("\n------------------------------\n我有一只小毛驴我从来也不骑\n------------------------------\n")

                if 'result' in dict_data and 'list' in dict_data['result']:
                    data = dict_data['result']['list']
                    result = []
                    outputa = ""

                    for i in data:
                        if i['type'] == 'A':
                            ip = i['ip']
                            result.append(f"type:{i['type']}, ip:{ip}")
                            outputa += query_ip_info(ip)

                            # print(outputa,'\n')
                            response = requests.get(f"http://ip-api.com/json/{ip}?lang=zh-CN")

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
                                'query':item['query']
                            }
                            results.append(result)

                        # 打印结果
                        for result in results:
                            print('----------------')
                            print('IP:',result['query'])
                            print('地址:', result['country'],result['regionName'],result['city'])
                            print('运营商:', result['isp'])
                            print()
                        # print(response1)
                    else:
                        # 请求失败，打印错误信息
                        print("Request failed with status code:", response.status_code)
                    if result:
                        print("完成\n\n")
                        # chaxun = []
                        # for line in outputa.splitlines():
                        #     ip_info = json.loads(line)
                        #     print(ip_info)
                        #
                        #     country = ip_info.get('country', '')
                        #     regionName = outputa.get('regionName', '')
                        #     city = outputa.get('city', '')
                        #     isp = outputa.get('isp', '')
                        #     print(country)
                        # chaxun.append(f"A地址IP: {ip} \n地址：{country('country', '')} {regionName} {city} \n运营商: {isp} ")
                        # print()
                        #
                        # if chaxun:
                        #     print(chaxun)


                    else:
                        print("没有相关A解析地址")
                else:
                    print("无法解析域名")
                    print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
                    print('*                                                         *')
                    print('*                                                         *')
                    print('*     注意 ：                                              *')
                    print('*                不可以带HTTP或HTTPS                        *')
                    print('*                                        只输域名就可以了    *')
                    print('*                                                         *')
                    print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
            else:
                print("无法解析")
                print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
                print('*                                                         *')
                print('*                                                         *')
                print('*     注意 ：                                              *')
                print('*                不可以带HTTP或HTTPS                        *')
                print('*                                        只输域名就可以了    *')
                print('*                                                         *')
                print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
        else:
            print("请求失败:", response.status_code, response.reason)
            print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
            print('*                                                         *')
            print('*                                                         *')
            print('*     注意 ：                                              *')
            print('*                不可以带HTTP或HTTPS                        *')
            print('*                                        只输域名就可以了    *')
            print('*                                                         *')
            print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    except requests.exceptions.RequestException as e:
        print("发生了网络错误:", e)
        print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
        print('*                                                         *')
        print('*                                                         *')
        print('*     注意 ：                                              *')
        print('*                不可以带HTTP或HTTPS                        *')
        print('*                                        只输域名就可以了    *')
        print('*                                                         *')
        print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    except json.JSONDecodeError as e:
        print("解析响应数据失败:", e)
        print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
        print('*                                                         *')
        print('*                                                         *')
        print('*     注意 ：                                              *')
        print('*                不可以带HTTP或HTTPS                        *')
        print('*                                        只输域名就可以了    *')
        print('*                                                         *')
        print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
    except Exception as e:
        print("发生了错误:", e)
        print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
        print('*     注意 ：                                              *')
        print('*                不可以带HTTP或HTTPS                        *')
        print('*                                        只输域名就可以了    *')
        print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')

# Example usage
while True:


    domain = input("请输入域名（例如，tianapi.com），或者输入 q 退出：")
    if domain.lower() == "q":
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


    get_domain_info(domain)
