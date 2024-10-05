#!bin/bash/env python3
# coding: utf-8
"""
    URL处理模块
"""
import re
import ipaddress
from urllib.parse import urlparse, urlunparse
from module.url.topdomain import TOP_DOMAIN   # 常见的顶级域名
from module.url.filenamsuffix import FILE_SUFFIXES  # 常见的文件后缀，且不和上面的这个域名有重复，故不怎么全


class ModifyURL:
    def __init__(self):
        # 协议对应的端口
        self.map_protocol_to_port = {
            r"http://": "80",
            r"https://": "443",
            r"ftp://": "21",
            r"ftps://": "990",  # FTP Secure
            r"sftp://": "22",   # Secure FTP
            r"ssh://": "22",
            r"smb://": "445",
            r"telnet://": "23",
            r"imap://": "143",
            r"imaps://": "993",
            r"pop://": "110",
            r"pops://": "995",
            r"ldap://": "389",
            r"ldaps://": "636",
            r"mqtt://": "1883",
            r"mqtts://": "8883",
            r"rtsp://": "554",
        }

        # 端口对应的协议
        self.map_port_to_protocol = {
            "80": r"http://",
            "443": r"https://",
            "21": r"ftp://",
            "990": r"ftps://",
            "22": r"sftp://",  # 也可以对应 SSH
            "445": r"smb://",
            "23": r"telnet://",
            "143": r"imap://",
            "993": r"imaps://",
            "110": r"pop://",
            "995": r"pops://",
            "389": r"ldap://",
            "636": r"ldaps://",
            "1883": r"mqtt://",
            "8883": r"mqtts://",
            "554": r"rtsp://",
        }

    def is_domain_strict_mode(self, domain: str) -> bool:
        """ 判断给出的字符串是否为合法的域名字符串, 不支持中文域名, 严格模式
        匹配示例:
            http://www.google.com False
            http://www.yahoo.com/ False
            http://www.yahoo.com:8080 False
            http://www.yahoo.com:8080/ False
            http://www.yahoo.com:8080/?index=1 False
            http://www.yahoo.com:8080/?index=0 False
            https://www.google.com False
            https://www.yahoo.com:8080/ False
            https://www.yahoo.com:8080/?index=1 False
            ftp://www.ftp.com False
            ftp://www.ftp.com:21 False
            ftp://127.0.0.1ftp://127.0.0.1:21 False
            ftp://127.0.0.1:21?index=1 False
            127.0.0.1 False
            127.0.0.1/query?index=1 False
            127.0.0.1:8080 False
            127.0.0.1:8080/ False
            127.0.0.1:8080/?index=1 False
            127.0.0.298 False
            127.0.0.298:8080 False
            www.baidu.com/url False
            www.baidu.com/query?name=小明 False
            www.baidu.com:8080 False
            www.baidu.com:8080/url False
            www.baidu.com:8080/url=我 False
            www.baidu.com True
            www.我.com False
            www.我 False
            www.1 False
            www.1. False
            www.1.c False
            wwww.1.cc True
            www.1.cc.com True
            wwww.1.ccwwww.1.cc. False

        :param domain: 需要验证的域名字符串
        """
        if type(domain) is not str:
            raise TypeError(f"传递的参数 'domain' 类型错误, 应当 <class 'str'>, 而不是 {type(domain)}.")

        # pattern = re.compile(r'^(www\.|wwww\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+\.[a-zA-Z]{2,13}$')
        # pattern = re.compile(r'^(www\.|wwww\.)?[a-zA-Z0-9-]{0,}(\.[a-zA-Z0-9-]+){0,}\.[a-zA-Z]{2,13}$')  # 匹配了 www 这样的，本意是想要匹配 localhost
        pattern = re.compile(r'^(?:localhost|(?:www\.|wwww\.)?[a-zA-Z0-9-]{0,}(\.[a-zA-Z0-9-]+){0,}\.[a-zA-Z]{2,13})$')

        if domain == 'localhost':
            return True
        # 匹配到了，那再判断顶级域名是否合法
        if pattern.match(domain):
            # 正则表达式匹配顶级域名
            pattern = r'\.[a-zA-Z]{2,}$'
            match = re.search(pattern, domain)
            top_domain = match.group(0) if match else None
            if ModifyURL.is_tld_exists(top_domain):
                return True
            else:
                return False
        else:
            return False

    def is_domain_lenient_mode(self, domain: str) -> bool:
        """ 判断给出的字符串是否为合法的域名字符, 不支持中文, 允许携带端口、路径、参数

        :param domain: 需要验证的域名字符串
        """

        if type(domain) is not str:
            raise TypeError(f"传递的参数 'domain' 类型错误, 应当 <class 'str'>, 而不是 {type(domain)}.")

        # 对于 localhost 直接算果, 验证端口范围
        if bool(re.match(r'^localhost(?::(?!0)(?:(?:6553[0-5]|655[0-2][0-9]|64[0-9]{3}|[1-5]?[0-9]{1,4}))(\/[^ \n]*)?)?$', domain)):
            return True

        # 对于其他的域名
        pattern = re.compile(
            r'^(?:www\.)?(?:(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6})(?::(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5]?[0-9]{1,4}))?(?:\/[^\s]*)?$'
        )

        if pattern.match(domain):
            # 排除常见的文件后缀, 例如 1.jpg
            suffix = self.__extract_top_domain(url=domain)
            if suffix:
                # 是否为文件后缀
                if suffix in FILE_SUFFIXES:
                    return False
                else:
                    # 是否为合法的域名
                    for t_domain in TOP_DOMAIN:
                        if t_domain['domain'] == suffix:
                            return True
                    return False
            else:
                return False
        else:
            return False

    @staticmethod
    def is_ip_address_strict_mode(ip: str) -> bool:
        """ 通过 ipaddress库验证是否是ip格式

        :param ip: 需要判断的ip地址字符串
        :return: True or False
        """
        if type(ip) is not str:
            raise TypeError(f"传递的参数 'ip' 类型错误, 应当 <class 'str'>, 而不是 {type(ip)}.")

        if not ip:
            return False
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_ip_address_lenient_mode(ip: str) -> bool:
        """ 通过正则判断是否为 ip , 宽容模式, 允许携带端口、路径、参数

        :param ip: 需要判断的ip地址字符串
        :return: True or False
        """

        pattern = re.compile(
            r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?::(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5]?[0-9]{1,4}))?(?:\/[^?]*)?(?:\/.*)?$'
        )

        match = pattern.match(ip)
        if not match:
            return False

        # 确保端口范围合法
        port = match.group(1)
        if port and (int(port) < 1 or int(port) > 65535):
            return False

        return True

    def is_url(self, url: str) -> bool:
        """ 判断是否为合法的 URL， 判断的依据为是否以协议开头，以及后续是否符合正则规则

        :param url:
        :return:
        """

        # 获取支持判断的协议
        for protocol, port in self.map_protocol_to_port.items():
            if url.startswith(protocol):
                # 进一步通过正则来判断，正则的协议为 protocol
                protocol_len = len(protocol)
                if len(url) <= protocol_len:  # 字符串的长度小于 URL 长度绝对不是url
                    continue
                else:
                    # 提取协议后半部分
                    domain_or_ip_with_other = url[protocol_len:]
                    # 判断
                    if self.is_domain_lenient_mode(domain=domain_or_ip_with_other) or self.is_ip_address_lenient_mode(
                            ip=domain_or_ip_with_other):
                        return True
                    else:
                        continue
            else:
                # 尚未匹配到协议
                continue

        # 遍历协议一遍，符合开头，但是后续部分不符合
        return False

    # 对 GUI 开放的接口
    # 过滤
    def filter(self, urls: list, original_order: bool = True, no_empty: bool = False, deduplicate: bool = False) -> list:
        """

        :param urls: 需要过滤的 url 列表
        :param original_order 排序的模式， True, 按照原始顺序，然后分到对应行，False, 先分类，然后输出到对应的类型下
        :param no_empty: 是否去除空行
        :param deduplicate: 去重
        :return:
            [{
                "domain_strict": domain_strict_list,    # 域名严格模式，仅仅匹配域名
                "domain_lenient": domain_lenient_list,  # 域名宽松模式，匹配域名[端口]/[路径]/[参数]
                "ip_strict": ip_strict_list,    # 严格模式,仅仅 ip
                "ip_lenient": ip_lenient_list,  # ip 格式, ip[端口]/[路径]/[参数]
                "url": url,    # URL 严格模式, 仅仅 协议://域名|ip[端口]/[路径]/[参数]
                "other": "other_list",   # 其他未匹配
            }]
        """

        if type(urls) is not list:
            raise ValueError(f"参数 urls 类型错, 应当为 <class 'list'>, 而不是 {type(urls)}")

        # 过滤后的结果
        filtered_urls = {"domain_strict": [], "domain_lenient": [], "ip_strict": [], "ip_lenient": [], "url": [],
                         "other": []}
        original_order_list = []

        if deduplicate:
            urls = list(set(urls))

        if original_order:
            for url in urls:

                if no_empty:
                    if not url.strip():
                        continue
                tmp_filtered_urls = {"domain_strict": [], "domain_lenient": [], "ip_strict": [], "ip_lenient": [],
                                     "url": [], "other": []}
                if self.is_domain_strict_mode(domain=url):
                    tmp_filtered_urls["domain_strict"].append(url)
                    tmp_filtered_urls['domain_lenient'].append('')
                    tmp_filtered_urls['ip_lenient'].append('')
                    tmp_filtered_urls['ip_strict'].append('')
                    tmp_filtered_urls['url'].append('')
                    tmp_filtered_urls['other'].append('')
                elif self.is_ip_address_strict_mode(ip=url):
                    tmp_filtered_urls["domain_strict"].append('')
                    tmp_filtered_urls['domain_lenient'].append('')
                    tmp_filtered_urls['ip_lenient'].append('')
                    tmp_filtered_urls["ip_strict"].append(url)
                    tmp_filtered_urls['url'].append('')
                    tmp_filtered_urls['other'].append('')
                elif self.is_domain_lenient_mode(domain=url):
                    tmp_filtered_urls["domain_strict"].append('')
                    tmp_filtered_urls["domain_lenient"].append(url)
                    tmp_filtered_urls["ip_lenient"].append('')
                    tmp_filtered_urls["ip_strict"].append('')
                    tmp_filtered_urls['url'].append('')
                    tmp_filtered_urls['other'].append('')
                elif self.is_ip_address_lenient_mode(ip=url):
                    tmp_filtered_urls["domain_strict"].append('')
                    tmp_filtered_urls['domain_lenient'].append('')
                    tmp_filtered_urls["ip_lenient"].append(url)
                    tmp_filtered_urls["ip_strict"].append('')
                    tmp_filtered_urls['url'].append('')
                    tmp_filtered_urls['other'].append('')
                elif self.is_url(url):
                    tmp_filtered_urls["domain_strict"].append('')
                    tmp_filtered_urls['domain_lenient'].append('')
                    tmp_filtered_urls["ip_lenient"].append('')
                    tmp_filtered_urls["ip_strict"].append('')
                    tmp_filtered_urls["url"].append(url)
                    tmp_filtered_urls['other'].append('')
                else:
                    tmp_filtered_urls["domain_strict"].append('')
                    tmp_filtered_urls['domain_lenient'].append('')
                    tmp_filtered_urls["ip_lenient"].append('')
                    tmp_filtered_urls["ip_strict"].append('')
                    tmp_filtered_urls["url"].append('')
                    tmp_filtered_urls["other"].append(url)
                original_order_list.append(tmp_filtered_urls)
            return original_order_list
        else:
            for url in urls:
                if self.is_domain_strict_mode(domain=url):
                    filtered_urls["domain_strict"].append(url)
                elif self.is_ip_address_strict_mode(ip=url):
                    filtered_urls["ip_strict"].append(url)
                elif self.is_domain_lenient_mode(domain=url):
                    filtered_urls["domain_lenient"].append(url)
                elif self.is_ip_address_lenient_mode(ip=url):
                    filtered_urls["ip_lenient"].append(url)
                elif self.is_url(url):
                    filtered_urls["url"].append(url)
                else:
                    filtered_urls["other"].append(url)
            return [filtered_urls]

    # 删除引号
    @staticmethod
    def remove_quotation_marks(urls: list, no_empty: bool = False, deduplicate: bool = False) -> list:
        """ 删除 URL开头的单引号，双引号

        :param urls: 需要处理的 URLS 列表
        :param no_empty: 跳过为空的
        :param deduplicate: 去重
        :return: [{'original': 原始的字符串, 'derivative': 去除引号后的]
        """

        if type(urls) is not list:
            raise ValueError(f"参数 urls 类型错, 应当为 <class 'list'>, 而不是 {type(urls)}")

        if deduplicate:
            urls = list(set(urls))

        if no_empty:
            result = [{'original': url, 'derivative': url.strip("'").strip('"').strip("‘").strip("’").strip("“").strip("”")} for url in urls if url.strip()]
        else:
            result = [{'original': url, 'derivative': url.strip("'").strip('"').strip("‘").strip("’").strip("“").strip("”")} for url in urls]

        return result

    # 删除一行的空白区域 删除空白行(可选)
    @staticmethod
    def remove_blank_space(urls: list, remove_blank_line: bool = True, deduplicate: bool = False) -> list:
        """ 删除 URL 开头末尾的空格

        :param urls: 需要处理的 URLS 列表
        :param remove_blank_line: 对于空白行的处理，是否删除
        :param deduplicate: 去重
        :return: [{'original': 原始的字符串, 'derivative': 处理后删除空行，空格的字符串}]
        """
        result = []

        if type(urls) is not list:
            raise ValueError(f"参数 urls 类型错, 应当为 <class 'list'>, 而不是 {type(urls)}")

        if deduplicate:
            urls = list(set(urls))

        for url in urls:
            if url:
                # 有内容， 先除空再判断
                if url.strip():
                    # 删除左右为空
                    result.append({'original': url, 'derivative': url.strip()})
                else:
                    if remove_blank_line:
                        # result.append({'original': url, 'derivative': url.strip()})
                        continue
                    else:
                        result.append({'original': url, 'derivative': url})
            else:
                url = ''
                if remove_blank_line:
                    continue
                else:
                    result.append({'original': url, 'derivative': url})

        return result

    # 提取参数，对别的地方不一定通用，所以我设为私有
    def __extract_protocol(self, url):
        # 正则表达式匹配协议
        protocol_pattern = r'^(?:(\w+)://)'

        # 提取协议
        protocol_match = re.match(protocol_pattern, url)
        protocol = protocol_match.group(1) if protocol_match else None

        return protocol + "://" if protocol else None

    def __extract_domain(self, url):
        # 对于localhost
        if bool(re.match(r'^localhost(?::(?:(?:6553[0-5]|655[0-2][0-9]|64[0-9]{3}|[1-5]?[0-9]{0,4}))?)?(/.*)?$', url)):
            return 'localhost'

        # 正则表达式匹配完整域名（排除 IP 地址）
        pattern = r'^(?:https?://)?((?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:/|$)'
        match = re.search(pattern, url)

        if match:
            return match.group(1)
        return None

    def __extract_port(self, url):
        # 正则表达式匹配端口号
        # 正则表达式用于提取域名和端口，支持任意协议，并限制端口范围为 1-65535
        pattern = r'^(?:[a-zA-Z][a-zA-Z\d+\-.]*://)?([^:/\s]+)(?::(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5]?[0-9]{1,4}))?(?=[/\s]|$)'
        match = re.match(pattern, url)

        if match:
            domain = match.group(1)  # 提取域名
            port = match.group(2)     # 提取端口
            return port
        return ''

    def __extract_path_and_params(self, url):
        """ 利用正则提取 URL中请求的路径 和 参数, 仅限内部通过了URL判断，或 域名、ip宽容模式下的判断后使用 """
        # 正则表达式匹配路径和查询参数
        path_pattern = r'^(?:(\w+)://[^/]+)?(/[^?]*)'  # 匹配任意协议的路径部分
        param_pattern = r'([^&=]*)=([^&]*)'  # 匹配查询参数

        # 提取路径
        path_match = re.match(path_pattern, url)
        path = path_match.group(2) if path_match else ""

        # 提取查询参数
        params = {}
        query_string = re.search(r'\?(.*)', url)

        if query_string:
            for match in re.finditer(param_pattern, query_string.group(1)):
                key = match.group(1)
                value = match.group(2)
                params[key] = value

        return path, params

    def __extract_ip(self, ip):
        """ 提取 ip, 仅限内部通过了 IP 判断后使用 """

        if type(ip) is not str:
            raise TypeError(f"参数 'ip' 类型错误, 应当为 <class 'str'>, 而不是 {type(ip)}")

        # 正则表达式匹配 IP 地址
        ip_pattern = r'^(?:(\w+)://)?((?:\d{1,3}\.){3}\d{1,3})(?::\d+)?'

        # 提取 IP 地址
        ip_match = re.match(ip_pattern, ip)
        ip = ip_match.group(2) if ip_match else None

        # 验证 IP 地址是否合法
        if ip and all(0 <= int(part) <= 255 for part in ip.split('.')):
            return ip
        return None

    def __extract_top_domain(self, url) -> str:
        """ 提取顶级域名, 仅仅适用于内部, 需要通过过判断是否为域名URL的情况下使用, 所以设置为私有

        :param url:  需要提取的 URL / domain
        :return: str 返回匹配到的
        """
        if not url:
            return ''

        if type(url) is not str:
            raise TypeError(f"参数 'url' 类型错误, 应当为 <class 'str'>, 而不是 {type(url)}")

        # 正则表达式匹配顶级域名
        match = re.search(r'\.(\w+)(?=[:\/]|$)', url)

        return f".{match.group(1)}" if match else ''

    @staticmethod
    def is_tld_exists(target_tld):
        """ 判断提供的是否是已知的合法顶级域名 例如 .com """

        # 创建一个集合以提高查找效率
        tld_set = {tld['domain'] for tld in TOP_DOMAIN}
        return target_tld in tld_set

    def extract_infos(self, urls: list, no_empty: bool = False, deduplicate: bool = False) -> [dict]:
        """ 从给出的列表字符串中提取可能的端口, 返回字典列表, 字典内容为 原始的字符串，提取的协议, 提取的域名, 提取的 ip, 提取的端口, 提取的参数和路径, 是否提取了东西

        :param urls:
        :param no_empty: 跳过为空的
        :param deduplicate: 去重
        :returns: [{'original': '原始的字符串', 'protocol': '', 'domain': '', 'ip':'', 'port':'', 'path': '', 'params': {}, 'is_other': True}]
        """

        result = []

        if type(urls) is not list:
            raise ValueError(f"参数 urls 类型错, 应当为 <class 'list'>, 而不是 {type(urls)}")

        if deduplicate:
            urls = list(set(urls))

        for url in urls:
            if no_empty:
                if not url.strip():
                    continue
            # 匹配为 域名
            if self.is_domain_strict_mode(domain=url):
                result.append(
                    {'original': url, 'protocol': '', 'domain': url, 'ip': '', 'port': '', 'path': '', 'params': '', 'is_other': False})
            # 匹配为 ip
            elif self.is_ip_address_strict_mode(ip=url):
                result.append(
                    {'original': url, 'protocol': '', 'domain': '', 'ip': url, 'port': '', 'path': '', 'params': '', 'is_other': False})
            # 匹配为 域名 + 其他
            elif self.is_domain_lenient_mode(domain=url):
                protocol = self.__extract_protocol(url=url)
                protocol = protocol if protocol else ''
                domain = self.__extract_domain(url=url)
                domain = domain if domain else ''
                port = self.__extract_port(url=url)
                port = port if port else ''
                path, params = self.__extract_path_and_params(url=url)
                path = path if path else ''
                result.append(
                    {'original': url, 'protocol': protocol, 'domain': domain, 'ip': '', 'port': port, 'path': path,
                     'params': params, 'is_other': False})
            # 匹配为 ip + 其他
            elif self.is_ip_address_lenient_mode(ip=url):
                protocol = self.__extract_protocol(url=url)
                protocol = protocol if protocol else ''
                ip = self.__extract_ip(ip=url)
                ip = ip if ip else ''
                port = self.__extract_port(url=url)
                port = port if port else ''
                path, params = self.__extract_path_and_params(url=url)
                path = path if path else ''
                params = params if params else ''
                result.append(
                    {'original': url, 'protocol': protocol, 'domain': '', 'ip': ip, 'port': port, 'path': path,
                     'params': params, 'is_other': False})
            # 匹配为 url
            elif self.is_url(url):
                protocol = self.__extract_protocol(url=url)
                protocol = protocol if protocol else ''
                domain = self.__extract_domain(url=url)
                domain = domain if domain else ''
                ip = self.__extract_ip(ip=url)
                ip = ip if ip else ''
                port = self.__extract_port(url=url)
                port = port if port else ''
                path, params = self.__extract_path_and_params(url=url)
                path = path if path else ''
                params = params if params else ''
                result.append(
                    {'original': url, 'protocol': protocol, 'domain': domain, 'ip': ip, 'port': port, 'path': path,
                     'params': params, 'is_other': False})
            # 都不是
            else:
                result.append(
                    {'original': url, 'protocol': '', 'domain': '', 'ip': '', 'port': '', 'path': '', 'params': '', 'is_other': True})

        return result

    def add_port(self, urls: list, no_empty: bool = False, deduplicate: bool = False) -> list:
        """ 添加端口, 返回字典列表 [{'original': 原始的字符串, 'derivative': 处理后添加端口的字符串}]

        :param urls:
        :param no_empty: 跳过为空的
        :param deduplicate: 去重
        :return: [{'original': 原始的字符串, 'derivative': 处理后添加端口的字符串}]
        """

        if deduplicate:
            urls = list(set(urls))

        result = []
        default_add = ':80'

        for url in urls:
            if no_empty:
                if not url.strip():
                    continue
            # 仅仅是域名
            if self.is_domain_strict_mode(domain=url):
                result.append({'original': url, 'derivative': url + default_add})
            # 仅仅是 ip
            elif self.is_ip_address_strict_mode(ip=url):
                result.append({'original': url, 'derivative': url + default_add})
            # 域名 宽容模式
            elif self.is_domain_lenient_mode(domain=url):
                # 已经有了端口，不添加
                if self.__extract_port(url=url):
                    result.append({'original': url, 'derivative': url})
                # 没有，添加
                else:
                    # 如果端口不存在，则添加
                    if ':' not in url:
                        url = url.replace('/', default_add + '/', 1)
                    # 如果端口已经存在，则跳过
                    else:
                        url = url
                    result.append({'original': url, 'derivative': url})
            # ip 同上面一样，其实不用添加
            elif self.is_ip_address_lenient_mode(ip=url):
                # 已经有了端口，不添加
                if self.__extract_port(url=url):
                    result.append({'original': url, 'derivative': url})
                # 没有，添加
                else:
                    # 如果端口不存在，则添加
                    if ':' not in url:
                        url = url.replace('/', default_add + '/', 1)
                    # 如果端口已经存在，则跳过
                    else:
                        url = url
                    result.append({'original': url, 'derivative': url})
            # 判断是否为 url
            elif self.is_url(url):
                # 提取协议
                protocol = self.__extract_protocol(url=url)
                # 如果存在协议，则依据协议和端口的映射关系选择端口，否则为 80
                # 不存在协议
                if not protocol:
                    # 如果端口不存在，则添加
                    if ':' not in url:
                        new_url = url.replace('/', default_add + '/', 1)
                    # 如果端口已经存在，则跳过
                    else:
                        new_url = url
                # 存在协议
                else:
                    # 存在端口
                    if self.__extract_port(url=url):
                        result.append({'original': url, 'derivative': url})
                        continue

                    # 不存在端口
                    try:
                        port = self.map_protocol_to_port[protocol.strip()]
                    except KeyError:
                        port = default_add.replace(":", '')

                    parsed_url = urlparse(url)

                    new_netloc = f"{parsed_url.hostname}:{port}" if parsed_url.hostname else parsed_url.netloc
                    new_url = urlunparse(parsed_url._replace(netloc=new_netloc))

                result.append({'original': url, 'derivative': new_url})
            else:
                result.append({'original': url, 'derivative': url})

        return result

    def add_protocol(self, urls: list, no_empty: bool = False, deduplicate: bool = False) -> list:
        """ 添加协议, 返回字典列表 [{'original': 原始的字符串, 'derivative': 处理后添加协议的字符串}] """

        result = []
        default_protocol = 'http://'

        if deduplicate:
            urls = list(set(urls))

        for url in urls:
            if no_empty:
                if not url.strip():
                    continue
            # 仅仅是域名
            if self.is_domain_strict_mode(domain=url):
                result.append({'original': url, 'derivative': default_protocol + url})
            # 仅仅是 IP
            elif self.is_ip_address_strict_mode(ip=url):
                result.append({'original': url, 'derivative': default_protocol + url})
            # 域名
            elif self.is_domain_lenient_mode(domain=url):
                # 已经有了协议，不添加
                if self.__extract_protocol(url=url):
                    result.append({'original': url, 'derivative': url})
                else:
                    # 提取端口
                    port = self.__extract_port(url=url)
                    # 存在端口，则依据端口添加
                    if port:
                        # 依据端口和协议的映射，进行添加
                        try:
                            protocol = self.map_port_to_protocol[port]
                        except KeyError:
                            protocol = default_protocol
                        result.append({'original': url, 'derivative': f"{protocol}{url}"})
                    # 不存在端口，使用默认的
                    else:
                        result.append({'original': url, 'derivative': default_protocol + url})

            # IP 同上面域名相似
            elif self.is_ip_address_lenient_mode(ip=url):
                # 已经有了协议，不添加
                if self.__extract_protocol(url=url):
                    result.append({'original': url, 'derivative': url})
                else:
                    # 提取端口
                    port = self.__extract_port(url=url)
                    # 存在端口，则依据端口添加
                    if port:
                        # 依据端口和协议的映射，进行添加
                        try:
                            protocol = self.map_port_to_protocol[port]
                        except KeyError:
                            protocol = default_protocol
                        result.append({'original': url, 'derivative': f"{protocol}{url}"})
                    # 不存在端口，使用默认的
                    else:
                        result.append({'original': url, 'derivative': default_protocol + url})
            # 都不是
            else:
                result.append({'original': url, 'derivative': url})

        return result


if __name__ == '__main__':
    URL = ModifyURL()
    while True:
        msg = input("输入验证的: ")
        print("是否为域名: ", end='')
        print("strict-> ", end='')
        print(URL.is_domain_strict_mode(domain=msg), end=' ')
        print("lenient-> ", end='')
        print(URL.is_domain_lenient_mode(domain=msg))
        print("是否为IP: ", end='')
        print("strict-> ", end='')
        print(URL.is_ip_address_strict_mode(ip=msg), end=' ')
        print("lenient-> ", end='')
        print(URL.is_ip_address_lenient_mode(ip=msg))
        print("是否为URL: ", end='')
        print(URL.is_url(url=msg))
