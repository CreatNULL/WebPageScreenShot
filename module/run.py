# coding: utf-8
""" 主要是导入各个模块，组合

Author: CreateNULL
Date: 2024-10-5
Description: A simple web page screenshot tool.
Copyright (c) 2024 CreateNULL. All rights reserved.
Version: 1.0.0
谁商用谁是狗，哪天要是被挂咸鱼了，卖家就是大傻狗（不是中华田园犬)
"""
import os
import json
import logging  # 日志记录
import configparser   # 配置文件读取
from DrissionPage import Chromium   # 实现截图的第三方库
from concurrent.futures import ThreadPoolExecutor, as_completed  # 多线程
from requests.exceptions import ConnectionError # 浏览器连接错误
from module.url.urlmodify import ModifyURL  # URL处理类
from module.network.initbrowser import init_browser  # 初始化配置对象， 用于创建
from module.network.screenshot import screenshot_page  # 实现截图的模块
from module.output.writeresult import WriteResult  # 写结果到 html
from module.proxy.verif import verify_proxy  # 验证代理格式
from module.proxy.verif import match_bypass_domain  # 提供对输入的域名，跳过代理的域名支持
from module.extension.add import create_proxy_extension, unzip_file # 浏览器代理插件，以及解压
from module.extension.add import create_add_headers_extension # 浏览器添加头部插件
from module.extension.delete import remove_matching_extension  # 卸载插件
from module.config.init import generate_config_ini  # 初始化配置文件
from module.config.load import load_config as load_cfg # 载入配置

# 关闭单例模式， 你不会喜欢关闭的，因为如果关闭，会一个url 一个程序窗口，不是无头模式下，嘿嘿爆米花

# from DrissionPage.common import Settings
# Settings.singleton_tab_obj = False

tab_ids = []  # 记录生成的标签 id
EXTENSION_PATH = './WebPageScreenshotExtensions'  # 扩展生成的路径，程序运行后，将生成的插件解压到该路径下指定的文件夹
PROXY_EXTENSION_PATH = os.path.join(EXTENSION_PATH, 'proxy')  # 代理插件的解压路径
HEADERS_EXTENSION_PATH = os.path.join(EXTENSION_PATH, 'headers')  # 代理插件的解压路径
if not os.path.exists(EXTENSION_PATH):
    os.makedirs(EXTENSION_PATH, exist_ok=True)
if not os.path.exists(PROXY_EXTENSION_PATH):
    os.makedirs(PROXY_EXTENSION_PATH, exist_ok=True)
if not os.path.exists(HEADERS_EXTENSION_PATH):
    os.makedirs(HEADERS_EXTENSION_PATH, exist_ok=True)
LOG_LEVEL = logging.INFO  # 控制日志输出级别

OUTPUT_REQUEST_ERROR_URL = False  # 记录访问成功 URL
OUTPUT_REQUEST_SUCCESS_URL = False  # 记录访问失败 URL

# 创建日志输出目录（如果不存在）
log_dir = 'WebPageScreenshotLogs'
os.makedirs(log_dir, exist_ok=True)

# 设置日志文件路径
log_file_path = os.path.join(log_dir, 'app.log')

# 创建日志记录器
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)

# 创建文件处理器
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(LOG_LEVEL)

# 创建终端处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加处理器到记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# 加载配置文件
def load_config(args):
    # 处理配置文件和命令行参数的关系
    if args.config:
        # 读取配置文件
        if not os.path.exists(args.config):     # 配置文件不存在
            config = generate_config_ini(config_file=args.config)
        else:
            config = configparser.ConfigParser()
        # 返回 args对象
        args = load_cfg(args, config)

    return args


# 从文件中读取 url
def read_urls_from_file(file_path):
    """ 从文件中读取 URL """
    urls = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                stripped_line = line.strip()
                if stripped_line:
                    urls.append(stripped_line)
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
    return urls


