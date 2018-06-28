import requests
headers = {
    'Cookies':'q_c1=b9e402f1a2614f4987cf4bdf7940b3be|1503537982000|1503537982000; _zap=ce0547a8-e513-4534-90d7-9e5ce69b6d0c; __guid=74140564.873205477658558600.1509502889465.1755; d_c0="ACBCBGzipwyPTpZSWC8YVZ3sma1fcfBqQj4=|1510204965"; z_c0=Mi4xZUtDLUJBQUFBQUFBSUVJRWJPS25EQmNBQUFCaEFsVk5mSFljV3dCeUppMUtmQUx2SkxDak1vdjAwazU2ODJvTllB|1513039996|3eb8368303c2635f5a66b6fbc07a671bc65c6e8b; __DAYU_PP=IBIBUf6qmFYyyjmVuEav282ec7663595; q_c1=b9e402f1a2614f4987cf4bdf7940b3be|1525333729000|1503537982000; _xsrf=7246d9c3129e8288cc3581634305946f; __utma=51854390.1061674988.1526536181.1526536181.1526541799.2; __utmz=51854390.1526541799.2.2.utmcsr=germey.gitbooks.io|utmccn=(referral)|utmcmd=referral|utmcct=/python3webspider/content/3.2.1-%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8.html; __utmv=51854390.100--|2=registration_date=20170420=1^3=entry_date=20170420=1; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8; monitor_count=21'
    ,'Host':'www.zhihu.com'
    ,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)

print('-------------------------------------')
# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)

s = requests.Session()
s.get('https://www.baidu.com/cookies/set/phone/15711184303')
response = s.get('https://www.baidu.com/cookies')
print(response.text)