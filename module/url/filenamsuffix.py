# coding: utf-8
"""
    常见的文件后缀，如需添加，则在对应的地方添加即可，
    后续新增后，请运行当前脚本验证 !!!
"""

# 图片文件后缀列表
IMAGE_SUFFIXES = [
    '.jpg',         # JPEG 格式，常用于数码照片，支持有损压缩
    '.jpeg',        # 同 .jpg，常用于高质量图片
    '.png',         # 便携式网络图形格式，支持无损压缩和透明度
    '.gif',         # 图形交换格式，支持动画和256色
    '.bmp',         # 位图格式，常用于 Windows 系统的图像
    '.tiff',        # 标签图像文件格式，常用于专业图像处理
    '.tif',         # TIFF 格式，通常用于高质量图像存储
    '.svg',         # 可缩放矢量图形，常用于网页图形
    '.webp',        # Google 开发的图像格式，支持有损和无损压缩
    '.heif',        # 高效图像文件格式，常用于 Apple 设备
    '.ico',         # 图标文件格式，通常用于网页图标
    '.exif'         # 嵌入于图像文件中的元数据，存储拍摄信息
]

# 音频文件后缀列表
AUDIO_SUFFIXES = [
    '.wav',         # 波形音频文件格式，常用于无损音频
    '.ape',         # APE (Monkey's Audio) 无损压缩音频格式
    '.mid',         # MIDI 音乐文件，用于音乐编排
    '.m4a',         # MPEG-4 音频文件，常用于 iTunes 和 Apple Music
    '.wma',         # Windows Media Audio 格式，微软的音频格式
    '.mp3',         # 常见的有损音频格式，广泛用于音乐存储
    '.flac',        # 自由无损音频编码格式，保留音质
    '.ogg',         # Ogg Vorbis 音频格式，开放格式
    '.aac',         # 高级音频编码格式，通常用于流媒体
    '.ra',          # RealAudio 格式，曾广泛用于网络音频流
    '.midi',        # MIDI 音乐文件格式，用于乐器演奏
    '.amr',         # 自适应动态范围音频压缩格式，主要用于语音
    '.opus',        # Opus 音频编码，专为语音和音乐流设计
    '.aiff'        # 音频交换文件格式，通常用于 Apple 设备
]

# 视频文件后缀列表
VIDEO_SUFFIXES = [
    '.3gp',    # 3GPP 视频格式，常用于移动设备
    '.mkv',    # Matroska 视频格式，支持多音轨和字幕
    '.flv',    # Flash 视频格式，主要用于在线视频流
    '.wmv',    # Windows Media Video 格式，由微软开发
    '.mp4',    # MPEG-4 视频格式，广泛使用，兼容性好
    '.avi',    # Audio Video Interleave 格式，较旧，支持多种编解码器
    '.mov',    # QuickTime 视频格式，苹果开发，支持高质量视频
    '.mpeg',   # 通用的视频格式，常用于DVD和视频流
    '.mpg',    # MPEG 视频格式，类似于 .mpeg，常用于视频播放
    '.webm',   # 网页视频格式，优化了流媒体播放
    '.f4v',    # Flash 视频格式，优化版，支持高质量视频
    '.m2ts',   # Blu-ray 电影格式，传输流格式
    '.ts',     # MPEG 传输流格式，常用于广播和流媒体
    '.3g2',    # 3GPP2 视频格式，适用于3G手机
    '.asf',    # Advanced Streaming Format，微软的流媒体格式
    '.vob',    # DVD 视频对象文件，存储在DVD上
    '.m4v',    # Apple 的 MPEG-4 视频格式，类似于 .mp4
    '.hevc',   # 高效视频编码（H.265），适用于高分辨率视频
    '.rm',     # RealMedia 格式，主要用于流媒体播放
    '.rmvb',   # RealMedia Variable Bitrate，流媒体格式，支持变码率
    '.h264',   # H.264 视频编码标准，广泛应用于高清视频压缩
    '.h265'    # H.265 视频编码标准，改进版的 H.264，支持更高压缩率
]


