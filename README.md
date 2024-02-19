# UAD
  用于快速检测Url是否存活的小工具
## 功能如下
```
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
```
- 批量检测url
```
python url_active_detect.py -u urls.txt  
```
![image](https://github.com/muyugit/UAD/assets/108386999/25d19a9d-3847-49ce-8e4c-803de4a3b61c)

- 指定显示某个状态码的url
```
python url_active_detect.py -u urls.txt -sc 200
```
![image](https://github.com/muyugit/UAD/assets/108386999/804e0f34-4c48-4b87-989b-a454a81f9c82)

- 排除包含某个关键字
```
python url_active_detect.py -u urls.txt -ex baidu
```
![image](https://github.com/muyugit/UAD/assets/108386999/686bbd83-bca1-4f92-8969-6b9f12358326)
- 排除一定大小的响应页面
```
python url_active_detect.py -u urls.txt -es 0
```
![image](https://github.com/muyugit/UAD/assets/108386999/bfb70c2e-2c88-441d-aaba-8f6ecf512528)
- 使用浏览器打开状态码为200的url

```
 python url_active_detect.py -u urls.txt -ob 200
```
![image](https://github.com/muyugit/UAD/assets/108386999/b94e152c-494c-43e5-9acd-b5aaf796c3d7)

- 将结果保存到文件
```
python url_active_detect.py -u urls.txt -sc 200 -o res.csv
```
![image](https://github.com/muyugit/UAD/assets/108386999/e3e65219-498d-4718-8085-bad3ab2a1db1)

![image](https://github.com/muyugit/UAD/assets/108386999/ed75dcf0-6fee-4edb-b5ff-ebd11ea42f5a)

