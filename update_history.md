## 更新
#### 更新日期：2024年10月11日-新增参数 --split 指开启分割输出文件，如果已经输出则指定输出的路径 + 使用 --split。（解决版本: 2024年10月11日_4_WebPageScreenShot.zip)
#### 更改日期: 2024年10月11日-使用新增使用Ehole原本的go封装成dll，供python调用，以此提高遍历 json速度。（解决版本: 2024年10月11日_WebPageScreenShot.zip）
修复 thread 问题
修复指纹识别时 favicon.ico 路径匹配问题<br/>
![image](https://github.com/user-attachments/assets/56b1c0ce-dfdc-4e60-a742-0c606dc321f2)<br/>
修改，默认使用 ehole 原项目指纹识别封装成dll后，供python调用，提高速度，当平台不是 Windows 或 Linux 时候使用原生Python实现（所以如果使用正则可能会有差异）<br/>
![image](https://github.com/user-attachments/assets/d9834ac6-6013-4a0e-9a23-0268b1135158)<br/>
![image](https://github.com/user-attachments/assets/2587c35b-2d48-497b-b795-b5988b031d46)<br/>

#### 更改日期: 2024年10月9日-新增指纹开启指纹识别 --finger (解决版本: 2024年10月9日_WebPageScreenShot.zip)
#### 更改日期: 2024年10月7日-添加新的参数--js，指定d模式下js注入的脚本(解决版本: 2024年10月7日_2_WebPageScreenShot.zip)

#### 更改日期: 2024年10月7日-添加新的参数，用于让输出更干净：（解决版本:2024年10月7日_WebPageScreenShot.zip）

#### 更改日期: 2024年10月6日-发现问题：(解决版本: 2024年10月6日_3_WebPageScreenShot.zip)
(1)、超时参数仅对 s 模式 和 d 模式下生效问题<br/>
解决方案:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;经阅它的源代码，发现，只需要在配置类中，指定好三个页面超时时间，即可<br/>
&nbsp;&nbsp;&nbsp;&nbsp;它会依据模式自动提取 d 模式下的第二个页面加载超时时间作为timeout，<br/>
&nbsp;&nbsp;&nbsp;&nbsp;源文件文件路径: venv/Lib/site-packages/DrissionPage/_pages/mix_tab.py<br/>
![image](https://github.com/user-attachments/assets/6627a938-03df-403f-bac7-4118e961726d)<br/>
<br/>

(2)、ERROR - 处理 URL http://www.localhost.com:5000 时出错: 此功能需显式设置下载路径（使用set.download_path()方法、配置对象或ini文件均可）。 对于参数的处理问题<br/>
解决方案:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;查阅官方文档，似乎和我预想的不一样，我以为是对于访问后自动接收，保存到文件夹中，但是实际似乎需要主动去下载。
<br/>

(3)、纠正 --help 现实的帮助信息错误<br/>
  - 纠正参数 --download-path ，现在，它可以设置，但是实际上它没有任何意义，预留参数
  - 统一文件夹名称为 ScreenShot_ 开头,下载: ScreenShot_Download（未来可能用上） 日志: ScreenShot_Logs 插件: ScreenShot_Extensions
<br/>

(4)、'dict' object cannot be interpreted as an integer<br/>
解决方案：<br/>
应该是多线程遍历 维护的列表 browser_tab 列表的时候，弹出元素导致的，修改逻辑新增key值，初始化时为设置状态 active: True，关闭后为 False<br/>


#### 更改日期: 2024年10月6日-发现问题: (解决版本: 2024年10月6日_2_WebPageScreenShot.zip)
(1)、优化，新增参数添加是否滚动截屏，之前的，滚动截屏，浪费时间。<br/>
解决方案: <br/>
&nbsp;&nbsp;&nbsp;&nbsp;利用官方提供的参数，指定 full_page = False 即可 
<br/>

(2)、处理 s 和 d 的两个模式经过测试返回值都是 bool  类型，之前错误理解 <br/>
解决方案：<br/>
&nbsp;&nbsp;&nbsp;&nbsp;那就去掉响应状态码吧，影响不大。 
<br/>

(3)、修复逻辑 当只启动一个浏览器时，没有关闭，或者多个的时候，没有关闭最后一个。<br/>
解决方案:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;利用之前维护的列表 browser_tab , 该线程执行完毕，调用浏览器对象退出，退出成功，将浏览器信息弹出列表，程序运行结束，遍历列表如果存在浏览器，则调用退出方法
<br/>

(4)、新增参数，阅读官方文档发现两个新的参数， force 强制退出浏览器，和 del_data 退出后删除用户目录。(√)<br/>
<br/>

(5)、之前的不小心把启动时最大化判断参数给注释了<br/>
<br/>

#### 更改日期: 2024年10月6日，改进访问到 200多个 URL后CPU和内存飙升问题
解决方案:
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