# 文档
# 文档文件后缀列表
DOCUMENT_SUFFIXES = [
    '.doc',        # Microsoft Word 文档格式
    '.docx',       # Microsoft Word 2007 及更新版本的文档格式
    '.odt',        # OpenDocument 文本格式，常用于 LibreOffice
    '.pdf',        # 便携文档格式，广泛用于文档共享
    '.pptx',       # Microsoft PowerPoint 演示文稿格式
    '.ppt',        # 旧版 Microsoft PowerPoint 演示文稿格式
    '.txt',        # 纯文本文件，常用于简单文本记录
    '.xls',        # Microsoft Excel 工作簿格式
    '.xlsx',       # Microsoft Excel 2007 及更新版本的工作簿格式
    '.rtf',        # 富文本格式，支持文本样式和格式
    '.tex',        # LaTeX 文档格式，常用于排版和学术论文
    '.env',        # 环境变量文件，常用于配置设置
    '.wps',        # WPS Office 文档格式
    '.properties',  # Java 属性文件格式，常用于配置
    '.json',       # JavaScript 对象表示法，常用于数据交换
    '.csv',        # 逗号分隔值文件，常用于数据表格
    '.xml',        # 可扩展标记语言，常用于数据存储和传输
    '.yaml',       # YAML 语言，常用于配置文件和数据序列化
    '.tar',        # Unix tar 文件格式，常用于打包多个文件
    '.tar.gz',     # tar 压缩文件，使用 gzip 压缩
    '.tar.bz2',    # tar 压缩文件，使用 bzip2 压缩
    '.zip',        # Zip 文件格式，广泛用于文件压缩
    '.7z',         # 7-Zip 文件格式，支持高压缩率
    '.bz2',        # bzip2 压缩文件格式
    '.gz',         # gzip 压缩文件格式
    '.lz',         # Lzip 压缩文件格式
    '.log',        # 日志文件，常用于记录程序运行信息
    '.pages',      # Apple Pages 文档格式
    '.dotx',       # Microsoft Word 模板格式
    '.htaccess',   # Apache 服务器的配置文件
    '.dockerfile', # Docker 配置文件，用于定义容器构建过程
    '.ini',        # 初始化文件格式，常用于配置设置
    '.class',      # Java 字节码文件，编译后的 Java 程序
    '.conf',       # 通用配置文件格式
    '.toml',       # TOML 文件格式，常用于配置设置
    '.mind',       # 思维导图文件格式
    '.xmind',      # XMind 思维导图格式
    # '.mm',         # FreeMind 思维导图文件格式
    '.drawio',     # Draw.io 文件格式
    '.whitesmith', # WhiteSmith 思维导图文件格式
]

# 脚本文件后缀列表
CODE_SUFFIXES = [
    '.cpp',        # C++ 源代码文件
    '.c',          # C 源代码文件
    '.java',       # Java 源代码文件
    '.rb',         # Ruby 源代码文件
    '.js',         # JavaScript 源代码文件
    '.bash',       # Bash 脚本文件
    '.go',         # Go 语言源代码文件
    '.hpp',        # C++ 头文件
    '.cs',         # C# 源代码文件
    '.tsx',        # TypeScript React 文件
    '.html',       # HTML 文件，用于构建网页
    '.htm',        # 旧版 HTML 文件扩展名
    # '.py',         # Python 源代码文件
    # '.sh',         # Shell 脚本文件
    # '.pl',         # Perl 脚本文件
    '.sql',        # SQL 脚本文件，用于数据库查询
    '.bat'         # Windows 批处理文件
]


# 其他
OTHER_SUFFIXES = [

]


FILE_SUFFIXES = IMAGE_SUFFIXES + AUDIO_SUFFIXES + VIDEO_SUFFIXES + DOCUMENT_SUFFIXES + CODE_SUFFIXES + OTHER_SUFFIXES


if __name__ == '__main__':
    import re

    # 检测后缀是否合法
    print("[*] 检测后缀格式: ")
    invalid_suffixes = []

    # 正则表达式用于匹配以点开头的后缀
    pattern = re.compile(r'^\.[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$')

    for suffix in FILE_SUFFIXES:
        if not pattern.match(suffix):
            invalid_suffixes.append(suffix)

    if invalid_suffixes:
        print("[!]", ', '.join(invalid_suffixes))
    else:
        print("[*] 后缀格式检测通过")
    print("-" * 10)

    # 检查重复项
    print("[*] 检测重复项: ")
    duplicates = set([x for x in FILE_SUFFIXES if FILE_SUFFIXES.count(x) > 1])
    if duplicates:
        print("[!] 重复的后缀:", duplicates)
    else:
        print("[*] 没有重复的后缀")
    print("-" * 10)

    # 判断是否有后缀名称和域名相同的
    print("[*] 检测文件后缀名 是否和域名冲突")
    from topdomain import TOP_DOMAIN
    t = ''
    for top_domain in TOP_DOMAIN:
        if top_domain['domain'] in FILE_SUFFIXES:
            t += top_domain['domain'] + ', '
    if t:
        print("[!] ", t)
    else:
        print("[*] 没有和域名冲突")
    print("-" * 10)
