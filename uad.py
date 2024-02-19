import requests
import random
import webbrowser
import argparse
import threading
from queue import Queue
import sys
import csv
import colorama

colorama.init(autoreset=True)
class uad(object):
    def __init__(self,filename,status_code,open_browser,th,savename,ex,es,co):
        ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.100.0"]
        self.headers = {
            'User-Agent':  random.choice(ua)
        }
        self.th=th
        self.filename= filename
        self.savename=savename
        self.status_code=status_code
        self.open_browser=open_browser
        self.res = []
    def open_url(self,q):
        while not q.empty():
            url= q.get()
            try:
                if url.find("https") == -1:
                    r = requests.get(url, allow_redirects=False, timeout=4, headers=self.headers, verify=False)
                else:
                    r = requests.get(url, allow_redirects=False, timeout=4, headers=self.headers, verify=True)
                self.output_res([url,r.status_code,r.text,len(r.text)])

            except Exception as e:
                # print(e)
                self.output_res([url,"无法访问",r.text,len(r.text)])
                self.res.append([url,"无法访问"])
                pass
    def output_res(self,line):
        if (ex is None and co is None and es is None) or (ex != None and ex not in line[2]) or (co != None and co in line[2]) or (es != None and es != str(line[3]) ):
            if self.status_code == None:
                if line[1] == 200 or line[1] == 301 or line[1] == 302:
                    print(colorama.Fore.GREEN + f"[+] {line[0]} {line[1]} {line[3]} \n")
                else:
                    print(f"[-] {line[0]} {line[1]} {line[3]}\n")
            elif str(line[1]) in self.status_code:
                print(f"[+] {line[0]} {line[1]} {line[3]}\n")
            if self.open_browser != None and str(line[1]) in self.open_browser:
                webbrowser.open(line[0])
            self.res.append([line[0],line[1]])
    def check_url(self):
        threads = []
        workQueue = Queue(1000)
        with open(self.filename ,"r",encoding="utf-8") as f:
            for line in f:
                workQueue.put(line.strip())
        for tname in range(self.th):
            thread = threading.Thread(target=self.open_url, name=str(tname), args=(workQueue,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
    def output_csv(self):
        title=["url","status_code"]
        with open(self.savename, "w", encoding='utf-8-sig', newline="") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=",")
            csvwriter.writerow(title)
            csvwriter.writerows(self.res)

        print("结果保存到 %s" %self.savename)
def arguments():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=f"***用于批量检测url是否存活***",
        epilog=f"示例:"
               
        f"\n\tpython {sys.argv[0]} -u urls.txt "
        f"\n\tpython {sys.argv[0]} -u urls.txt -sc 200,301"
        f"\n\tpython {sys.argv[0]} -u urls.txt -o res.csv"
        f"\n\tpython {sys.argv[0]} -u urls.txt -ob 200,302"
        f"\n\t"
    )
    parser.add_argument("-u", "--urls",help="存有url的文件")
    parser.add_argument("-sc", "--status_code",help="过滤状态码")
    parser.add_argument("-ob", "--open_browser",help="使用浏览器打开指定状态码的链接")
    parser.add_argument("-th", "--threads",help="设置线程数",default=15)
    parser.add_argument("-o", "--output",help="保存结果")
    parser.add_argument("-ex", "--Excluded",help="排除包含关键字的页面")
    parser.add_argument("-es", "--Excludedsize",help="排除一定大小的页面")
    parser.add_argument("-co", "--contain",help="显示包含关键字的页面")

    arguments.option = parser.parse_args()

if __name__ == '__main__':
    log='''
         _   _    _   _  _    
        | | | | / \  |  _ \ 
        | | | |/ _ \ | | | |
        | |_| / ___ \| |_| |
         \___/_/   \_\____/  v1.3
    '''
    print(colorama.Fore.GREEN+log)
    arguments()
    filename = arguments.option.urls
    status_code = arguments.option.status_code
    open_browser = arguments.option.open_browser
    savename = arguments.option.output
    th = arguments.option.threads
    ex = arguments.option.Excluded
    es = arguments.option.Excludedsize
    co = arguments.option.contain

    myuad = uad(filename,status_code,open_browser,th,savename,ex,es,co)
    myuad.check_url()
    if savename != None:
        myuad.output_csv()