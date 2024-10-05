# Python实现的访问网页截图

## 这是什么
一个访问网页，并且截图的工具.
<br/>
<br/>
- 支持 POST （JSON、data、file）
- 支持 GET (json、data、file)
- 要手动指定 POST，不然默认就是 GET
- 默认情况下，程序使用 9222 端口，浏览器可执行文件路径为'chrome'。第三方库官方文档: https://drissionpage.cn/browser_control/connect_browser
- Ctrl + C 可以结束，理论上，不会有残留的进程，因为我用屎山代码不断的尝试退出。但是如果访问的url很多，可能结束很慢，等不及的自己手动结束进程吧，Windows taskkill /IM chrome.exe /F,嘿嘿
- 输出一个html文件，截图也在里面, 无其他生成（除了运行的日志文件夹、本身开启浏览器创建的用户配置文件、如果使用代理则会生成一个插件目录、如果使用配置文件 --config , 首次指定会创建你指定的名称的，默认的配置文件）
- 运行的时候会出现一个白色的背景，不知道咋关，明明无头模式。

## 自问自答环节:
<br/>

```
​	我:
​		有大佬写的截图工具，`gowitness` 而且是用 go 写的，更快，为什么还要写？
​	答：
​		因为我菜，不会 GO，只会Python，我只是个导包侠 ┭┮﹏┭┮, 而且大佬的没看到参数支持 POST, 而且输出的很多图片，图片文件又不适合携带特殊的字符串
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

## 依赖
```text
pip install DrissionPage
```
<br/>
<br/>
<br/>
<br/>

## 使用
DrissionPage 这个库分为两种访问模式：d 模式用于控制浏览器，s 模式使用requests收发数据包 (https://drissionpage.cn/browser_control/mode_change/#%EF%B8%8F-mode), 也许可以粗略的认为，一个类似用chromedriver 控制访问，一个用 requests 去访问。
**<span style="color:red">注意:</span>**
>     headers/params/data/json/file/cookies/allow_redicts 参数在 s 模式下才会生效，所以当出现这些参数的时候，可以粗略的认为，切换到了requests 去请求，
>     官方文档内写着: https://drissionpage.cn/SessionPage/visit
>     所以，我设置了如果携带这些参数的时候，指定的多个证书，只会读取第一个，这样你只能指定的格式为pem啦，哈哈
>     ![image](https://github.com/user-attachments/assets/469fc0b6-55f0-4403-8fb0-bdca3221bcdc)
>     官方文档: https://drissionpage.cn/SessionPage/visit/#%EF%B8%8F%EF%B8%8F-post

为啥我关闭了这个参数，因为，会在当前文件夹下创建了 User Data里面的一堆东西，乱死了，所以我手动指定，默认为当前文件夹下的 User Data<br/>
官方文档: https://drissionpage.cn/tutorials/functions/new_browser/#%EF%B8%8F%EF%B8%8F-auto_port%E6%96%B9%E6%B3%95<br/>
![image](https://github.com/user-attachments/assets/d67fadf9-d6c0-49ff-b182-8256d50699e5)

![image](https://github.com/user-attachments/assets/da8e943a-6722-48e0-ab5c-d105308e4e00)

<br/>
<br/>
<br/>
<br/>

### 一、基本访问
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

### 二、使用代理
#### 代理抓包软件
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://127.0.0.1:8083
```
![image](https://github.com/user-attachments/assets/656d0d42-1ebb-40fc-aaca-e8a801e3df7e)
<br/>
<br/>

#### 加载证书可以使用参数 --ssl-cert 
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

### 三、请求携带URL参数
```
 python .\webPageScreenshot.py --url http://www.localhost.com --params '{\"User-Agent\": \"my-agent\"}'  --proxy http://127.0.0.1:8083
```
![image](https://github.com/user-attachments/assets/9adc6adc-bd43-4fa7-be45-b96720700a53)
<br/>
<br/>
<br/>
<br/>

### 四、携带请求json
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

### 五、携带请求data
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

### 六、携带请求 file
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

### 七、请求添加头部

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

### 八、添加cookie
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

### 九、报错:
![image](https://github.com/user-attachments/assets/8fe3b0ae-cdf4-46b9-bbe1-fa75c32b37b5)
解决:<br/>
在路径.\screenshot\module\url\下的 topdomain.py 中添加域名
原因: 我爬取了维基页面、腾讯页面、阿里页面的所有顶级，有些不常见的可能被识别为错误的域名，URL验证中为了防止误入类似1.jpg的被识别为域名，嘿嘿
![image](https://github.com/user-attachments/assets/b85629af-c36c-4aad-bb76-2d75404dad47)

### 十、测试:
![3b2199d0b4c4e28413478b0974b84f3](https://github.com/user-attachments/assets/05a91183-ae5e-4bf4-a42d-328c4a8bc72f)
![b99540e5643ea722815eb988d3ac5d2](https://github.com/user-attachments/assets/fd62707b-da5b-472b-aa3c-cf8b2281a383)
![image](https://github.com/user-attachments/assets/b91f9cce-6cf1-4837-a89f-6e599fb5e44e)


## 有 bug 联系作者:
备注： GitHub
![13f909da0b79b8341ff15a5ce5c194a](https://github.com/user-attachments/assets/c99d053d-7d1d-4353-9e9a-a11d1c14d897)
