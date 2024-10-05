""" 初始化浏览器配置模块，返回 配置选项对象
"""
import os
import logging
from DrissionPage import Chromium, ChromiumOptions
from typing import Union
# from DrissionPage.common import configs_to_here  # 如果没有配置文件，则复制配置文件到指定的路径 # 预留


def init_browser(config_path: str = 'dp_configs.ini',
                 browser_path: str = None,    # 指定浏览器路径
                 local_port: str = None,  # 浏览器端口
                 auto_port: bool = True,  # 自动寻找端口
                 download_path: str = None, # 下载保存路径, 默认 .
                 user_data_path: str = None, # 用户的配置路径
                 no_sandbox: bool = True,    # 关闭沙盒
                 headless: bool = True,  # 无头模式
                 incognito: bool = False,    # 无痕模式启动浏览器
                 ignore_certificate_errors: bool = True, # 忽略证书错误
                 start_maximized: bool = True,   # 最大化窗口
                 extensions: list = None,  # 需要添加的浏览器扩展
                 use_system_user_path: bool = False,  # 是否使用系统的的用户配置文件路径
                 retry_times: int = 0, # 失败重试次数
                 retry_interval: float = 2, # 失败重试间隔
                 time_out: tuple = (10, 30, 30),  # 超时设置（默认超时时间，用于元素等待、alert 等待、WebPage的 s 模式连接等等，除以下两个参数的场景，都使用这个设置, 页面加载超时时间, JavaScript 运行超时时间)
                 set_arguments: list = None,  # Chromium 内核浏览器有一系列的启动配置，以--开头，可在浏览器创建时传入，控制浏览器行为和初始状态。https://peter.sh/experiments/chromium-command-line-switches/
                 remove_arguments: list = None,  # 此方法用于设置启动参数。
                 clear_arguments: bool = False,   # 此方法用于清空已设置的arguments参数
                 save_config: bool = False,
                 ssl_cert: list = None, # 需要加载的证书
                 ):   # 保存配置到配置文件
    r"""创建并配置Chromium浏览器选项。返回创建后的对象，以及配置

    Args:
        config_path (str): 配置文件保存路径，默认是 'dp_configs.ini'。
        browser_path (str): 浏览器可执行文件的路径，默认为 None。
        local_port (str): 浏览器端口，默认为 None。
        auto_port (bool): 是否自动寻找端口，默认为 True。
        download_path (str): 下载保存路径，默认为 None。
        user_data_path (str): 用户的配置路径, 默认为 None。
        no_sandbox (bool): 是否关闭沙盒模式，默认为 True。
        headless (bool): 是否启用无头模式，默认为 True。
        incognito (bool): 是否启用无痕模式，默认为 False。
        ignore_certificate_errors (bool): 是否忽略证书错误，默认为 True。
        start_maximized (bool): 启动时是否最大化窗口，默认为 True。
        extensions (list): 需要添加的浏览器扩展列表，默认为 None。
        use_system_user_path (bool): 是否使用系统的用户配置文件路径，默认为 False。
        retry_times (int): 失败重试次数，默认为 0。
        retry_interval (float): 失败重试间隔，默认为 2。
        time_out (tuple): 超时设置，默认 (10, 30, 30)，分别为元素等待、页面加载和 JavaScript 运行超时时间。
        set_arguments (list): 启动参数列表，默认为 None。
        remove_arguments (list): 要移除的启动参数列表，默认为 None。
        clear_arguments (bool): 是否清空已设置的参数，默认为 False。
        save_config (bool): 是否将配置保存到文件，默认为 False。
        :param headers: 添加头部，如果存在覆盖

    Returns:
        Tuple[ChromiumOptions, dict]: 返回配置好的 ChromiumOptions 对象和相关设置的信息字典。
    """

    logging.info("初始化浏览器配置, 验证参数...")
    # 参数验证
    if not isinstance(config_path, str):
        raise ValueError("config_path must be a string.")
    if browser_path and not isinstance(browser_path, str):
        raise ValueError("browser_path must be a string or None.")
    if local_port and not isinstance(local_port, str):
        raise ValueError("local_port must be a string or None.")
    if download_path and not isinstance(download_path, str):
        raise ValueError("download_path must be a string or None.")
    if user_data_path and not isinstance(user_data_path, str):
        raise ValueError("user_data_path must be a string or None.")
    if extensions and not isinstance(extensions, list):
        raise ValueError("extensions must be a list or None.")
    if set_arguments and not isinstance(set_arguments, list):
        raise ValueError("set_arguments must be a list or None.")
    if remove_arguments and not isinstance(remove_arguments, list):
        raise ValueError("remove_arguments must be a list or None.")
    if not isinstance(no_sandbox, bool):
        raise ValueError("no_sandbox must be a boolean.")
    if not isinstance(headless, bool):
        raise ValueError("headless must be a boolean.")
    if not isinstance(incognito, bool):
        raise ValueError("incognito must be a boolean.")
    if not isinstance(ignore_certificate_errors, bool):
        raise ValueError("ignore_certificate_errors must be a boolean.")
    if not isinstance(start_maximized, bool):
        raise ValueError("start_maximized must be a boolean.")
    if not isinstance(retry_times, int):
        raise ValueError("retry_times must be an integer.")
    if not isinstance(retry_interval, (int, float)):
        raise ValueError("retry_interval must be an integer or float.")
    if not isinstance(time_out, tuple) or len(time_out) != 3 or not all(isinstance(t, (int, float)) for t in time_out):
        raise ValueError("time_out must be a tuple of three numbers (base, page_load, script).")
    if clear_arguments and not isinstance(clear_arguments, bool):
        raise ValueError("clear_arguments must be a boolean.")
    if save_config and not isinstance(save_config, bool):
        raise ValueError("save_config must be a boolean.")
    # 等待后续研究明白了再说
    # if not os.path.exists(config_path):
    #     logging.warning("指定的配置文件不存在，准备创建...")
    #     if input("是否创建 [Y/n]? ").upper() != "N":
    #         configs_to_here(config_path.replace('.ini', ''))
    #         config_path = os.path.abspath(config_path)
    #         logging.info("配置文件已创建。")
    #     else:
    #         logging.warning("不创建配置文件")
    #         config_path = None

    if browser_path and not os.path.exists(browser_path):
        raise ValueError("Browser path Not Fount !")

    # 配置浏览器选项...
    logging.info("正在配置浏览器选项...")

    if not browser_path:
        logging.info("未指定浏览器，使用系统自带")
        browser_path = None

    # 创建配置对象
    logging.info("创建配置对象...")
    logging.info("由于不知道为何原因无法使用配置文件中的配置，故，此处设置为不读取配置文件")
    logging.info("修改不适用配置文件")
    config_path = ""
    if config_path:
        logging.info("配置文件路径: %s", config_path)
        co = ChromiumOptions(ini_path=config_path, read_file=True).new_env()
    else:
        logging.info("不读取配置文件")
        co = ChromiumOptions(read_file=False).new_env()

    # 此方法用于清空已设置的arguments参数
    if clear_arguments:
        logging.info("清空已设置的参数")
        co.clear_arguments()

    # 此方法用于设置启动参数。
    if set_arguments:
        for arg in set_arguments:
            logging.info(f"添加配置 {arg}")
            co.set_argument(arg)

    # 固定配置
    logging.info("设置新版本的无头模式，以此支持无头模式下的插件使用,"
                 "禁用浏览器正在被自动化程序控制的提示, 不要阻止过时的插件, "
                 "规避滑块检测，"
                 "关闭安全策略 禁用浏览器的同源策略,"
                 " 允许运行不安全的内容, "
                 "禁止xss防护, "
                 "禁用缓存")
    co.set_argument('--headless=new')   # 无头模式, linux下如果系统不支持可视化不加这条会启动失败
    co.set_argument('--disable-infobars')   # 禁用浏览器正在被自动化程序控制的提示
    co.set_argument('--allow-outdated-plugins')   # 不要阻止过时的插件
    co.set_argument("--disable-blink-features=AutomationControlled")   # 规避滑块检测
    co.set_argument("--disable-web-security")   # 关闭安全策略 禁用浏览器的同源策略
    co.set_argument("--allow-running-insecure-content")  # 允许运行不安全的内容
    co.set_argument('--disable-xss-auditor')  # 禁止xss防护
    co.set_argument("--disable-cache")  # 禁用缓存

    # 添加证书
    if ssl_cert:
        logging.info("添加证书...")
        # 加载证书:
        for cert in ssl_cert:
            cert = str(cert)
            logging.info(f"加载证书: {cert}")
            # 证书路径存在
            if os.path.exists(cert):
                # 加载证书
                co.set_argument(f'--ssl-client-certificate={ssl_cert}')
            else:
                raise FileNotFoundError(f"ssl client certificate:  {ssl_cert} not found!")

    # 设置浏览器端口
    if auto_port:
        # 设置为True，自动寻找可用端口
        logging.info("设置为浏览器自动寻找端口")
        co.auto_port(auto_port)
        # 设置为None ，防止和 auto_port 冲突
        local_port = None

    # 设置用户文件夹
    if user_data_path:
        logging.info(f"使用用户文件夹: {user_data_path}")
        # 防止和 user_data_path 参数冲突
        use_system_user_path = False
        logging.info("禁止使用系统内的浏览器用户配置文件夹")

    # 页面加载失败重试次数
    if retry_times or retry_times ==0:
        logging.info(f"设置连接失败重试次数: {str(retry_times)}")
        co.set_retry(times=int(retry_times),)

    # 页面加载重试时间间隔
    if retry_interval or retry_interval == 0:
        logging.info(f"设置浏览器重试间隔: {str(retry_interval)}")
        co.set_retry(interval=float(retry_interval),)

    # 设置超时时间
    if time_out:
        logging.info("设置超时")
        if len(time_out) == 3:
            base = time_out[0] # 默认超时时间，用于元素等待、alert 等待、WebPage的 s 模式连接等等，除以下两个参数的场景，都使用这个设置
            page_load = time_out[1] # 页面加载超时时间
            script = time_out[2]  # JavaScript 运行超时时间
            co.set_timeouts(base=base, page_load=page_load, script=script)
            logging.info(f"设置默认超时时间:{base}, 夜间加载超时时间: {page_load}, JavaScript运行超时时间: {script}")
        else:
            raise ValueError("time_out 参数必须是一个元组, 且格式为: (base, page_load, script).")

    # 设置是否使用系统安装的浏览器默认用户文件夹
    co.use_system_user_path(on_off=use_system_user_path)

    logging.info(f"浏览器端口: {local_port}")
    # 设置各种路径信息
    co.set_paths(
        browser_path=browser_path,
        address=None,   # 肯定是使用本地
        local_port=local_port,
        download_path=download_path,
        user_data_path=user_data_path,
        cache_path=None,  # 缓存路径
    )

    # 启用无头模式
    if headless:
        logging.info("使用无头模式")
        co.headless()

    # 无沙盒模式
    if no_sandbox:
        logging.info("禁用沙盒")
        co.set_argument('--no-sandbox')

    # 启动时最大化
    if start_maximized:
        logging.info("启动时最大化")
        co.set_argument('--start-maximized')

    # 匿名模式
    if incognito:
        logging.info("匿名访问")
        co.incognito()

    # 移除配置对象中保存的所有插件路径。如需移除部分插件，请移除全部后再重新添加需要的插件
    co.remove_extensions()
    # 添加插件
    if extensions is not None:
        for extension in extensions:
            logging.info(f"添加插件: {extension}")
            co.add_extension(extension)

    # 忽略证书错误
    if ignore_certificate_errors:
        logging.info("忽略证书错误")
        co.ignore_certificate_errors()

    # 保存设置到文件
    if save_config:
        logging.info("保存此次配置到配置文件")
        co.save(path=config_path)

    # 此方法用于在启动配置中删除一个启动参数，只要传入参数名称即可，不需要传入值。
    if remove_arguments:
        for arg in remove_arguments:
            logging.info(f"删除配置 {arg}")
            co.remove_argument(arg)

    # 浏览器, 用户数据文件夹路径
    set_infos = {
        "address": co.address,    # 该属性为要控制的浏览器地址，格式为 ip:port，默认为'127.0.0.1:9222'。
        "browser_path": co.browser_path,      # 该属性返回浏览器可执行文件的路径
        "user_data_path": co.user_data_path,      # 该属性返回用户数据文件夹路径
        "temp_path": co.tmp_path,    # 该属性返回临时文件夹路径，可用于保存自动分配的用户文件夹路径。
        "download_path": co.download_path,    # 该属性返回默认下载路径文件路径
        "user": co.user,   # 该属性返回用户配置文件夹名称。
        "load_mode": co.load_mode,    # 该属性返回页面加载策略。有'normal'、'eager'、'none'三种
        "timeouts": co.timeouts,       # 该属性返回超时设置。包括三种：'base'、'page_load'、'script'。 类型：dict
        "retry_times": co.retry_times,     # 该属性返回连接失败时的重试次数。 类型：int
        "retry_interval": co.retry_interval,   # 该属性返回连接失败时的重试间隔（秒）。类型：float
        "proxy": co.proxy,    # 该属性返回 代理设置。
        "extensions": co.extensions,   # 该属性以list形式返回要加载的插件路径。类型：list
        "preferences": co.preferences,    # 该属性返回用户首选项配置 类型：dict
        "system_user_path": co.system_user_path,  # 该属性返回是否使用系统按照的浏览器的用户文件夹。类型：bool
        "is_existing_only": co.is_existing_only,  # 该属性返回是否仅使用已打开的浏览器 类型：bool
        "is_auto_port": co.is_auto_port,  # 该属性返回是否仅使用自动分配端口和用户文件夹路径。类型：bool
        "is_headless": co.is_headless,     # 该属性返回是否以无头模式启动浏览器。类型：bool
    }

    return co, set_infos


if __name__ == '__main__':
    co, infos = init_browser(config_path='dp_configs.ini', user_data_path='user_data', headless=True)
    browser = Chromium(addr_or_opts=co)