# 加载 url
def load_urls(args,):
    """ 处理 URL 将URL分类、查看是否有不合法的 URL，有则记录，无则将不规范的 URL 规范化

    """
    # 加载 URL
    if not args.url and not args.file:  # 两处都没用指定
        return None
    elif args.url:  # 命令行给了 urls
        input_urls = args.url
    elif args.file:  # 命令指定从文件中读取
        input_urls = read_urls_from_file(args.file)
    else:
        ...

    # 提取处理
    url_modify = ModifyURL()
    url_result = url_modify.filter(urls=input_urls, # 访问的urls列表
                                   original_order=False,  # 分类排序
                                   no_empty=True,   # 去空
                                   deduplicate=True  # 去重
                                   )

    # URL 分类提取
    domain_strict = url_result[0]['domain_strict']
    domain_lenient = url_result[0]['domain_lenient']
    ip_strict = url_result[0]['ip_strict']
    ip_lenient = url_result[0]['ip_lenient']
    urls = url_result[0]['url']
    other = url_result[0]['other']

    if any(other):
        logging.error(f"存在错误的 URL: {str(other)}")
        for _ in other:
            print(_)
        return
    else:
        # 将其他的转为 URL
        new_urls = ([_['derivative'] for _ in url_modify.add_protocol(domain_strict) +
                 url_modify.add_protocol(domain_lenient) +
                 url_modify.add_protocol(ip_lenient) +
                 url_modify.add_protocol(ip_strict)] +
                urls
        )

    return new_urls


def remove_plugins(args):
    secure_preference = os.path.join(args.user_data_path, 'Default/Secure Preferences')
    for plugin_path in [HEADERS_EXTENSION_PATH, PROXY_EXTENSION_PATH] + args.extensions:
        try:
            remove_matching_extension(secure_preferences_file=secure_preference, target_plugn_path=plugin_path)
        except FileNotFoundError:
            continue


# 加载代理
def load_proxy(args):
    # 设置代理，创建代理插件
    logging.info(f"使用代理")
    # 返回 requests 需要的格式，和 原始的 http://user:pwd@127.0.0.1:8080 格式
    proxy_requests_format, proxy_info = verify_proxy(args.proxy, args.proxy_active)

    # 重赋值给 args.proxy , 给 screenshot 中的请求函数使用
    args.proxy = proxy_requests_format

    # 提取参数给创建代理插件使用
    protocol = proxy_info['protocol']
    host = proxy_info['host']
    port = proxy_info['port'] if 'port' in proxy_info else '80' if proxy_info['protocol'].lower() == 'http://' else '443' if proxy_info['protocol'].lower() == 'https://' else ''
    user = proxy_info['username'] if proxy_info['username'] else ''
    pwd = proxy_info['password'] if proxy_info['password'] else ''

    if args.proxy_active:
        logging.info("激活代理存活验证...")

    logging.info(f"使用代理: 协议->{protocol},账号->{user + ':' if user else ''},密码->{'*'*len(pwd)}, 主机->{host}, 端口->{proxy_info['port'] if proxy_info['port'] else ''}")

    if args.proxy_bypass:
        logging.info(f"跳过以下host不代理: {str(args.proxy_bypass)}")

    # 创建插件
    logging.info("创建代理插件")
    proxy_plug = create_proxy_extension(scheme=protocol.split(':')[0],
                                        proxy_host=host,
                                        proxy_port=port,
                                        proxy_username=user,
                                        proxy_password=pwd,
                                        plugin_path=EXTENSION_PATH,
                                        bypass=args.proxy_bypass)
    # 解压插件
    logging.info(f"解压插件: {proxy_plug} -> {PROXY_EXTENSION_PATH}")
    unzip_file(src=proxy_plug, dest=PROXY_EXTENSION_PATH)
    # 加载插件
    args.extensions = args.extensions + [PROXY_EXTENSION_PATH]
    return args


