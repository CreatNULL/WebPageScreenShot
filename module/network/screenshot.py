# coding: utf-8
""" 实现页面截图模块

"""
import os
import logging
from typing import Union
import DrissionPage.errors


def __turn_upload(files: dict) -> dict:
    """ 处理指定的文件上传的参数，转为所需的格式
    """
    if type(files) is not dict:
        raise ValueError("上传指定的文件格式对象不正确")

    # 获取所有的可能的文件路径
    new_file_dict = {}

    for param, file in files.items():
        # 指定的为文件路径
        if os.path.isfile(file):
            try:
                with open(file, "rb") as f:
                    new_file_dict[param] = f.read()
            except Exception as e:
                raise ValueError(f"上传文件读取失败: {str(e)}")
        else:
            # 不是文件，则作为参数的值上传
            new_file_dict[param] = file

    return new_file_dict


def screenshot_page(
        tab,  # 页面标签对象
        url: str,  # 访问的URL
        method: str = 'GET',  # 请求的方式 POST/GET
        params: dict = None,   # URL 请求参数
        headers: Union[dict, str] = None,  # 请求头， dict格式
        data: Union[dict, str] = None,  # 携带的数据
        json: Union[dict, str] = None,  # 要发送的 JSON 数据
        files: dict = None,   # 要上传的文件
        allow_redirects: bool = True,  # 是否允许重定向
        cookies: dict = None,  # 添加 Cookie
        del_cookies: bool = False,  # 是否清除所有 Cookie
        proxy: dict = None,  # 代理设置
        verify_ssl: bool = False,  # 是否验证 SSL 证书
        # hide: bool = True, # 隐藏窗口仅仅支持Windows
):
    r"""
    截取指定页面的截图并返回页面的相关信息。headers/params/data/json/file/cookies/allow_redicts 在 s 模式下才会生效
    每个标签页对象创建时都处于 d 模式, 使用 change_mode()方法进行切换。模式切换的时候会同步登录信息。
    切换后，注意如果设置了代理，需要重新设置，在 .get 中，因为它是 session 模式，而之前是 d 浏览器控制模式，之前的配置对它不生效。

    Args:
        tab: 页面标签对象，表示当前操作的浏览器标签。
        url (str): 要访问的 URL 地址。
        method (str): 请求的方式，支持 'GET' 和 'POST'，默认为 'GET'。
        params (dict, optional): URL 请求参数，默认为 None。
        headers (dict, optional): 请求头，默认为 None。
        data (Union[dict, str], optional): 要携带的数据，默认为 None。
        json (Union[dict, str], optional): 要发送的 JSON 数据，默认为 None。
        files (dict, optional): 要上传的文件，默认为 None。
        allow_redirects (bool): 是否允许重定向，默认为 True。
        cookies (dict, optional): 要添加的 Cookie，默认为 None。
        del_cookies (bool): 是否清除所有 Cookie，默认为 False。
        proxy (dict, optional): 代理设置，默认为 None。
        verify_ssl (bool): 是否验证 SSL 证书，默认为 False。
        hide （bool): 影藏 tab 等，这个方法是直接隐藏浏览器进程。在任务栏上也会消失。只支持 Windows 系统，并且必需已安装 pypiwin32 库

    Returns:
        dict: 包含以下信息的字典：
            - tab_id (str): 当前标签页的 ID。
            - title (str): 页面标题。
            - url (str): 访问的 URL。
            - tab_url (str): 当前标签页的 URL。
            - user_agent (str): User-Agent 信息。
            - method (str): 请求方法。
            - screenshot (str): 页面截图的 base64 编码字符串。
            - status_code (str): HTTP 状态码。
            - timeouts (dict): 超时设置。
            - retry_times (int): 重试次数。
            - retry_interval (float): 重试等待间隔。
            - load_mode (str): 页面加载策略。
            - response_html (str): 页面 HTML 文本。
            - response_json (dict): 请求内容解析为 JSON。
            - proxy (dict, optional): 代理设置，默认为 None。
            - verify_ssl (bool|str): 是否验证 SSL 证书，默认为 False。

    Raises:
        ValueError: 如果 URL 格式不正确，或者请求方法不在允许范围内。
    """

    # 验证 URL 格式
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")

    if headers is not None and not isinstance(headers, dict):
        raise ValueError("Headers must be a dict.")

    if cookies is not None and not isinstance(cookies, dict):
        raise ValueError("Cookies must be a dict.")

    if files is not None and not isinstance(files, dict):
        raise ValueError("Files must be a dict.")

    # 验证请求方法
    if method.upper() not in ['GET', 'POST']:
        raise ValueError("Method must be either 'GET' or 'POST'.")

    # 与 headless 模式不一样，这个方法是直接隐藏浏览器进程。在任务栏上也会消失。只支持 Windows 系统，并且必需已安装 pypiwin32 库才可使用。
    # https://drissionpage.cn/browser_control/page_operation/#-setwindowhide
    # 浏览器隐藏后并没有关闭，下次运行程序还会接管已隐藏的浏览器
    # 浏览器隐藏后，如果有新建标签页，会自行显示出来
    # if hide:
    #     tab.set.window.hide()

    # 清除所有 Cookie
    if del_cookies:
        tab.set.cookies.clear()

    if headers:
        tab.set.headers(headers)
    else:
        headers = {}

    # tab 相关操作: https://www.drissionpage.cn/browser_control/get_page_info

    # 设置文件下载处理模式
    tab.set.when_download_file_exists(mode='rename')

    # s 和 d 模式: https://www.drissionpage.cn/browser_control/mode_change
    # headers/params/data/json/file/cookies/allow_redicts 在 s 模式下才会生效
    # 每个标签页对象创建时都处于 d 模式, 使用change_mode()方法进行切换。模式切换的时候会同步登录信息。
    # 切换模式时只同步 cookies，不同步 headers，
    logging.debug(f"设置请求 -> {url}, 请求头部: {headers}, 参数: {params}, cookie: {cookies}, json: {json}, 数据: {data}, 文件: {files}, 允许重定向: {allow_redirects}, 代理: {proxy}, 验证证书: {verify_ssl}")
    # 这里需要排除重定向，否则基本永远走这下面的逻辑
    # 这里 如果仅仅是 headers 下 我使用 谷歌插件来实现吧

    status_code = None
    response_ok = False

    if params or data or files or json or cookies:
        tab.change_mode(mode='s', go=False, copy_cookies=True)
        if tab.mode != 's':
            raise ValueError("切换到模式 's' 失败")
        # GET 和 POST 方法 -> https://www.drissionpage.cn/browser_control/visit
        # 根据请求模式执行请求

        # 转为文件上传所需的
        if files:
            files = __turn_upload(files)

        if method.upper() == 'POST':
            response = tab.post(url=url,
                                show_errmsg=True,
                                params=params,  # URL 请求参数
                                data=data,
                                files=files,
                                cookies=cookies,
                                allow_redirects=allow_redirects,
                                json=json,
                                proxies=proxy,
                                verify=verify_ssl,
                                headers=headers
                                )
        else:  # 默认是 GET
            response = tab.get(url=url,
                               show_errmsg=True,
                               params=params,  # URL 请求参数
                               data=data,
                               json=json,
                               files=files,
                               cookies=cookies,
                               allow_redirects=allow_redirects,
                               proxies=proxy,
                               verify=verify_ssl,
                               headers=headers
                               )
        # session 模式下才有
        status_code = response.status_code
    else:
        try:
            # 根据请求模式执行请求
            if method.upper() == 'POST':
                response_ok = tab.post(url=url,
                                    show_errmsg=True,)
            else:  # 默认是 GET
                response_ok = tab.get(url=url,
                                   show_errmsg=True,)
        except Exception as e:
            response_ok = False
            if '状态码' in str(e):
                status_code = str(e).split("状态码： ")[1]
            else:
                raise

    # ----------------- 截图 -----------------------
    try:
        base64_str = tab.get_screenshot(as_base64=True, full_page=True)
    except Exception as e:
        base64_str = str(e)
    # ---------------- 页面信息 ---------------------
    # 获取页面信息
    tab_id = tab.tab_id  # 当前标签页的 ID
    title = tab.title   # 页面标题
    tab_url = tab.url   # 页面 URL
    user_agent = tab.user_agent   # User-Agent 信息
    status_code = status_code if status_code else '200' if response_ok else status_code
    # 超时和重试设置
    timeouts = tab.timeouts  # 超时设置
    retry_times = tab.retry_times  # 网络连接失败时的重试次数
    retry_interval = tab.retry_interval  # 重试等待间隔
    load_mode = tab.load_mode  # 页面加载策略

    # 获取响应信息
    try:
        response_html = tab.html  # 页面 HTML 文本
    except Exception:
        response_html = None

    try:
        response_json = tab.json  # 请求内容解析为 JSON
    except DrissionPage.errors.ElementNotFoundError:
        response_json = None

    return {
        "tab_id": tab_id,
        "title": title,
        "url": url,
        "tab_url": tab_url,
        "user_agent": user_agent,
        "method": method,
        "screenshot": base64_str,
        "status_code": status_code,
        "timeouts": timeouts,
        "retry_times": retry_times,
        "retry_interval": retry_interval,
        "load_mode": load_mode,
        "response_html": response_html,
        "response_json": response_json,
        "params": params,  # 添加请求参数
        "headers": headers,  # 添加请求头
        "data": data,  # 添加携带的数据
        "json": json,  # 添加发送的 JSON 数据
        "files": files,   # 添加上传的文件
        "proxy": proxy,  # 添加代理参数
        "verify_ssl": verify_ssl,  # 添加 SSL 验证参数
    }


def all_in_one():
    if 1 == 1:
        print("6LCB5ZWG55So6LCB5piv54uX77yM5ZOq5aSp6KaB5piv6KKr5oyC5ZK46bG85LqG77yM5Y2W5a625bCx5piv5aSn5YK754uX77yI5LiN5piv5Lit5Y2O55Sw5Zut54qsKQ==")
    else:
        print("5oGt5Zac5L2g5Y+R6LSi77yM56Wd5oKo5LuK5bm05Y+R5aSn6LSi")