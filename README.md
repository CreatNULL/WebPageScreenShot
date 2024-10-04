# WebPageScreenShot
Python实现的访问网页截图

## 这是什么

一个访问网页，并且截图的工具.



## 自问自答环节:

​	我:
​		有大佬写的截图工具，`gowitness` 而且是用 go 写的，更快，为什么还要写？
​	答：
​		因为我菜，不会 GO，只会Python，我只是个导包侠 ┭┮﹏┭┮, 而且大佬的没看到参数支持 POST
​	我:
​		为啥使用这个  `DrissionPage`？不用 `Selenium`
​	答:
​		公众号上看到了它的介绍，以前用 `Selenium` 写过一个类似的，结束的时候总是容易僵尸进程，
​		我的`chromedriver.exe` 死在我的后台，太惨啦，
​		`linux` 上还好，`windows` 下 它是老大！！，我Ctrl+C 我还得等他慢慢结束

看到的公众号上的介绍:

本库采用全自研的内核，内置了 N 多实用功能，对常用功能作了整合和优化，对比 selenium，有以下优点：

- 无 `webdriver` 特征
- 无需为不同版本的浏览器下载不同的驱动
- 运行速度更快
- 可以跨 `iframe`查找元素，无需切入切出把 `iframe` 看作普通元素，获取后可直接在其中查找元素，逻辑更清晰
- 可以同时操作浏览器中的多个标签页，即使标签页为非激活状态，无需切换可以直接读取浏览器缓存来保存图片，无需用 GUI 点击另存
- 可以对整个网页截图，包括视口外的部分（90以上版本浏览器支持）可处理非open状态的 shadow-root

 爱了爱了，我导包我快乐！！膜拜大佬



## 依赖

```text
pip install DrissionPage
```



## 使用

### 一、基本访问

```
python .\webPageScreenshot.py --url http://www.taobao.com 
```

程序首次运行后，会创建配置文件`config.ini`

##### 程序运行后：
- 会创建两个目录: `WebPageScreenshotExtensions` 和 `WebPageScreenshotLog` ,分别保存设置代理时创建的插件，和程序运行的日志 (为什么文件名这么长? 我不是有病哦，怕有和其它的冲突)
- 无头模式运行，打开一个白色的页面，但是关掉即可，问题不大
- 一个输出文件名为 result.html

##### 运行终端显示:
![image](https://github.com/user-attachments/assets/0df0a373-0170-4cb9-8640-14b66a7ed535)

##### 输出文件:
打开后会显示网站标题和缩略图
![image](https://github.com/user-attachments/assets/7a27896b-2c8e-4f7e-96d6-c698598b4a54)
鼠标移动到缩略图后，图片会放大显示，方便快速浏览
![image](https://github.com/user-attachments/assets/632047ee-ed4d-4205-834a-b5f901414b71)
点击标题后，详细信息展开
![image](https://github.com/user-attachments/assets/9c1add3c-0b47-4452-88e8-249ac618d0ba)
![image](https://github.com/user-attachments/assets/04ce64b7-446c-44a4-8e7f-8cbaa967cfe3)

#### 访问多个URL 
```
python .\webPageScreenshot.py --url http://www.taobao.com --url https://hk.jd.com/ --url https://www.baidu.com 
```
![image](https://github.com/user-attachments/assets/5f75b66f-e731-48c0-a04b-1bcb14d46086)



### 二、使用代理
#### 代理抓包软件
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://127.0.0.1:8083
```
![image](https://github.com/user-attachments/assets/656d0d42-1ebb-40fc-aaca-e8a801e3df7e)

#### 加载证书可以使用参数 --ssl-cert 
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://127.0.0.1:8083 --ssl-cert .\cert\mitm-server.crt
```
多个证书 --ssl-cert 证书1  --ssl-cert 证书2

#### 设置代理，理论上我这个是支持账号密码的，因为我是通过插件实现的
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://user:pwd@127.0.0.1:8083 
```
#### 设置代理，跳过指定的域名
可以看到我们第一次抓包，会有很多的没用的域名，可以通过参数来过滤, 抓取到的数据包就干净了很多
```
python .\webPageScreenshot.py --url http://www.taobao.com --proxy http://127.0.0.1:8083 --proxy-bypass "*google.com" --proxy-bypass "*alicdn.com" --proxy-bypass "*mmstat.com" --proxy-bypass "*googleapis.com" --proxy-bypass "*gvt1.com" --proxy-bypass "*gstatic.com"
```
![image](https://github.com/user-attachments/assets/50a912bb-15c9-4ce9-8f29-08efe4bb9de7)


### 三、请求携带参数
```
 python .\webPageScreenshot.py --url http://www.localhost.com --params '{\"User-Agent\": \"my-agent\"}'  --proxy http://127.0.0.1:8083
```
![image](https://github.com/user-attachments/assets/9adc6adc-bd43-4fa7-be45-b96720700a53)



### 四、请求添加头部

如果服务不支，则会返回  Document is empty 类似的错误
```
python .\webPageScreenshot.py --method POST --url http://www.localhost.com  --proxy http://127.0.0.1:8083  --proxy-bypass "*google.com" --proxy-bypass "*alicdn.com" --proxy-bypass "*mmstat.com" --proxy-bypass "*googleapis.com" --proxy-bypass "*gvt1.com" --proxy-bypass "*gstatic.com" --json="666"
```
可以看到虽然报错，但是确实请求了
![image](https://github.com/user-attachments/assets/5ccddaec-6df5-4a7a-8c14-f6ba89fd26ac)



