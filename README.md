
# Python实现的访问网页截图 （等待修复bug)


## 等待解决的问题
- 超时参数仅对 d 模式下生效问题
- ERROR - 处理 URL http://www.localhost.com:5000 时出错: 此功能需显式设置下载路径（使用set.download_path()方法、配置对象或ini文件均可）。 对于参数的处理问题
  
## 一、这是什么
一个访问网页，并且截图的工具.实现快速访问，批量截图。
<br/>
<br/>

```
- 支持 POST （JSON、data、file）
- 支持 GET (json、data、file)
- 要手动指定 POST，不然默认就是 GET，不管是否使用了 --data   --json --files
- 默认情况下，程序使用 9222 端口，浏览器可执行文件路径为'chrome'。
  - 参考 DrissionPage 第三方库官方文档: https://drissionpage.cn/browser_control/connect_browser
- Ctrl + C 可以结束进程，理论上，不会有残留的进程，除非强行关闭。但是如果访问的url很多，可能结束很慢，等不及的自己手动结束进程吧，或者尝试使用参数 --force-stop-browser 或者 Windows下使用 taskkill /IM chrome.exe /F,嘿嘿
- 建议 Linux 上运行（4GB内存）
- 结果输出
  - 输出文件
     (1). 一个访问成功的文件列表 success_url.txt ，提供给下一步访问等;
     (2). 访问失败文件 error_url.txt ，记录访问失败，如果是应为超时的原因可以重设超时时间，再次运行。
     (3). 运行日志，记录运行流程，方便出问题追踪。
     (4). 一个指定代理时或指定 headers 时创建的代理插件目录
     (5). 一个 result.html 记录访问成功的图片和网站，
     (6)、如果使用配置文件 --config , 首次指定会创建你指定的名称的，默认的配置文件）
- 可以通过指定读取配置文件，创建和使用配置文件是同一个命令 --config 配置文件名称

```

## 二、由来
```
      以前刚开始学习的时候，面对 findsomething 插件提取的url后 或者 fofa 批量查找的 url 想着要是有个工具能帮我访问截图就好啦。
但是，找半天，没找到，想自己实现，那时候只有一个selenium 库，于是用哪个写了一个，作为毕设，结果后面用的是否发现，有时候可以，有时
候到一定数量后就访问失败，一直报错，也不知道为啥原因，它也原生不支持 post，当时通过 js 实现的 post，然后将返回的结果渲染到浏览器再
截图。
      后面发现一个大佬的用go写的项目 gowitness ，确实牛逼，哈哈，但是我没找到有 POST 的参数，有时候我想试试 POST json 也许会有不一
样的效果。但是它不支持似乎。最近看到有个库，刚好国庆有时间，就自己写一个吧，哈哈。
```

<br/>
<br/>

## 三、缺点
  - 建议 Linux 下运行，无论是结束进程和无头模式都很舒服，Windows 运行的时候会出现一个白色的背景，全屏最大，明明无头模式，结束进程还得等他慢慢来。不介意的可以，嘿嘿，或者扔到虚拟机里，桀桀桀

<br/>