# 加载头部
def load_headers(args):
    # 设置代理，创建代理插件
    logging.info(f"使用添加头部")
    # 创建插件
    logging.info("创建添加头部插件")
    headers = {}
    try:
        for line in args.headers:
            # 从配置文件中读取可能多一个 ''
            if line.strip():
                key, value = line.split(": ", 1)
                headers[key] = value
        args.headers = headers
    except ValueError as e:
        logging.error(f"错误的 HTTP 头部格式 {args.headers}, 注意需要安照 ': ' 而不是 ':' 哦~, {str(e)}")
        return

    headers_plug = create_add_headers_extension(plugin_path=HEADERS_EXTENSION_PATH, headers=args.headers, bypass=args.headers_bypass)
    # 解压插件
    logging.info(f"解压插件: {headers_plug} -> {HEADERS_EXTENSION_PATH}")
    unzip_file(src=headers_plug, dest=HEADERS_EXTENSION_PATH)
    # 加载插件
    args.extensions = args.extensions + [HEADERS_EXTENSION_PATH]

    return args

    
# 实例化浏览器对象
def load_browser(args):
    # 初始化配置对象
    co, infos = init_browser(
        # config_path=args.config_path,  # 预留 这个第三方库的配置文件
        # save_config=args.save_config,  # 预留 是否保存该配置文件
        browser_path=args.browser_path,
        local_port=args.local_port,
        auto_port=args.auto_port,
        download_path=args.download_path,
        user_data_path=args.user_data_path,
        no_sandbox=args.no_sandbox,
        headless=True if not args.no_headless else False,
        incognito=args.incognito,
        ignore_certificate_errors=args.ignore_certificate_errors,
        start_maximized=args.start_maximized,
        extensions=args.extensions,
        time_out=tuple(args.timeout),
        retry_times=args.retry_times,
        retry_interval=args.retry_interval,
        use_system_user_path=args.use_system_user_path,
        set_arguments=args.set_arguments,
        remove_arguments=args.remove_arguments,
        clear_arguments=args.clear_arguments,
        ssl_cert=args.ssl_cert,
    )
    logging.debug(f"args 配置: {vars(args)}")
    logging.debug(f"详细浏览器配置: {infos}")
    logging.info("依据配置初始化浏览器对象")
    browser = Chromium(addr_or_opts=co)
    return browser


# 访问url
def process_url(browser, url, args, write_result):
    """ 被多线程调用 ，调用截图函数 screenshot_page """
    logging.info(f"访问 URL: {url}")
    logging.debug("创建新的标签页")
    new_tab = browser.new_tab()
    logging.debug("记录标签页 id: {}".format(new_tab.tab_id))
    tab_ids.append(new_tab.tab_id)
    logging.debug("开始访问截图")
    tab_result = screenshot_page(tab=new_tab,
                                 url=url,
                                 method=args.method,
                                 params=args.params,
                                 headers=args.headers if not match_bypass_domain(url, args.proxy_bypass) else None,
                                 data=args.data,
                                 json=args.json,
                                 files=args.files,
                                 allow_redirects=args.allow_redirects,
                                 cookies=args.cookies,
                                 del_cookies=args.del_cookies,
                                 # s 模式下的 代理设置, 以及调用 match_bypass_domain 匹配是否需要跳过代理
                                 proxy=args.proxy if not match_bypass_domain(url, args.proxy_bypass) else None,
                                 # s 模式下的证书 验证，如果为false则为关闭，否则，传递第一个指定的证书，它不支持多个证书
                                 verify_ssl=False if args.ignore_certificate_errors and not args.ssl_cert else args.ssl_cert[0],
                                 # hide=False if not args.no_headless else True,
                                 )
    # 关闭标签页
    logging.info("访问结束, 关闭标签页...")
    new_tab.close()
    logging.info("写入HTML")
    write_result.write_html_body(data=tab_result)
    return url


