# coding: utf-8
""" 配置文件初始化，日志的默认生成配置

"""
import configparser


def generate_config_ini(config_file: str):
    config = configparser.ConfigParser()

    # 在这里可以定义默认配置
    config['DEFAULT'] = {
        'url': [],
        'file': '',
        'method': 'GET',
        'output_path': '.',
        'threads': '5',
        'params': '',  # url 请求参数
        'headers': [],
        'headers_bypass': [],
        'data': str(None),   # 携带的数据
        'json': str(None),  # 要发送的 JSON 数据，会自动设置 Content-Type 为'application/json'
        'files': str(None),  # 上传的文件，可以是一个字典，其中键是文件名，值是文件对象或文件路径
        'proxy': str(None),
        'proxy_active': str(None),
        'proxy_bypass': [],
        'ssl_cert': [],
        'allow_redirects': 'True',
        'cookies': str(None),      #
        'del_cookies': 'False',
        'retry_times': '0',
        'retry_interval': '2.0',
        'timeout': '6, 8, 8',
        'browser_path': '',
        'local_port': '',
        'auto_port': 'False',
        'download_path': '',
        'user_data_path': './User Data',
        'no_sandbox': 'True',
        'no_headless': 'False',
        'incognito': 'False',
        'ignore_certificate_errors': 'True',
        'start_maximized': 'True',
        'extensions': [],
        'use_system_user_path': 'False',
        'set_arguments': [],
        'remove_arguments': [],
        'clear_arguments': 'False',
        # 'config_path': 'dp_configs.ini',
    }

    with open(config_file, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

    return config