## 下个版本目标：添加添加js脚本功能 - 可能成功
https://drissionpage.cn/browser_control/ele_operation/#-run_js<br/>
![image](https://github.com/user-attachments/assets/c599c985-eff5-4755-a4ac-ec4f2c1d3d47)<br/>


### 四、更新
#### 更改日期: 2024年10月6日-发现问题: 超时时间设置问题 <span style="color: red;">等待处理</span> (解决版本: 2024年10月6日_2_WebPageScreenShot.zip)
  - 优化，新增参数添加是否滚动截屏，之前的，滚动截屏，浪费时间。(√)
    - 解决方案: 利用官方提供的参数，指定 full_page = False 即可 
  - 处理 s 和 d 的两个模式经过测试返回值都是 bool  类型，之前错误理解 (√)
    - 解决方案：那就去掉响应状态码吧，影响不大。 
  - 等待修复逻辑 当只启动一个浏览器时，没有关闭，或者多个的时候，没有关闭最后一个。（√）
  - 解决方案:
    - 利用之前维护的列表 browser_tab , 该线程执行完毕，调用浏览器对象退出，退出成功，将浏览器信息弹出列表，程序运行结束，遍历列表如果存在浏览器，则调用退出方法
  - 新增参数，阅读官方文档发现两个新的参数， force 强制退出浏览器，和 del_data 退出后删除用户目录。(√)
  - 之前的不小心把启动时最大化判断参数给注释了

#### 更改日期: 2024年10月6日，改进访问到 200多个 URL后CPU和内存飙升问题
##### 解决方案:
  - 指定阈值，将输入的URL，划分为块，分为不同的任务批次，通过监视上一个浏览器的运行情况，再执行创建下一个浏览器对象，实现阻塞
  - 每个浏览器对象多线程访问，实现多线程的优势，将原本的可选项记录访问失败的URL日志作为必选项，追踪错误方便。
  - 每个浏览器运行的情况实现逻辑:
    (1). 首先，全局维护一个列表 browser_tabs = [], 记录创建的浏览器信息。
    (2). 每次创建，会添加字典 {'browser': '创建的浏览器对象', 'tabs': [该浏览器创建的所有标签对象], 'time': '创建的时间', 'index': '浏览器的编号'} 到列表中
    (3). 通过判断 tabs 列表中的 所有标签的 states.is_alive 属性是否存活，即是否关闭，判断是否创建新的浏览器对象，但是可能会存在卡死的情况
    (4). 处理卡死的情况，通过 time字段，首先上一次到这一次创建浏览器的时间的一半，再次判断，直到归零或者全部退出了，则判断为退出成功。
  - 后期可依据性能修改阈值，不宜低于指定的线程数，不宜太高 300 什么的（底部有测试 1000 条 5 个线程 150 阈值的测试）
  - ![image](https://github.com/user-attachments/assets/52c87cc1-b973-40df-b253-d0c40d76de17)


#### 首次提交日期: 2024年10月5日 - 发现性能题
- 访问到 200 - 300 个url后 CPU和内存瓶颈，猜测是访问过多的url后缓存爆照。

    
<br/>
<br/>

## 五、自问自答环节:
<br/>

```
​	我:
​		有大佬写的截图工具，`gowitness` 而且是用 go 写的，更快，为什么还要写？
​	答：
​		因为我菜，不会 GO，只会Python，我只是个导包侠 ┭┮﹏┭┮,
    而且大佬的没看到参数支持 POST
    输出的很多图片，图片文件名，又不适合携带特殊的字符串，无法快速访问
​	我:
​		为啥使用这个  `DrissionPage`？不用 `Selenium`
​	答:
​		公众号上看到了它的介绍，以前用 `Selenium` 写过一个类似的，结束的时候总是容易僵尸进程，
​		我的`chromedriver.exe` 死在我的后台，太惨啦，
​		`linux` 上还好，`windows` 下 它是老大！！，我Ctrl+C 我还得等他慢慢结束
```

<br/>
看到的公众号上的介绍:
<br/>

本库采用全自研的内核，内置了 N 多实用功能，对常用功能作了整合和优化，对比 selenium，有以下优点：
- 无 `webdriver` 特征
- 无需为不同版本的浏览器下载不同的驱动
- 运行速度更快
- 可以跨 `iframe`查找元素，无需切入切出把 `iframe` 看作普通元素，获取后可直接在其中查找元素，逻辑更清晰
- 可以同时操作浏览器中的多个标签页，即使标签页为非激活状态，无需切换可以直接读取浏览器缓存来保存图片，无需用 GUI 点击另存
- 可以对整个网页截图，包括视口外的部分（90以上版本浏览器支持）可处理非open状态的 shadow-root
  
<br/>
 爱了爱了，我导包我快乐！！膜拜大佬
<br/>
<br/>
<br/>
<br/>

## 六、依赖
```text
pip install DrissionPage
```
<br/>
<br/>
<br/>
<br/>

## 七、使用
DrissionPage 这个库分为两种访问模式：d 模式用于控制浏览器，s 模式使用requests收发数据包 (https://drissionpage.cn/browser_control/mode_change/#%EF%B8%8F-mode), 也许可以粗略的认为，一个类似用chromedriver 控制访问，一个用 requests 去访问。
**<span style="color:red">注意:</span>**
>     headers/params/data/json/file/cookies/allow_redicts 参数在 s 模式下才会生效，所以当出现这些参数的时候，可以粗略的认为，切换到了requests 去请求，
>     官方文档内写着: https://drissionpage.cn/SessionPage/visit
>     所以，我设置了如果携带这些参数的时候，指定的多个证书，只会读取第一个，这样你只能指定的格式为pem啦，哈哈
![image](https://github.com/user-attachments/assets/469fc0b6-55f0-4403-8fb0-bdca3221bcdc)
>     参考官方文档: https://drissionpage.cn/SessionPage/visit/#%EF%B8%8F%EF%B8%8F-post

为啥我关闭了这个参数，因为，会在当前文件夹下创建了 User Data里面的一堆东西，乱死了，所以我手动指定，默认为当前文件夹下的 User Data<br/>
官方文档: https://drissionpage.cn/tutorials/functions/new_browser/#%EF%B8%8F%EF%B8%8F-auto_port%E6%96%B9%E6%B3%95<br/>
![image](https://github.com/user-attachments/assets/d67fadf9-d6c0-49ff-b182-8256d50699e5)

![image](https://github.com/user-attachments/assets/da8e943a-6722-48e0-ab5c-d105308e4e00)

<br/>
<br/>
<br/>
<br/>

### (一)、基本使用
```
python .\webPageScreenshot.py --url http://www.taobao.com 
```
程序首次运行后，会创建配置文件`config.ini`
<br/>
<br/>

##### 程序运行后：
- 会创建两个目录: `WebPageScreenshotExtensions` 、 `WebPageScreenshotLog`和 `User Data` ,分别保存设置代理时创建的插件，程序运行的日志 和 浏览器用户文件夹 (为什么文件名这么长? 我不是有病哦，怕有和其它的冲突)
- 无头模式运行，打开一个白色的页面，但是关掉即可，问题不大
- 一个输出文件名为 result.html ((●'◡'●)这里我懒啦)
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

### (九)、报错:
![image](https://github.com/user-attachments/assets/8fe3b0ae-cdf4-46b9-bbe1-fa75c32b37b5)
解决:<br/>
在路径.\screenshot\module\url\下的 topdomain.py 中添加域名
原因: 我爬取了维基页面、腾讯页面、阿里页面的所有顶级，有些不常见的可能被识别为错误的域名，URL验证中为了防止误入类似1.jpg的被识别为域名，嘿嘿<br/>
![image](https://github.com/user-attachments/assets/b85629af-c36c-4aad-bb76-2d75404dad47)<br/>
<br/>
<br/>

### (十)、测试:
fofa 搜索坤坤关键字，保存数据 1 千 条，使用阈值 150 ，线程 5，超时时间设置 (6, 8, 8), 09:27:36 开始 - 09:53:01 结束, 测试期间内存基本在 2 左右 有时会升到 3 ，CPU基本较低，偶尔飙升到 98%，很快恢复。<br/>
![3b2199d0b4c4e28413478b0974b84f3](https://github.com/user-attachments/assets/05a91183-ae5e-4bf4-a42d-328c4a8bc72f)
![b99540e5643ea722815eb988d3ac5d2](https://github.com/user-attachments/assets/fd62707b-da5b-472b-aa3c-cf8b2281a383)
![image](https://github.com/user-attachments/assets/b91f9cce-6cf1-4837-a89f-6e599fb5e44e)<br/>
开始时间:<br/>
![image](https://github.com/user-attachments/assets/e8a61b7d-2a63-4c86-9678-ac8eab28741c)<br/>

结束时间:<br/>
![image](https://github.com/user-attachments/assets/d28e35d3-65a7-4d1c-8785-4574c9a8cdf8)<br/>
平均每分钟访问URL数量:<br/>
![image](https://github.com/user-attachments/assets/fbe0ed5a-ee44-4b26-ba7f-a7b3a8e9b0a3)<br/>

### 十一、配置文件参数
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
        'download_path': '',    # 程序下载路径
        'user_data_path': './User Data',    # 用户数据目录
        'del_user_data': 'False',   # 退出浏览器后，删除用户目录
        'force_stop_browser': 'False',  # 退出浏览器时，强制退出
        'no_sandbox': 'True',   # 不启用沙盒模式
        'no_headless': 'False',     # 关闭 无头模式
        'incognito': 'False',   # 启用无痕浏览
        'ignore_certificate_errors': 'True',    # 忽略 SSL 证书错误
        'start_maximized': 'True',  # 启动时窗口最大化
        'extensions': [],   # 浏览器扩展插件
        'use_system_user_path': 'False',    # 是否使用安装浏览器的系统用户目录
        'set_arguments': [],    # 设置其他 浏览器的参数
        'remove_arguments': [],  # 删除指定的浏览器参数
        'clear_arguments': 'False',     # 启动前清楚所有浏览器配置
        'full_page': 'False',   # 整页滚动截屏
        'threads': '5', # 每次打开多少的个标签页，也就是多少线程去执行
        'output_path': '.'  # html 输出文件的路径
```
## 有 bug 联系作者:
备注： GitHub
![13f909da0b79b8341ff15a5ce5c194a](https://github.com/user-attachments/assets/c99d053d-7d1d-4353-9e9a-a11d1c14d897)