# 调用上方 process_url 执行多线程访问
def run(args, browser, urls):
    logging.info("多线程访问...")
    # 处理写入结果
    logging.info("实例化结果处理类")

    # 写入文件类
    write_result = WriteResult(output=args.output_path)
    logging.info("写入 HTML文件 头部 + 基本 css 样式")
    write_result.write_html_head()

    # 使用线程池处理多个URL
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        try:
            futures = {executor.submit(process_url, browser, url, args, write_result): url for url in urls}
            for future in as_completed(futures):
                url = futures[future]
                # 获取结果
                try:
                    future.result()  # 获取结果以捕获异常
                    # 结束输出访问成功
                    if OUTPUT_REQUEST_SUCCESS_URL:
                        write_result.write_success_url(url=url)
                except Exception as e:
                    logging.error(f"处理 URL {url} 时出错: {e}")
                    #  输出访问失败的
                    if OUTPUT_REQUEST_ERROR_URL:
                        write_result.write_error_url(url=url)
        except KeyboardInterrupt:
            logging.warning("用户手动退出")
            # 基本可以关闭了
            try:
                logging.debug("尝试关闭标签页")
                browser.close_tabs(tab_ids)
                logging.debug("尝试退出浏览器")
                browser.quit()
                if os.name == 'nt':
                    os.system(f"taskkill /PID {browser.process_id} /F")
            except KeyboardInterrupt:
                logging.debug("再次被 Ctrl + C 终止, 尝试关闭标签页, 以及退出浏览器, 杀死关闭进程")
                browser.close_tabs(tab_ids)
                browser.quit()
                if os.name == 'nt':
                    os.system(f"taskkill /PID {browser.process_id} /F")

    # 需要注意的是，程序结束时浏览器不会自动关闭，下次运行会继续接管该浏览器。无头浏览器因为看不见很容易被忽视。可在程序结尾用browser.quit()将其关闭。
    # https://www.drissionpage.cn/tutorials/functions/headless
    # 写入 HTML 尾部
    write_result.write_html_foot()
    # 正常退出的
    browser.close_tabs(tab_ids)


# 程序主入口
def main(args=None):
    if not args:
        raise ValueError("请传递 args")

    # 加载配置
    args = load_config(args)

    # 加载 URL, 不可在读取，配置文件上
    new_urls = load_urls(args)
    if not new_urls:
        return

    # 删除所有的插件
    # 卸载上次的
    remove_plugins(args)

    # 添加代理, 是 d 模式下的代理
    if args.proxy:
        args = load_proxy(args)
    else:
        args.proxy = None

    # 加载 cookies
    if args.cookies:
        args.cookies = json.loads(args.cookies)
    else:
        args.cookies = None

    # 添加头部， d 模式下的 头部
    if args.headers:
        args = load_headers(args)
    else:
        # s 模式下的 headers 不允许 赋值为 None，不然报错 'NoneType' object has no attribute 'split'
        args.headers = {}

    if args.files:
        args.files = json.loads(args.files)
    else:
        args.files = None

    # 加载 提交的数据
    try:
        # 加载json格式的 json 提交
        if args.json:
            args.json = json.loads(args.json)
    except json.decoder.JSONDecodeError as e:
        logging.error("json 提交的数据格式错误: " + str(e))
        return

    if not args.data:
        args.data = None

    logging.debug(f"设置的 args: {vars(args)}")

    # 创建浏览器
    browser = load_browser(args=args)

    try:
        # 执行多线程访问
        run(args=args, browser=browser, urls=new_urls)
    finally:
        # 尝试退出
        try:
            browser.close_tabs(tab_ids)
            browser.quit()
        except (ConnectionError, FileNotFoundError, KeyboardInterrupt):  # 上方如果成功退出，浏览器无法连接
            pass
        finally:
            remove_plugins(args)


