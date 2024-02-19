# UAD
  用于快速检测Url是否存活的小工具
## 功能如下

  -u URLS, --urls URLS  存有url的文件
  -sc STATUS_CODE, --status_code STATUS_CODE
                        过滤状态码
  -ob OPEN_BROWSER, --open_browser OPEN_BROWSER
                        使用浏览器打开指定状态码的链接
  -th THREADS, --threads THREADS
                        设置线程数
  -o OUTPUT, --output OUTPUT
                        保存结果
  -ex EXCLUDED, --Excluded EXCLUDED
                        排除包含关键字的页面
  -es EXCLUDEDSIZE, --Excludedsize EXCLUDEDSIZE
                        排除一定大小的页面
  -co CONTAIN, --contain CONTAIN
                        显示包含关键字的页面

示例:
        python .\url_active_detect.py -u urls.txt
        python .\url_active_detect.py -u urls.txt -sc 200,301
        python .\url_active_detect.py -u urls.txt -o res.csv
        python .\url_active_detect.py -u urls.txt -ob 200,302
###批量检测url
        
![image](https://github.com/muyugit/UAD/assets/108386999/25d19a9d-3847-49ce-8e4c-803de4a3b61c)


