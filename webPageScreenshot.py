# coding: utf-8
"""
许可证声明：
本项目仅允许个人使用，禁止任何基于本项目的修改后进行商业用途。
任何形式的商业使用都需获得作者的书面许可。

Author: CreateNULL
Date: 2024-10-5
Description: A simple web page screenshot tool.
Copyright (c) 2024 CreateNULL. All rights reserved.
Version: 1.0.0
"""
from module.run import main
import argparse
from DrissionPage import SessionPage, ChromiumPage
banner = r"""
 __        __         _       ____                           ____                                        ____    _               _   
 \ \      / /   ___  | |__   |  _ \    __ _    __ _    ___  / ___|    ___   _ __    ___    ___   _ __   / ___|  | |__     ___   | |_ 
  \ \ /\ / /   / _ \ | '_ \  | |_) |  / _` |  / _` |  / _ \ \___ \   / __| | '__|  / _ \  / _ \ | '_ \  \___ \  | '_ \   / _ \  | __|
   \ V  V /   |  __/ | |_) | |  __/  | (_| | | (_| | |  __/  ___) | | (__  | |    |  __/ |  __/ | | | |  ___) | | | | | | (_) | | |_ 
    \_/\_/     \___| |_.__/  |_|      \__,_|  \__, |  \___| |____/   \___| |_|     \___|  \___| |_| |_| |____/  |_| |_|  \___/   \__|
                                              |___/                                                                                  
                                                                                                                            
                                                                                                                            
                                                                                                                        -- By : CreatNULL


"""


def init_arguments():
    parser = argparse.ArgumentParser(
        description=r"""
    一个网页截图工具，支持 GET、POST (json/data/file)

        """,formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--url', type=str, action='append', default=[],
                        help='要打开的网址列表，多个网址以空格分隔')
    parser.add_argument('--file', type=str,
                        help='要打开的网址列表文件，一行一个')
    parser.add_argument('--method', type=str, choices=['GET', 'POST'], default='GET',
                        help="请求的方式，支持 'GET' 和 'POST'，默认为 'GET'。")
    parser.add_argument('--params', type=str, default=None,
                        help="URL 请求参数，以 JSON 字符串格式提供，例如: '{\"key\": \"value\"}'。")
    parser.add_argument('--data', type=str, default=None,
                        help="要携带的数据，可以是字符串或 JSON 格式。")
    parser.add_argument('--json', type=str, default=None,
                        help="要发送的 JSON 数据，以 JSON 字符串格式提供。")
    parser.add_argument('--files', type=str, default=None,
                        help="要上传的文件，以 JSON 字符串格式提供，例如: '{\"上传时候的file文件名称\": \"上传的文件路径\"}'。")
    parser.add_argument('--headers', action='append', default=[],
                        help="请求头，以字符串格式提供，例如: User-Agent: Demo-User-Agent。")
    parser.add_argument('--cookies', type=str, default=None,
                        help="要添加的 Cookie，以 JSON 字符串格式提供。")
    parser.add_argument('--del-cookies', action='store_true',
                        help="是否清除所有 Cookie，默认为 False。")
    # 超时
    parser.add_argument('--timeout', type=lambda s: tuple(map(int, s.split(','))), default=tuple([6, 8, 8]),
                        help="对于 d 模式下， 超时时间设置，默认为 [6,8,8]。"
                             "第一个值为默认超时时间，第二个值为页面加载超时时间，"
                             "第三个值为 JavaScript 运行超时时间，单位为秒。"
                             "对于 s 模式下，只读取第一个，"
                             "连接超时时间")
    parser.add_argument('--retry-times', type=int, default=0,
                        help="页面加载失败重试次数，默认为 0。")
    parser.add_argument('--retry-interval', type=float, default=2.0,
                        help="页面加载失败重试间隔，默认为 2 秒。")
    parser.add_argument('--allow-redirects', action='store_true', default=False,
                        help="是否允许重定向，默认为 True。")
    parser.add_argument('--ssl-cert', action='append', default=[],
                        help='需要加载的ssl证书')
    # 代理
    parser.add_argument('--proxy', type=str, default=None,
                            help='设置代理，例如: "http://127.0.0.1:8080"')
    parser.add_argument('--proxy-active', action='store_true',
                        help='是否关闭代理存活验证, 默认关闭')
    parser.add_argument('--proxy-bypass', action='append', default=[],
                        help='不代理的主机列表')
    # 浏览器配置
    parser.add_argument('--browser-path', type=str, default=None,
                        help='浏览器可执行文件的路径，默认为 None')
    parser.add_argument('--local-port', type=str, default=None,
                        help='浏览器端口，默认设置下，DrissionPage 会在 9222 端口创建浏览器，如果该端口下浏览器已经启动，则会接管使用。')
    parser.add_argument('--auto-port', type=bool, default=False,
                        help='是否自动寻找端口，可指定程序自动创建全新的浏览器')
    parser.add_argument('--download-path', type=str, default=None,
                        help='下载保存路径，默认为 None')
    parser.add_argument('--user-data-path', type=str, default='./User Data',
                        help='用户的配置路径，默认为 None')
    parser.add_argument('--no-sandbox', type=bool, default=True,
                        help='是否关闭沙盒模式，默认为 True')
    parser.add_argument('--no-headless', action='store_true',
                        help='是否关闭无头模式，默认为 False。')
    parser.add_argument('--incognito', type=bool, default=False,
                        help='是否启用无痕模式，默认为 False')
    parser.add_argument('--ignore-certificate-errors', type=bool, default=True,
                        help='是否忽略证书错误，默认为 True')
    parser.add_argument('--start-maximized', type=bool, default=True,
                        help='启动时是否最大化窗口，默认为 True')
    parser.add_argument('--extensions', action='append', default=[],
                        help='需要添加的浏览器扩展列表')
    parser.add_argument('--use-system-user-path', type=bool, default=False,
                        help='是否使用系统的用户配置文件路径，默认为 False')
    parser.add_argument('--set-arguments', type=str, action='append', default=[],
                        help='启动参数列表 (谷歌浏览器的)')
    parser.add_argument('--remove-arguments', type=str, action='append', default=[],
                        help='要移除的启动参数列表 (谷歌浏览器的)')
    parser.add_argument('--clear-arguments', type=bool, default=False,
                        help='是否清空已设置的参数，默认为 False')
    parser.add_argument('--config', type=str, default='',
                        help='配置文件')
    # 其他
    # 截屏
    parser.add_argument('--full-page', action='store_true', default=False,
                        help='完整截屏，即下拉滚动截屏，默认 False')
    parser.add_argument('--output-path', type=str, default='.',
                        help='html 结果文件输出路径')
    parser.add_argument("--threads",  type=int, default=5,)
    # 预留 - 这个第三方库的配置文件，没弄明白，反正怎么弄配置文件都不生效
    # parser.add_argument('--config-path', type=str, default='dp_configs.ini',
    #                     help='配置文件保存路径，默认是 dp_configs.ini')
    return parser.parse_args()


if __name__ == '__main__':
    print(banner)
    main(args=init_arguments())
