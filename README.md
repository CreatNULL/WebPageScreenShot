# Python实现的访问网页截图


## 等待解决的问题（未解决）


## 最新版本:
2026.02.05._WebPageScreenShot.tar.gz 最新版本<br />
https://github.com/CreatNULL/WebPageScreenShot/releases/download/v1.0/2026.02.05._WebPageScreenShot.tar.gz

## 一、这是什么
一个访问网页，并且截图的工具.实现快速访问，批量截图，以前当毕设的，现在突然想要批量访问url，看看截图，当初给写烂尾了，现在修修补补一下。
<br/>
<br/>
```
- 支持 POST （JSON、data、file）
- 支持 GET (json、data、file)
- 要手动指定 POST，不然默认就是 GET，不管是否使用了 --data   --json --files
- 默认情况下，程序使用 9222 端口，浏览器可执行文件路径为'chrome'。
  - 参考 DrissionPage 第三方库官方文档: https://drissionpage.cn/browser_control/connect_browser
- Ctrl + C 可以结束进程，理论上，不会有残留的进程，除非强行关闭。但是如果访问的url很多，可能结束很慢，等不及的自己手动结束进程吧，或者尝试使用参数 --force-stop-browser 或者 Windows下使用 taskkill /IM chrome.exe /F,嘿嘿
- 指纹识别使用的是 https://github.com/EdgeSecurityTeam/EHole 的指纹库，也是把它的指纹识别模块搞成dll 和 .so
- 结果输出
  - 输出文件
     (1). 一个访问成功的文件列表 success_url.txt ，提供给下一步访问等;
     (2). 访问失败文件 error_url.txt ，记录访问失败，如果是应为超时的原因可以重设超时时间，再次运行。
     (3). 运行日志，记录运行流程，方便出问题追踪。不需要则使用 --no-log 参数
     (4). 一个指定代理时或指定 headers 时创建的代理插件目录，ScreenShot_Extensions，--del-extensions 会删除所有的插件文件和这个目录及本身
     (5). 一个 result.html 记录访问成功的图片和网站，
     (6)、如果使用配置文件 --config , 首次指定会创建你指定的名称的，默认的配置文件）
     (7)、用户目录 ScreenShot_User_Data  退出后删除 --del-user-data 参数
- 可以通过指定读取配置文件，创建和使用配置文件是同一个命令 --config 配置文件名称，
- 如果输出文件的太大使用 --split 参数，或启动时候指定这个，100个 url一划分。

```
![image](https://github.com/user-attachments/assets/707d22e6-000b-4e42-8d52-caed2be1ee94)<br/>


## 下个版本目标：
对yakit 导出的 .har 网络包解析，然后去请求截图？

## 说明
DrissionPage 这个库分为两种访问模式：d 模式用于控制浏览器，s 模式使用requests收发数据包 (https://drissionpage.cn/browser_control/mode_change/#%EF%B8%8F-mode), <br />
我个人觉的，可以粗略的认为，一个类似用chromedriver 控制访问，一个用 requests 去访问。<br/>
**<span style="color:red">注意:</span>**<br/>
>     headers/params/data/json/file/cookies/allow_redicts 参数在 s 模式下才会生效，(headers 除外，因为我用插件实现了修改 headers ，所以当 指定了 headrs 的时候，默认不会切换到 s 模式)
>     所以当出现这些参数的时候，可以粗略的认为，切换到了requests 去请求，
>     官方文档内写着: https://drissionpage.cn/SessionPage/visit
>     所以，我设置了如果携带这些参数的时候，指定的多个证书，只会读取第一个，这样你只能指定的格式为pem啦，哈哈
![image](https://github.com/user-attachments/assets/469fc0b6-55f0-4403-8fb0-bdca3221bcdc)
>     参考官方文档: https://drissionpage.cn/SessionPage/visit/#%EF%B8%8F%EF%B8%8F-post

<br/>
<br/>

### (一)、基本使用
```
python .\webPageScreenshot.py --url http://www.taobao.com 
```
<br/>
<br/>

##### 程序运行后：
- 会创建目录: `ScreenShot_User_Data_Extensions` 、 `ScreenShot_User_Log`和 `ScreenShot_User_Data` ,分别保存设置代理时创建的插件，程序运行的日志 和 浏览器用户文件夹 (为什么文件名这么长? 我不是有病哦，怕有和其它的冲突)
- 无头模式运行
- 一个输出文件名为 result.html ((●'◡'●)这里我懒啦)，URL给的不要太多哦，不然html文件输出会很大，不过也不要紧，我写了切割文件的。。
<br/>
<br/>

##### 运行终端显示:
![image](https://github.com/user-attachments/assets/0df0a373-0170-4cb9-8640-14b66a7ed535)
<br/>
<br/>

##### 输出文件:
会自动统计当前的数量<br/>
![image](https://github.com/user-attachments/assets/bf315448-db76-4e62-aebd-19bd1897923a)<br/>
打开后会显示网站标题和缩略图<br/>
![image](https://github.com/user-attachments/assets/7a27896b-2c8e-4f7e-96d6-c698598b4a54)<br/>
鼠标移动到缩略图后，图片会放大显示，方便快速浏览<br/>
![image](https://github.com/user-attachments/assets/632047ee-ed4d-4205-834a-b5f901414b71)<br/>
点击标题后，详细信息展开<br/>
![image](https://github.com/user-attachments/assets/9c1add3c-0b47-4452-88e8-249ac618d0ba) <br/>
![image](https://github.com/user-attachments/assets/04ce64b7-446c-44a4-8e7f-8cbaa967cfe3) </br>
<br/>
<br/>
##### 使用配置文件
```
python .\webPageScreenshot.py --config .\config.ini
```
![image](https://github.com/user-attachments/assets/3b4fdecf-09e7-4d69-bd6e-86fcb0c20700)<br/>


#### 访问多个URL 
```
python .\webPageScreenshot.py --url http://www.taobao.com --url https://hk.jd.com/ --url https://www.baidu.com 
```
![image](https://github.com/user-attachments/assets/5f75b66f-e731-48c0-a04b-1bcb14d46086)<br/>
##### 使用配置文件
使用, 分割 或 使用 [] 表示<br/>
![image](https://github.com/user-attachments/assets/c6b649aa-74b3-416d-b3c6-d89b9649c996)<br/>
![image](https://github.com/user-attachments/assets/c5f5a1e5-e10a-416a-8b04-67e93516717e)<br/>
![image](https://github.com/user-attachments/assets/16059bb2-732e-4deb-9d4a-aa015b26b2f6)<br/>
<br/>
<br/>

### (二)、使用代理
#### 代理抓包软件
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://127.0.0.1:8083
```
![image](https://github.com/user-attachments/assets/656d0d42-1ebb-40fc-aaca-e8a801e3df7e)
<br/>
<br/>

#### 加载证书可以使用参数 --ssl-cert （未验证）
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://127.0.0.1:8083 --ssl-cert .\cert\mitm-server.crt
```
多个证书 --ssl-cert 证书1  --ssl-cert 证书2
<br/>
<br/>

#### 设置代理
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://user:pwd@127.0.0.1:8083 
```
##### 使用配置文件
![image](https://github.com/user-attachments/assets/e8970174-7ba4-4ced-95b5-ae50934c65ed)

<br/>
<br/>

#### 设置代理，使用账号密码
![image](https://github.com/user-attachments/assets/e0d73148-d55d-4d60-a203-af4700481258)
没使用账号密码前:<br/>
![image](https://github.com/user-attachments/assets/550b03d1-c42a-4a92-bc3e-3791e1b7cce6)
使用账号密码后: <br/>
![image](https://github.com/user-attachments/assets/49fbcd52-cbb9-4a29-8fd4-6c7278102090)
![image](https://github.com/user-attachments/assets/ce7632bc-e8b3-45b3-a73d-99095d7df9de)


#### 设置代理，跳过指定的域名
可以看到我们第一次抓包，会有很多的没用的域名，可以通过参数来过滤, 抓取到的数据包就干净了很多
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://127.0.0.1:8083 --proxy-bypass "*google.com" --proxy-bypass "*alicdn.com" --proxy-bypass "*mmstat.com" --proxy-bypass "*googleapis.com" --proxy-bypass "*gvt1.com" --proxy-bypass "*gstatic.com"
```
![image](https://github.com/user-attachments/assets/50a912bb-15c9-4ce9-8f29-08efe4bb9de7)
<br/>
实现方法:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;对于 s 模式下，通过, 下方图片的函数匹配规则，输入的域名是否需要代理，不需要则设置为 None。
&nbsp;&nbsp;&nbsp;&nbsp;对于 d 模式下，会加载其他的不相关的 url，所以通过加载**浏览器插件实现**，所以需要注意的是，如果你指定的是 d 模式下的域名，**则 Python 的正则可能不适用插件**<br/>
![image](https://github.com/user-attachments/assets/9eb110af-cbe0-44b8-b683-40f5416c0f26)
##### 通过配置文件
![image](https://github.com/user-attachments/assets/9eca9d16-799b-45cd-9acf-ed674e860aa3)<br/>
![image](https://github.com/user-attachments/assets/273cb549-57fe-4bf4-af09-aad1095f7f53)<br/>
<br/>
<br/>
<br/>
<br/>

### (三)、请求携带URL参数
```
 python .\webPageScreenshot.py --url http://www.localhost.com --params '{\"User-Agent\": \"my-agent\"}'  --proxy http://127.0.0.1:8083
```
![image](https://github.com/user-attachments/assets/9adc6adc-bd43-4fa7-be45-b96720700a53)
<br/>
<br/>
<br/>
<br/>

### (四)、携带请求json
```
python .\webPageScreenshot.py --method POST --url http://www.localhost.com:5000  --proxy http://127.0.0.1:8083  --proxy-bypass "*google.com" --proxy-bypass "*alicdn.com" --proxy-bypass "*mmstat.com" --proxy-bypass "*googleapis.com" --proxy-bypass "*gvt1.com" --proxy-bypass "*gstatic.com" --json '{"page": 1, "num": 2}'
```
![image](https://github.com/user-attachments/assets/0cc69c29-c18b-4909-af34-6755e708dae4)
对于测试json个人建议使用配置文件更加的方便<br/>
```
python .\webPageScreenshot.py --config .\config.ini
```
![image](https://github.com/user-attachments/assets/aafba3a1-9de2-49fe-90a4-0d8491194d75) <br/>
![image](https://github.com/user-attachments/assets/a159e894-61e0-4620-a52a-77828e861068) <br/>
<br/>
<br/>
<br/>
<br/>

### (五)、携带请求data
```
python .\webPageScreenshot.py --method POST --url http://www.localhost.com:5000  --proxy http://127.0.0.1:8083  --proxy-bypass "*google.com" --proxy-bypass "*alicdn.com" --proxy-bypass "*mmstat.com" --proxy-bypass "*googleapis.com" --proxy-bypass "*gvt1.com" --proxy-bypass "*gstatic.com" --data "测试=1"

```
![image](https://github.com/user-attachments/assets/35d70513-ac3f-412c-b149-0362caa7f6e6)<br/>
##### 使用配置文件
![image](https://github.com/user-attachments/assets/9e927197-5c78-4551-bc19-386fd7f3cf9d)<br/>
![image](https://github.com/user-attachments/assets/8d4695bd-3f53-479f-ba91-63b443f41ee1)<br/>
<br/>
<br/>
<br/>
<br/>

### (六)、携带请求 file
```
python .\webPageScreenshot.py --url www.localhost.com:5000/post --files '{\"config.ini\": \"./config.ini\"}' --proxy http://127.0.0.1:8080
```
![image](https://github.com/user-attachments/assets/7926c24a-f9e0-4ed2-b844-88fe85280e88)

##### 通过配置文件
![image](https://github.com/user-attachments/assets/0308be17-b62d-452a-b26c-bcf8cbe541b0)
![image](https://github.com/user-attachments/assets/feb59239-7e80-45d7-87e3-635c38612a05)

<br/>
<br/>
<br/>
<br/>

### (七)、请求添加头部

如果需要多个头部，则使用多个 --headers 来指定
```
python .\webPageScreenshot.py --method POST --url http://www.localhost.com  --proxy http://127.0.0.1:8080  --json="666" --headers "User-Agent: bbbb\nw: 11111"  --headers "bb: bbbb"
```
![image](https://github.com/user-attachments/assets/359628f4-9607-49a4-a99a-1f9ba27359e4)

通过配置文件指定<br/>
![image](https://github.com/user-attachments/assets/df16e97e-b679-459d-855a-0e64a2acec49)
![image](https://github.com/user-attachments/assets/74816905-390b-4299-8142-3c082733897e)
<br/>
<br/>
<br/>
<br/>

### (八)、添加cookie
```
python .\webPageScreenshot.py  --method GET --url http://www.localhost.com:5000/get  --proxy-bypass "*google.com" --proxy-bypass "*alicdn.com" --proxy-bypass "*mmstat.com" --proxy-bypass "*googleapis.com"  --proxy http://127.0.0.1:8080   --json '{\"A\": 1}' --cookies '{\"a\": \"b\"}'
```
![image](https://github.com/user-attachments/assets/f9d29d2c-e166-4228-83a1-8aa4db9142bc)

##### 通过配置文件
![image](https://github.com/user-attachments/assets/855a0a08-01a8-435a-8da0-70a5a66fd1c8)

![image](https://github.com/user-attachments/assets/c6431cab-5905-4c25-8d96-f59f926d6da7)
<br/>
<br/>
<br/>
<br/>

### (九)、D模式下的 注入js 脚本
排除百度，匹配其他所有，执行弹窗 `inject.js`<br/>
```
python .\webPageScreenshot.py --url www.baidu.com --url www.taobao.com --js .\inject.js
```

利用插件，实现js脚本的注入，实现其他功能（也许可以用其他插件实现？) <br/>
缺点:<br/>
  只支持 d 模式。测试中发现不能使用弹窗 (否则会算成访问超时, 所以官方文档里有对应的处理弹窗的方法，但是我怕如果哪个网站点击了不该点击的不太好，就没有添加了)，不过可以用js创建模态框来曲线救国哈哈<br/>
js脚本模板:
```
// ==UserScript==
// 匹配的域名
// @match        https://*/*
// 排除的域名
// @exclude      *://*baidu.com/*
// ==/UserScript==

(function() {
    'use strict';
// 创建模态框的函数
    function createModal() {
        // 创建模态框的外部容器
        const modalOverlay = document.createElement('div');
        modalOverlay.style.position = 'fixed';
        modalOverlay.style.top = '0';
        modalOverlay.style.left = '0';
        modalOverlay.style.width = '100%';
        modalOverlay.style.height = '100%';
        modalOverlay.style.backgroundColor = 'rgba(0, 0, 0, 0.7)'; // 透明背景
        modalOverlay.style.display = 'flex';
        modalOverlay.style.alignItems = 'center';
        modalOverlay.style.justifyContent = 'center';
        modalOverlay.style.zIndex = '1000';

        // 创建模态框内容
        const modalContent = document.createElement('div');
        modalContent.style.backgroundColor = 'white';
        modalContent.style.padding = '20px';
        modalContent.style.borderRadius = '8px';
        modalContent.style.textAlign = 'center';
        modalContent.style.width = '80%'; // 占据页面 80%
        modalContent.style.fontSize = '2em'; // 增大文字

        // 添加文本
        const modalText = document.createElement('p');
        modalText.textContent = '我是好人';
        modalContent.appendChild(modalText);

        // 添加关闭按钮
        const closeButton = document.createElement('button');
        closeButton.textContent = '关闭';
        closeButton.style.marginTop = '10px';
        closeButton.onclick = function () {
            document.body.removeChild(modalOverlay);
        };
        modalContent.appendChild(closeButton);

        // 将内容添加到外部容器
        modalOverlay.appendChild(modalContent);

        // 将模态框添加到文档
        document.body.appendChild(modalOverlay);
    }

// 调用函数创建并显示模态框
    createModal();

})();
```
效果预览:<br/>
可以看到匹配到域名后创建模态框，弹窗显示我是好人。哈哈<br/>
![image](https://github.com/user-attachments/assets/5d01e14e-b627-420d-a961-bc8e3c95d6f5)<br/>
![image](https://github.com/user-attachments/assets/11e95dc2-f69e-42cd-8102-d4880b7dae5b)





### 配置文件参数
```
          'url': [],  # URL 列表，可以指定多个 ['http://www.baidu.com', 'www.taobao.com']
        'file': '',  # 读取的存储 url列表的 文件 ./url.txt
        'method': 'GET', # 请求模式, 需要手动指定请求模式，否则 GET如果指定了data，GET也会提交data，其他同理
        'params': '',  # url 请求参数， 就是转为 /index?参数key=参数value
        'data': str(None),   # 携带的数据
        'json': str(None),  # 要发送的 JSON 数据，会自动设置 Content-Type 为'application/json'
        'files': str(None),  # 上传的文件，可以是一个字典，其中键是文件名，值是文件对象或文件路径
        'headers': [],  # 请求头 ['User-Agent: AAAA', ]
        'headers_bypass': [],   # 跳过的主机列表 ['*localhost']
        'cookies': str(None),   # {}   # 添加请求的 cookie，json格式
        'del_cookies': 'False', # 访问前删除所有 cookie
        'timeout': '6, 8, 8',   # 页面超时设置
        'retry_times': '0',     # 重试次数
        'retry_interval': '2.0',    # 重试间隔
        'allow_redirects': 'True',  # 允许重定向
        'ssl_cert': [],  # 证书
        'proxy': str(None),   # 代理 支持账号密码
        'proxy_active': str(None),  # 代理可用性验证
        'proxy_bypass': [],   # 跳过代理的主机
        'browser_path': '',     # 指定使用的浏览器路径
        'local_port': '',   # 指定浏览器的端口
        'auto_port': 'False',  # 自动寻找端口
        'download_path': './ScreenShot_Download',    # 程序下载路径
        'user_data_path': './ScreenShot_User_Data',    # 用户数据目录
        'del_user_data': 'False',   # 退出浏览器后，删除用户目录
        'js': [],  # js注入的js脚本
        'force_stop_browser': 'False',  # 退出浏览器时，强制退出
        'no_sandbox': 'True',   # 不启用沙盒模式
        'no_headless': 'False',     # 关闭 无头模式
        'incognito': 'False',   # 启用无痕浏览
        'ignore_certificate_errors': 'True',    # 忽略 SSL 证书错误
        'start_maximized': 'True',  # 启动时窗口最大化
        'extensions': [],   # 浏览器扩展插件
        'del_extensions': 'False',  # 删除浏览器插件文件
        'set_arguments': [],    # 设置其他 浏览器的参数
        'remove_arguments': [],  # 删除指定的浏览器参数
        'clear_arguments': 'False',     # 启动前清楚所有浏览器配置
        'full_page': 'False',   # 整页滚动截屏
        'threads': '5', # 每次打开多少的个标签页，也就是多少线程去执行
        'output_path': '.',  # html 输出文件的路径
        'no_log': 'False',   # 不输出日志文件
        'finger': 'False',   # 开启指纹识别
```

