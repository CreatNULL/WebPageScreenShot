import re
import logging
import requests
import urllib3
from typing import List
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 禁用安全请求警告


class ProxyError(Exception):  # 自定义异常, 代理错误
    pass


class ProxyFormatError(ProxyError):
    pass


class ProxyValueError(ProxyError):
    pass


def match_bypass_domain(domain: str, bypass_domains: List[str]) -> bool:
    """ 用作匹配过滤的域名, 匹配 domain 参数 指定的域名，是否被 bypass_domain 指定的规则列表匹配成功
    为过滤不需要代理的域名提过滤供支持

    Args:
        text (str): 要匹配的文本。
        patterns (List[str]): 正则表达式模式列表。

    Returns:
        bool: 如果匹配到任意模式返回 True，否则返回 False。
    """
    if not bypass_domains:
        bypass_domains = []


    # 解决语法不兼容问题:  nothing to repeat at position 0 *abc 是谷歌插件可以支持的
    # https://pythonjishu.com/dfmnotatvzgaksr/
    bypass_domains = [_.replace("*", '.*', 1) if _.strip().startswith("*") else _ for _ in bypass_domains]
    logging.debug(f"跳过的主机: {bypass_domains}")
    for pattern in bypass_domains:
        if re.findall(pattern, domain):
            return True
    return False


def __extract_url(url_str: str) -> dict:
    """ 正则提取输入的URL中的存在的 协议、账号、密码、域名、ip、端口、

    :param url_str: 代理 URL
    :return {
        'protocol': None,
        'username': None,
        'password': None,
        'host': None,
        'port': None
    } 或 None
    """

    # 正则表达式匹配
    ip_regex = re.compile(
        r'^(?P<protocol>\w{3,5}://)(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\:?(?P<port>0|[1-9][0-9]{0,4})?$'
    )

    domain_regex = re.compile(
        r'^(?P<protocol>\w{3,5}://)((?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+)\:?(?P<port>0|[1-9][0-9]{0,4})?$'
    )

    with_usr_pwd_regex = re.compile(
        r'^(?P<protocol>https?://)(?P<username>[\w\d_]*)?:(?P<password>[\w\d_]*)?@?(?P<host>(?:(?:\d{1,3}\.){3}\d{1,3}|[a-zA-Z0-9.-]+))(?:\:(?P<port>\d+))?$'
    )

    # 提取结果的字典
    components = {
        'protocol': None,
        'username': None,
        'password': None,
        'host': None,
        'port': None
    }

    # 匹配 IP 地址
    ip_match = ip_regex.match(url_str)
    if ip_match:
        components['protocol'] = ip_match.group('protocol')
        components['host'] = ip_match.group(2)  # 这是 IP
        components['port'] = ip_match.group('port')
        return components

    # 匹配域名
    domain_match = domain_regex.match(url_str)
    if domain_match:
        components['protocol'] = domain_match.group('protocol')
        components['host'] = domain_match.group(2)  # 这是域名
        components['port'] = domain_match.group('port')
        return components

    with_usr_pwd_match = with_usr_pwd_regex.match(url_str)
    if with_usr_pwd_match:
        components['protocol'] = with_usr_pwd_match.group('protocol')
        components['username'] = with_usr_pwd_match.group('username')
        components['password'] = with_usr_pwd_match.group('password')
        components['host'] = with_usr_pwd_match.group('host')  # 这是域名
        components['port'] = with_usr_pwd_match.group('port')
        return components

    # 如果都不匹配，返回 None


def verify_proxy(proxy_url: str, active: bool = True) -> tuple:
    """验证代理格式是否正确以及提供可选参数，是否验证存活

    Args:
        proxy_url (str): 代理的URL
        active (bool, optional): 是否验证代理存活. Defaults to True.

    Returns:
        tuple: 验证通过转为 request 格式的代理URL, 代理元数据
    """

    if not proxy_url:
        logging.error('未指定代理。')
        raise ValueError('No proxy specified.')

    if not isinstance(proxy_url, str):
        logging.error("指定的代理主机的参数类型错误")
        raise ValueError(f"parameter 'proxy_url': Wrong parameter type {type(proxy_url)}, the correct parameter type is <class 'str'>")

    # 代理的账号密码
    username = ''
    password = ''

    # url 格式验证
    logging.info('验证代理格式')
    if '@' in proxy_url:
        # 提取 username 和 password
        try:
            _ = proxy_url.split("://")
            if len(_) == 2:  # protocol://username:password@domain:port
                username, password = _[1].split("@")[0], _[1].split("@")[1]
                proxy_url = proxy_url.replace(f"{username}:{password}@", '')
            elif len(_) == 1:  # username:password@domain:port
                username, password = _[0].split("@")[0], _[0].split("@")[1]
                proxy_url = proxy_url.replace(f"{username}:{password}@", '')
            else:
                logging.error("代理格式错误")
                return {}
        except ValueError:
            logging.error("代理格式错误")
            return {}

    # 解析代理URL的组件
    extract_proxy = __extract_url(url_str=proxy_url)

    if extract_proxy is None:
        logging.error('代理格式错误')
        return {}
    else:
        # 重新拼接
        if username and password:
            verified_proxy_url = f"{extract_proxy['protocol']}{username}:{password}@{extract_proxy['host']}{':' + extract_proxy['port'] if extract_proxy['port'] else ''}"
        else:
            verified_proxy_url = f"{extract_proxy['protocol']}{extract_proxy['host']}{':' + extract_proxy['port'] if extract_proxy['port'] else ''}"

        # 验证代理协议
        if extract_proxy['protocol'] not in ['http://', 'https://']:
            logging.error('代理协议错误, 仅支持http 和 https。')
            return {}

        # 如果需要验证代理存活
        if active:
            logging.info('验证代理存活...')
            domestic_target_url = "https://www.baidu.com"
            abroad_target_url = "https://www.google.com/"

            proxies = {
                'http': verified_proxy_url,
                'https': verified_proxy_url,
            }

            try:
                logging.info('代理尝试请求百度...')
                domestic_response = requests.get(domestic_target_url, proxies=proxies, timeout=6, verify=False)

                if domestic_response.status_code != 200:
                    logging.info('代理请求百度失败, 尝试请求谷歌...')
                    abroad_response = requests.get(abroad_target_url, proxies=proxies, timeout=6, verify=False)
                    if abroad_response.status_code != 200:
                        logging.error('代理请求谷歌失败。')
                        return {}

                logging.info('代理存活!')
            except (requests.exceptions.ProxyError, requests.exceptions.ReadTimeout) as e:
                logging.error('代理请求失败！代理未存活！')
                return {}
            except Exception as e:
                logging.error('代理请求失败! ', exc_info=True)
                return {}

    return {'http': verified_proxy_url, 'https': verified_proxy_url}, extract_proxy


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    while True:
        proxy_url = input("输入代理URL: ")
        print(verify_proxy(proxy_url=proxy_url, active=False))

