# coding: utf-8
"""
从不通过的渠道获取的顶级域名，基本涵盖了大部分的, 使用的话，导入 TOP_DOMAIN 即可，格式 [{'domain': ''}]
如果后续新增，请运行当前脚本验证是否有重复项目
"""
# 如果需要新的域名:
SELF_DOMAIN_LIST = [{"domain": ".jdm"}, {"domain": ".one"}, {"domain": ".moe"}]

# 维基页面的所有顶级域名
WIKI_TOPDOMAIN = [
    {
        "domain": ".com",
        "entity": "商業"
    },
    {
        "domain": ".org",
        "entity": "組織"
    },
    {
        "domain": ".net",
        "entity": "網絡"
    },
    {
        "domain": ".int",
        "entity": "国际组织"
    },
    {
        "domain": ".edu",
        "entity": "教育"
    },
    {
        "domain": ".gov",
        "entity": "美国国家和各州政府机构"
    },
    {
        "domain": ".mil",
        "entity": "美军"
    },
    {
        "domain": ".arpa",
        "entity": "“地址和路由参数区域”"
    },
    {
        "domain": ".ac",
        "entity": "阿森松岛（英国）"
    },
    {
        "domain": ".ad",
        "entity": "安道尔"
    },
    {
        "domain": ".ae",
        "entity": "阿联酋"
    },
    {
        "domain": ".af",
        "entity": "阿富汗"
    },
    {
        "domain": ".ag",
        "entity": "安地卡及巴布達"
    },
    {
        "domain": ".ai",
        "entity": "安圭拉（英国）"
    },
    {
        "domain": ".al",
        "entity": "阿尔巴尼亚"
    },
    {
        "domain": ".am",
        "entity": "亞美尼亞"
    },
    {
        "domain": ".ao",
        "entity": "安哥拉"
    },
    {
        "domain": ".aq",
        "entity": "南极洲"
    },
    {
        "domain": ".ar",
        "entity": "阿根廷"
    },
    {
        "domain": ".as",
        "entity": "美属萨摩亚（美国）"
    },
    {
        "domain": ".at",
        "entity": "奥地利"
    },
    {
        "domain": ".au",
        "entity": "澳大利亞"
    },
    {
        "domain": ".aw",
        "entity": "阿鲁巴（荷兰王国）"
    },
    {
        "domain": ".ax",
        "entity": "奥兰（芬兰）"
    },
    {
        "domain": ".az",
        "entity": "阿塞拜疆"
    },
    {
        "domain": ".ba",
        "entity": "波黑"
    },
    {
        "domain": ".bb",
        "entity": "巴巴多斯"
    },
    {
        "domain": ".bd",
        "entity": "孟加拉国"
    },
    {
        "domain": ".be",
        "entity": "比利时"
    },
    {
        "domain": ".bf",
        "entity": "布吉納法索"
    },
    {
        "domain": ".bg",
        "entity": "保加利亚"
    },
    {
        "domain": ".bh",
        "entity": "巴林"
    },
    {
        "domain": ".bi",
        "entity": "布隆迪"
    },
    {
        "domain": ".bj",
        "entity": "贝宁"
    },
    {
        "domain": ".bm",
        "entity": "百慕大（英国）"
    },
    {
        "domain": ".bn",
        "entity": "文莱"
    },
    {
        "domain": ".bo",
        "entity": "玻利维亚"
    },
    {
        "domain": ".br",
        "entity": "巴西"
    },
    {
        "domain": ".bs",
        "entity": "巴哈马"
    },
    {
        "domain": ".bt",
        "entity": "不丹"
    },
    {
        "domain": ".bw",
        "entity": "博茨瓦纳"
    },
    {
        "domain": ".by",
        "entity": "白俄羅斯"
    },
    {
        "domain": ".bz",
        "entity": "伯利兹"
    },
    {
        "domain": ".ca",
        "entity": "加拿大"
    },
    {
        "domain": ".cc",
        "entity": "科科斯（基林）群島（澳大利亚）"
    },
    {
        "domain": ".cd",
        "entity": "刚果民主共和国"
    },
    {
        "domain": ".cf",
        "entity": "中非"
    },
    {
        "domain": ".cg",
        "entity": "刚果共和国"
    },
    {
        "domain": ".ch",
        "entity": "瑞士"
    },
    {
        "domain": ".ci",
        "entity": "科特迪瓦"
    },
    {
        "domain": ".ck",
        "entity": "庫克群島"
    },
    {
        "domain": ".cl",
        "entity": "智利"
    },
    {
        "domain": ".cm",
        "entity": "喀麦隆"
    },
    {
        "domain": ".cn",
        "entity": "中华人民共和国"
    },
    {
        "domain": ".co",
        "entity": "哥伦比亚"
    },
    {
        "domain": ".cr",
        "entity": "哥斯达黎加"
    },
    {
        "domain": ".cu",
        "entity": "古巴"
    },
    {
        "domain": ".cv",
        "entity": "佛得角"
    },
    {
        "domain": ".cw",
        "entity": "库拉索（荷兰王国）"
    },
    {
        "domain": ".cx",
        "entity": "圣诞岛"
    },
    {
        "domain": ".cy",
        "entity": "賽普勒斯"
    },
    {
        "domain": ".cz",
        "entity": "捷克"
    },
    {
        "domain": ".de",
        "entity": "德国"
    },
    {
        "domain": ".dj",
        "entity": "吉布提"
    },
    {
        "domain": ".dk",
        "entity": "丹麦"
    },
    {
        "domain": ".dm",
        "entity": "多米尼克"
    },
    {
        "domain": ".do",
        "entity": "多米尼加"
    },
    {
        "domain": ".dz",
        "entity": "阿尔及利亚"
    },
    {
        "domain": ".ec",
        "entity": "厄瓜多尔"
    },
    {
        "domain": ".ee",
        "entity": "爱沙尼亚"
    },
    {
        "domain": ".eg",
        "entity": "埃及"
    },
    {
        "domain": ".er",
        "entity": "厄立特里亚"
    },
    {
        "domain": ".es",
        "entity": "西班牙"
    },
    {
        "domain": ".et",
        "entity": "衣索比亞"
    },
    {
        "domain": ".eu",
        "entity": "欧洲联盟"
    },
    {
        "domain": ".fi",
        "entity": "芬兰"
    },
    {
        "domain": ".fj",
        "entity": "斐济"
    },
    {
        "domain": ".fk",
        "entity": "福克蘭群島（英国）"
    },
    {
        "domain": ".fm",
        "entity": "密克羅尼西亞聯邦"
    },
    {
        "domain": ".fo",
        "entity": "法罗群岛（丹麦王国）"
    },
    {
        "domain": ".fr",
        "entity": "法國"
    },
    {
        "domain": ".ga",
        "entity": "加彭"
    },
    {
        "domain": ".gd",
        "entity": "格瑞那達"
    },
    {
        "domain": ".ge",
        "entity": "格鲁吉亚"
    },
    {
        "domain": ".gf",
        "entity": "法属圭亚那（法国）"
    },
    {
        "domain": ".gg",
        "entity": "根西（英国）"
    },
    {
        "domain": ".gh",
        "entity": "加纳"
    },
    {
        "domain": ".gi",
        "entity": "直布罗陀（英国）"
    },
    {
        "domain": ".gl",
        "entity": "格陵兰（丹麦王国）"
    },
    {
        "domain": ".gm",
        "entity": "冈比亚"
    },
    {
        "domain": ".gn",
        "entity": "几内亚"
    },
    {
        "domain": ".gp",
        "entity": "瓜德罗普（法国）"
    },
    {
        "domain": ".gq",
        "entity": "赤道几内亚"
    },
    {
        "domain": ".gr",
        "entity": "希腊"
    },
    {
        "domain": ".gs",
        "entity": "南乔治亚和南桑威奇群岛（英国）"
    },
    {
        "domain": ".gt",
        "entity": "危地马拉"
    },
    {
        "domain": ".gu",
        "entity": "關島（美国）"
    },
    {
        "domain": ".gw",
        "entity": "几内亚比绍"
    },
    {
        "domain": ".gy",
        "entity": "圭亚那"
    },
    {
        "domain": ".hk",
        "entity": "香港"
    },
    {
        "domain": ".hm",
        "entity": "赫德岛和麦克唐纳群岛"
    },
    {
        "domain": ".hn",
        "entity": "洪都拉斯"
    },
    {
        "domain": ".hr",
        "entity": "克罗地亚"
    },
    {
        "domain": ".ht",
        "entity": "海地"
    },
    {
        "domain": ".hu",
        "entity": "匈牙利"
    },
    {
        "domain": ".id",
        "entity": "印度尼西亞"
    },
    {
        "domain": ".ie",
        "entity": "愛爾蘭"
    },
    {
        "domain": ".il",
        "entity": "以色列"
    },
    {
        "domain": ".im",
        "entity": "马恩岛（英国）"
    },
    {
        "domain": ".in",
        "entity": "印度"
    },
    {
        "domain": ".io",
        "entity": "英屬印度洋領地（英国）"
    },
    {
        "domain": ".iq",
        "entity": "伊拉克"
    },
    {
        "domain": ".ir",
        "entity": "伊朗"
    },
    {
        "domain": ".is",
        "entity": "冰島"
    },
    {
        "domain": ".it",
        "entity": "義大利"
    },
    {
        "domain": ".je",
        "entity": "澤西（英国）"
    },
    {
        "domain": ".jm",
        "entity": "牙买加"
    },
    {
        "domain": ".jo",
        "entity": "约旦"
    },
    {
        "domain": ".jp",
        "entity": "日本"
    },
    {
        "domain": ".ke",
        "entity": "肯尼亚"
    },
    {
        "domain": ".kg",
        "entity": "吉尔吉斯斯坦"
    },
    {
        "domain": ".kh",
        "entity": "柬埔寨"
    },
    {
        "domain": ".ki",
        "entity": "基里巴斯"
    },
    {
        "domain": ".km",
        "entity": "科摩罗"
    },
    {
        "domain": ".kn",
        "entity": "圣基茨和尼维斯"
    },
    {
        "domain": ".kp",
        "entity": "朝鮮民主主義人民共和國"
    },
    {
        "domain": ".kr",
        "entity": "大韓民國"
    },
    {
        "domain": ".kw",
        "entity": "科威特"
    },
    {
        "domain": ".ky",
        "entity": "开曼群岛（英国）"
    },
    {
        "domain": ".kz",
        "entity": "哈萨克斯坦"
    },
    {
        "domain": ".la",
        "entity": "老挝"
    },
    {
        "domain": ".lb",
        "entity": "黎巴嫩"
    },
    {
        "domain": ".lc",
        "entity": "圣卢西亚"
    },
    {
        "domain": ".li",
        "entity": "列支敦斯登"
    },
    {
        "domain": ".lk",
        "entity": "斯里蘭卡"
    },
    {
        "domain": ".lr",
        "entity": "利比里亚"
    },
    {
        "domain": ".ls",
        "entity": "賴索托"
    },
    {
        "domain": ".lt",
        "entity": "立陶宛"
    },
    {
        "domain": ".lu",
        "entity": "盧森堡"
    },
    {
        "domain": ".lv",
        "entity": "拉脫維亞"
    },
    {
        "domain": ".ly",
        "entity": "利比亞"
    },
    {
        "domain": ".ma",
        "entity": "摩洛哥"
    },
    {
        "domain": ".mc",
        "entity": "摩納哥"
    },
    {
        "domain": ".md",
        "entity": "摩尔多瓦"
    },
    {
        "domain": ".me",
        "entity": "蒙特內哥羅"
    },
    {
        "domain": ".mg",
        "entity": "马达加斯加"
    },
    {
        "domain": ".mh",
        "entity": "马绍尔群岛"
    },
    {
        "domain": ".mk",
        "entity": "北馬其頓"
    },
    {
        "domain": ".ml",
        "entity": "马里"
    },
    {
        "domain": ".mm",
        "entity": "緬甸"
    },
    {
        "domain": ".mn",
        "entity": "蒙古国"
    },
    {
        "domain": ".mo",
        "entity": "澳門"
    },
    {
        "domain": ".mp",
        "entity": "北马里亚纳群岛（美国）"
    },
    {
        "domain": ".mq",
        "entity": "马提尼克（法国）"
    },
    {
        "domain": ".mr",
        "entity": "毛里塔尼亚"
    },
    {
        "domain": ".ms",
        "entity": "蒙特塞拉特（英国）"
    },
    {
        "domain": ".mt",
        "entity": "馬爾他"
    },
    {
        "domain": ".mu",
        "entity": "模里西斯"
    },
    {
        "domain": ".mv",
        "entity": "馬爾地夫"
    },
    {
        "domain": ".mw",
        "entity": "马拉维"
    },
    {
        "domain": ".mx",
        "entity": "墨西哥"
    },
    {
        "domain": ".my",
        "entity": "马来西亚"
    },
    {
        "domain": ".mz",
        "entity": "莫桑比克"
    },
    {
        "domain": ".na",
        "entity": "纳米比亚"
    },
    {
        "domain": ".nc",
        "entity": "新喀里多尼亞（法国）"
    },
    {
        "domain": ".ne",
        "entity": "尼日尔"
    },
    {
        "domain": ".nf",
        "entity": "诺福克岛"
    },
    {
        "domain": ".ng",
        "entity": "奈及利亞"
    },
    {
        "domain": ".ni",
        "entity": "尼加拉瓜"
    },
    {
        "domain": ".nl",
        "entity": "荷蘭"
    },
    {
        "domain": ".no",
        "entity": "挪威"
    },
    {
        "domain": ".np",
        "entity": "尼泊尔"
    },
    {
        "domain": ".nr",
        "entity": "瑙鲁"
    },
    {
        "domain": ".nu",
        "entity": "纽埃"
    },
    {
        "domain": ".nz",
        "entity": "新西兰"
    },
    {
        "domain": ".om",
        "entity": "阿曼"
    },
    {
        "domain": ".pa",
        "entity": "巴拿马"
    },
    {
        "domain": ".pe",
        "entity": "秘魯"
    },
    {
        "domain": ".pf",
        "entity": "法屬玻里尼西亞（法国）"
    },
    {
        "domain": ".pg",
        "entity": "巴布亚新几内亚"
    },
    {
        "domain": ".ph",
        "entity": "菲律賓"
    },
    {
        "domain": ".pk",
        "entity": "巴基斯坦"
    },
    {
        "domain": ".pl",
        "entity": "波蘭"
    },
    {
        "domain": ".pm",
        "entity": "圣皮埃尔和密克隆（法国）"
    },
    {
        "domain": ".pn",
        "entity": "皮特凯恩群岛（英国）"
    },
    {
        "domain": ".pr",
        "entity": "波多黎各（美国）"
    },
    {
        "domain": ".ps",
        "entity": "巴勒斯坦[29]"
    },
    {
        "domain": ".pt",
        "entity": "葡萄牙"
    },
    {
        "domain": ".pw",
        "entity": "帛琉"
    },
    {
        "domain": ".py",
        "entity": "巴拉圭"
    },
    {
        "domain": ".qa",
        "entity": "卡塔尔"
    },
    {
        "domain": ".re",
        "entity": "留尼汪（法国）"
    },
    {
        "domain": ".ro",
        "entity": "羅馬尼亞"
    },
    {
        "domain": ".rs",
        "entity": "塞爾維亞"
    },
    {
        "domain": ".ru",
        "entity": "俄羅斯"
    },
    {
        "domain": ".rw",
        "entity": "卢旺达"
    },
    {
        "domain": ".sa",
        "entity": "沙烏地阿拉伯"
    },
    {
        "domain": ".sb",
        "entity": "所罗门群岛"
    },
    {
        "domain": ".sc",
        "entity": "塞舌尔"
    },
    {
        "domain": ".sd",
        "entity": "苏丹"
    },
    {
        "domain": ".se",
        "entity": "瑞典"
    },
    {
        "domain": ".sg",
        "entity": "新加坡"
    },
    {
        "domain": ".sh",
        "entity": "聖赫勒拿（英国）"
    },
    {
        "domain": ".si",
        "entity": "斯洛維尼亞"
    },
    {
        "domain": ".sk",
        "entity": "斯洛伐克"
    },
    {
        "domain": ".sl",
        "entity": "塞拉利昂"
    },
    {
        "domain": ".sm",
        "entity": "圣马力诺"
    },
    {
        "domain": ".sn",
        "entity": "塞内加尔"
    },
    {
        "domain": ".so",
        "entity": "索马里"
    },
    {
        "domain": ".sr",
        "entity": "苏里南"
    },
    {
        "domain": ".ss",
        "entity": "南蘇丹"
    },
    {
        "domain": ".st",
        "entity": "聖多美和普林西比"
    },
    {
        "domain": ".su",
        "entity": "苏联"
    },
    {
        "domain": ".sv",
        "entity": "薩爾瓦多"
    },
    {
        "domain": ".sx",
        "entity": "荷屬聖馬丁（荷兰王国）"
    },
    {
        "domain": ".sy",
        "entity": "叙利亚"
    },
    {
        "domain": ".sz",
        "entity": "斯威士兰"
    },
    {
        "domain": ".tc",
        "entity": "特克斯和凯科斯群岛（英国）"
    },
    {
        "domain": ".td",
        "entity": "乍得"
    },
    {
        "domain": ".tf",
        "entity": "法属南部和南极领地"
    },
    {
        "domain": ".tg",
        "entity": "多哥"
    },
    {
        "domain": ".th",
        "entity": "泰國"
    },
    {
        "domain": ".tj",
        "entity": "塔吉克斯坦"
    },
    {
        "domain": ".tk",
        "entity": "托克勞"
    },
    {
        "domain": ".tl",
        "entity": "东帝汶"
    },
    {
        "domain": ".tm",
        "entity": "土库曼斯坦"
    },
    {
        "domain": ".tn",
        "entity": "突尼西亞"
    },
    {
        "domain": ".to",
        "entity": "汤加"
    },
    {
        "domain": ".tr",
        "entity": "土耳其"
    },
    {
        "domain": ".tt",
        "entity": "千里達及托巴哥"
    },
    {
        "domain": ".tv",
        "entity": "图瓦卢"
    },
    {
        "domain": ".tw",
        "entity": "臺灣"
    },
    {
        "domain": ".tz",
        "entity": "坦桑尼亚"
    },
    {
        "domain": ".ua",
        "entity": "烏克蘭"
    },
    {
        "domain": ".ug",
        "entity": "乌干达"
    },
    {
        "domain": ".uk",
        "entity": "英国"
    },
    {
        "domain": ".us",
        "entity": "美国"
    },
    {
        "domain": ".uy",
        "entity": "乌拉圭"
    },
    {
        "domain": ".uz",
        "entity": "乌兹别克斯坦"
    },
    {
        "domain": ".va",
        "entity": "梵蒂冈"
    },
    {
        "domain": ".vc",
        "entity": "圣文森特和格林纳丁斯"
    },
    {
        "domain": ".ve",
        "entity": "委內瑞拉"
    },
    {
        "domain": ".vg",
        "entity": "英屬維爾京群島（英国）"
    },
    {
        "domain": ".vi",
        "entity": "美屬維爾京群島（美国）"
    },
    {
        "domain": ".vn",
        "entity": "越南"
    },
    {
        "domain": ".vu",
        "entity": "瓦努阿圖"
    },
    {
        "domain": ".wf",
        "entity": "瓦利斯和富图纳"
    },
    {
        "domain": ".ws",
        "entity": "萨摩亚"
    },
    {
        "domain": ".ye",
        "entity": "葉門"
    },
    {
        "domain": ".yt",
        "entity": "马约特"
    },
    {
        "domain": ".za",
        "entity": "南非"
    },
    {
        "domain": ".zm",
        "entity": "尚比亞"
    },
    {
        "domain": ".zw",
        "entity": "辛巴威"
    },
    {
        "domain": "xn--lgbbat1ad8j",
        "entity": ".الجزائر"
    },
    {
        "domain": "xn--y9a3aq",
        "entity": ".հայ（英语：.հայ）"
    },
    {
        "domain": "xn--mgbcpq6gpa1a",
        "entity": ".البحرين"
    },
    {
        "domain": "xn--54b7fta0cc",
        "entity": ".বাংলা"
    },
    {
        "domain": "xn--90ais",
        "entity": ".бел"
    },
    {
        "domain": "xn--90ae",
        "entity": ".бг[43]"
    },
    {
        "domain": "xn--fiqs8s",
        "entity": ".中国"
    },
    {
        "domain": "xn--fiqz9s",
        "entity": ".中國"
    },
    {
        "domain": "xn--wgbh1c",
        "entity": ".مصر"
    },
    {
        "domain": "xn--e1a4c",
        "entity": ".ею"
    },
    {
        "domain": "xn--qxa6a",
        "entity": ".ευ"
    },
    {
        "domain": "xn--node",
        "entity": ".გე"
    },
    {
        "domain": "xn--qxam",
        "entity": ".ελ[43]"
    },
    {
        "domain": "xn--j6w193g",
        "entity": ".香港"
    },
    {
        "domain": "xn--h2brj9c",
        "entity": ".भारत"
    },
    {
        "domain": "xn--mgbbh1a71e",
        "entity": ".بھارت"
    },
    {
        "domain": "xn--fpcrj9c3d",
        "entity": ".భారత్"
    },
    {
        "domain": "xn--gecrj9c",
        "entity": ".ભારત"
    },
    {
        "domain": "xn--s9brj9c",
        "entity": ".ਭਾਰਤ"
    },
    {
        "domain": "xn--xkc2dl3a5ee0h",
        "entity": ".இந்தியா"
    },
    {
        "domain": "xn--45brj9c",
        "entity": ".ভারত"
    },
    {
        "domain": "xn--2scrj9c",
        "entity": ".ಭಾರತ"
    },
    {
        "domain": "xn--rvc1e0am3e",
        "entity": ".ഭാരതം"
    },
    {
        "domain": "xn--45br5cyl",
        "entity": ".ভাৰত"
    },
    {
        "domain": "xn--3hcrj9c",
        "entity": ".ଭାରତ"
    },
    {
        "domain": "xn--mgbbh1a",
        "entity": ".بارت"
    },
    {
        "domain": "xn--h2breg3eve",
        "entity": ".भारतम्"
    },
    {
        "domain": "xn--h2brj9c8c",
        "entity": ".भारोत"
    },
    {
        "domain": "xn--mgbgu82a",
        "entity": ".ڀارت"
    },
    {
        "domain": "xn--mgba3a4f16a",
        "entity": ".ایران"
    },
    {
        "domain": "xn--mgbtx2b",
        "entity": ".عراق"
    },
    {
        "domain": "xn--mgbayh7gpa",
        "entity": ".الاردن"
    },
    {
        "domain": "xn--80ao21a",
        "entity": ".қаз"
    },
    {
        "domain": "xn--q7ce6a",
        "entity": ".ລາວ"
    },
    {
        "domain": "xn--mix082f",
        "entity": ".澳门"
    },
    {
        "domain": "xn--mix891f",
        "entity": ".澳門"
    },
    {
        "domain": "xn--mgbx4cd0ab",
        "entity": ".مليسيا"
    },
    {
        "domain": "xn--mgbah1a3hjkrd",
        "entity": ".موريتانيا"
    },
    {
        "domain": "xn--l1acc",
        "entity": ".мон"
    },
    {
        "domain": "xn--mgbc0a9azcg",
        "entity": ".المغرب"
    },
    {
        "domain": "xn--d1alf",
        "entity": ".мкд"
    },
    {
        "domain": "xn--mgb9awbf",
        "entity": ".عمان"
    },
    {
        "domain": "xn--mgbai9azgqp6j",
        "entity": ".پاکستان"
    },
    {
        "domain": "xn--ygbi2ammx",
        "entity": ".فلسطين"
    },
    {
        "domain": "xn--wgbl6a",
        "entity": ".قطر"
    },
    {
        "domain": "xn--p1ai",
        "entity": ".рф"
    },
    {
        "domain": "xn--mgberp4a5d4ar",
        "entity": ".السعودية"
    },
    {
        "domain": "xn--90a3ac",
        "entity": ".срб"
    },
    {
        "domain": "xn--yfro4i67o",
        "entity": ".新加坡"
    },
    {
        "domain": "xn--clchc0ea0b2g2a9gcd",
        "entity": ".சிங்கப்பூர்"
    },
    {
        "domain": "xn--3e0b707e",
        "entity": ".한국"
    },
    {
        "domain": "xn--fzc2c9e2c",
        "entity": ".ලංකා"
    },
    {
        "domain": "xn--xkc2al3hye2a",
        "entity": ".இலங்கை"
    },
    {
        "domain": "xn--mgbpl2fh",
        "entity": ".سودان"
    },
    {
        "domain": "xn--ogbpf8fl",
        "entity": ".سورية"
    },
    {
        "domain": "xn--kprw13d",
        "entity": ".台湾"
    },
    {
        "domain": "xn--kpry57d",
        "entity": ".台灣"
    },
    {
        "domain": "xn--o3cw4h",
        "entity": ".ไทย"
    },
    {
        "domain": "xn--pgbs0dh",
        "entity": ".تونس"
    },
    {
        "domain": "xn--j1amh",
        "entity": ".укр"
    },
    {
        "domain": "xn--mgbaam7a8h",
        "entity": ".امارات"
    },
    {
        "domain": "xn--mgb2ddes",
        "entity": ".اليمن"
    },
    {
        "domain": ".academy",
        "entity": "学术机构"
    },
    {
        "domain": ".accountant",
        "entity": "会计及金融事务所"
    },
    {
        "domain": ".accountants",
        "entity": "会计及金融事务所"
    },
    {
        "domain": ".active",
        "entity": "通用"
    },
    {
        "domain": ".actor",
        "entity": "演员"
    },
    {
        "domain": ".ads",
        "entity": ""
    },
    {
        "domain": ".adult",
        "entity": "成人娱乐（色情）"
    },
    {
        "domain": ".aero",
        "entity": "航空运输工业"
    },
    {
        "domain": ".africa",
        "entity": ""
    },
    {
        "domain": ".agency",
        "entity": "商业协会"
    },
    {
        "domain": ".airforce",
        "entity": "防卫承包商"
    },
    {
        "domain": ".amazon",
        "entity": ""
    },
    {
        "domain": ".analytics",
        "entity": ""
    },
    {
        "domain": ".apartments",
        "entity": "公寓"
    },
    {
        "domain": ".app",
        "entity": "手机应用[49]"
    },
    {
        "domain": ".archi",
        "entity": "建筑师及建筑事务所[50]"
    },
    {
        "domain": ".army",
        "entity": "防卫承包商"
    },
    {
        "domain": ".art",
        "entity": "艺术家、博物馆、画廊、经销商、服务提供方和承包商"
    },
    {
        "domain": ".associates",
        "entity": "商业协会"
    },
    {
        "domain": ".attorney",
        "entity": "律师和法律组织"
    },
    {
        "domain": ".auction",
        "entity": ""
    },
    {
        "domain": ".audible",
        "entity": ""
    },
    {
        "domain": ".audio",
        "entity": "立体声/音频系统、音乐"
    },
    {
        "domain": ".author",
        "entity": ""
    },
    {
        "domain": ".auto",
        "entity": ""
    },
    {
        "domain": ".autos",
        "entity": ""
    },
    {
        "domain": ".aws",
        "entity": ""
    },
    {
        "domain": ".baby",
        "entity": ""
    },
    {
        "domain": ".band",
        "entity": ""
    },
    {
        "domain": ".bank",
        "entity": "银行"
    },
    {
        "domain": ".bar",
        "entity": "酒吧及相关行业"
    },
    {
        "domain": ".barefoot",
        "entity": ""
    },
    {
        "domain": ".bargains",
        "entity": "礼品券及网上销售"
    },
    {
        "domain": ".baseball",
        "entity": ""
    },
    {
        "domain": ".basketball",
        "entity": ""
    },
    {
        "domain": ".beauty",
        "entity": ""
    },
    {
        "domain": ".beer",
        "entity": "啤酒酿酒厂及爱好者"
    },
    {
        "domain": ".berlin",
        "entity": "与德国首都柏林相关的任何公司、品牌、个人和其他事物"
    },
    {
        "domain": ".best",
        "entity": ""
    },
    {
        "domain": ".bestbuy",
        "entity": ""
    },
    {
        "domain": ".bet",
        "entity": ""
    },
    {
        "domain": ".bible",
        "entity": ""
    },
    {
        "domain": ".bid",
        "entity": "拍卖"
    },
    {
        "domain": ".bike",
        "entity": "自行车"
    },
    {
        "domain": ".bingo",
        "entity": "美式宾果"
    },
    {
        "domain": ".bio",
        "entity": "有机农业[56]"
    },
    {
        "domain": ".biz",
        "entity": "商業"
    },
    {
        "domain": ".black",
        "entity": "任何喜欢黑发色的人[60]"
    },
    {
        "domain": ".blackfriday",
        "entity": "黑色星期五、零售业"
    },
    {
        "domain": ".blockbuster",
        "entity": ""
    },
    {
        "domain": ".blog",
        "entity": "博客"
    },
    {
        "domain": ".blue",
        "entity": "任何喜欢蓝发色的人[62]"
    },
    {
        "domain": ".boo",
        "entity": "—"
    },
    {
        "domain": ".book",
        "entity": ""
    },
    {
        "domain": ".boats",
        "entity": ""
    },
    {
        "domain": ".boots",
        "entity": ""
    },
    {
        "domain": ".bot",
        "entity": ""
    },
    {
        "domain": ".boutique",
        "entity": "专业业务"
    },
    {
        "domain": ".box",
        "entity": "个人和企业，以便推广个人云存储"
    },
    {
        "domain": ".broadway",
        "entity": ""
    },
    {
        "domain": ".broker",
        "entity": ""
    },
    {
        "domain": ".build",
        "entity": "建筑业"
    },
    {
        "domain": ".builders",
        "entity": "建筑工人"
    },
    {
        "domain": ".business",
        "entity": "商业"
    },
    {
        "domain": ".buy",
        "entity": ""
    },
    {
        "domain": ".buzz",
        "entity": "销售和社交网络"
    },
    {
        "domain": ".cab",
        "entity": "出租车公司"
    },
    {
        "domain": ".cafe",
        "entity": "咖啡产业"
    },
    {
        "domain": ".call",
        "entity": ""
    },
    {
        "domain": ".cam",
        "entity": "娱乐[64]"
    },
    {
        "domain": ".camera",
        "entity": "与照相机相关的企业"
    },
    {
        "domain": ".camp",
        "entity": "露营"
    },
    {
        "domain": ".cancerresearch",
        "entity": "对通过研究抗击癌症感兴趣的组织、研究机构和个人[66]"
    },
    {
        "domain": ".capital",
        "entity": "金融公司"
    },
    {
        "domain": ".car",
        "entity": ""
    },
    {
        "domain": ".cards",
        "entity": "通用"
    },
    {
        "domain": ".care",
        "entity": "医疗保健人员"
    },
    {
        "domain": ".career",
        "entity": ""
    },
    {
        "domain": ".careers",
        "entity": "职业雇佣"
    },
    {
        "domain": ".cars",
        "entity": "汽车业"
    },
    {
        "domain": ".case",
        "entity": ""
    },
    {
        "domain": ".cash",
        "entity": "金融"
    },
    {
        "domain": ".casino",
        "entity": "赌场"
    },
    {
        "domain": ".catering",
        "entity": "食品服务"
    },
    {
        "domain": ".catholic",
        "entity": ""
    },
    {
        "domain": ".center",
        "entity": "通用"
    },
    {
        "domain": ".cern",
        "entity": "CERN"
    },
    {
        "domain": ".ceo",
        "entity": "首席执行官"
    },
    {
        "domain": ".cfd",
        "entity": ""
    },
    {
        "domain": ".channel",
        "entity": ""
    },
    {
        "domain": ".chat",
        "entity": "在线聊天"
    },
    {
        "domain": ".cheap",
        "entity": "销售商"
    },
    {
        "domain": ".christmas",
        "entity": "圣诞节"
    },
    {
        "domain": ".church",
        "entity": "教堂"
    },
    {
        "domain": ".cipriani",
        "entity": ""
    },
    {
        "domain": ".circle",
        "entity": ""
    },
    {
        "domain": ".city",
        "entity": "通用"
    },
    {
        "domain": ".claims",
        "entity": "零售、拍卖"
    },
    {
        "domain": ".cleaning",
        "entity": "保洁服务"
    },
    {
        "domain": ".click",
        "entity": ""
    },
    {
        "domain": ".clinic",
        "entity": "诊所"
    },
    {
        "domain": ".clothing",
        "entity": "Apparel"
    },
    {
        "domain": ".cloud",
        "entity": ""
    },
    {
        "domain": ".club",
        "entity": "集团、组织、集会、社群、通用"
    },
    {
        "domain": ".coach",
        "entity": "旅游（航班和客车）"
    },
    {
        "domain": ".codes",
        "entity": "电脑和加密代码爱好者"
    },
    {
        "domain": ".coffee",
        "entity": "咖啡馆和咖啡爱好者"
    },
    {
        "domain": ".college",
        "entity": "教育"
    },
    {
        "domain": ".community",
        "entity": "社交群组、邻居"
    },
    {
        "domain": ".company",
        "entity": "商业协会"
    },
    {
        "domain": ".compare",
        "entity": ""
    },
    {
        "domain": ".computer",
        "entity": "技术"
    },
    {
        "domain": ".condos",
        "entity": "不动产"
    },
    {
        "domain": ".construction",
        "entity": "建筑业"
    },
    {
        "domain": ".consulting",
        "entity": "聘用顾问"
    },
    {
        "domain": ".contact",
        "entity": ""
    },
    {
        "domain": ".contractors",
        "entity": "改建和个体经营"
    },
    {
        "domain": ".cooking",
        "entity": "共享食谱"
    },
    {
        "domain": ".cool",
        "entity": "公众利益"
    },
    {
        "domain": ".coop",
        "entity": "合作社"
    },
    {
        "domain": ".country",
        "entity": "通用"
    },
    {
        "domain": ".coupon",
        "entity": ""
    },
    {
        "domain": ".coupons",
        "entity": "兑换券"
    },
    {
        "domain": ".courses",
        "entity": ""
    },
    {
        "domain": ".credit",
        "entity": "金融机构"
    },
    {
        "domain": ".creditcard",
        "entity": "金融机构"
    },
    {
        "domain": ".cruise",
        "entity": ""
    },
    {
        "domain": ".cricket",
        "entity": "板球"
    },
    {
        "domain": ".cruises",
        "entity": "邮轮公司和旅游"
    },
    {
        "domain": ".dad",
        "entity": "家庭"
    },
    {
        "domain": ".dance",
        "entity": "舞蹈工作室和公司"
    },
    {
        "domain": ".data",
        "entity": ""
    },
    {
        "domain": ".date",
        "entity": "在线约会"
    },
    {
        "domain": ".dating",
        "entity": "在线约会"
    },
    {
        "domain": ".day",
        "entity": "通用"
    },
    {
        "domain": ".deal",
        "entity": ""
    },
    {
        "domain": ".deals",
        "entity": "在线购物和票券兑换"
    },
    {
        "domain": ".degree",
        "entity": "通用"
    },
    {
        "domain": ".delivery",
        "entity": "通用"
    },
    {
        "domain": ".democrat",
        "entity": "民主党政客"
    },
    {
        "domain": ".dental",
        "entity": "牙医"
    },
    {
        "domain": ".dentist",
        "entity": "牙医"
    },
    {
        "domain": ".design",
        "entity": "图形艺术和时尚"
    },
    {
        "domain": ".dev",
        "entity": "开发"
    },
    {
        "domain": ".diamonds",
        "entity": "钻石和珠宝工业"
    },
    {
        "domain": ".diet",
        "entity": ""
    },
    {
        "domain": ".digital",
        "entity": "通用"
    },
    {
        "domain": ".direct",
        "entity": "通用"
    },
    {
        "domain": ".directory",
        "entity": "通用目录"
    },
    {
        "domain": ".discount",
        "entity": "通用"
    },
    {
        "domain": ".diy",
        "entity": ""
    },
    {
        "domain": ".docs",
        "entity": ""
    },
    {
        "domain": ".doctor",
        "entity": ""
    },
    {
        "domain": ".dog",
        "entity": "狗商店及主人"
    },
    {
        "domain": ".domains",
        "entity": "域名注册者"
    },
    {
        "domain": ".dot",
        "entity": ""
    },
    {
        "domain": ".download",
        "entity": "技术"
    },
    {
        "domain": ".drive",
        "entity": ""
    },
    {
        "domain": ".duck",
        "entity": ""
    },
    {
        "domain": ".earth",
        "entity": ""
    },
    {
        "domain": ".eat",
        "entity": "餐馆和吃货（英语：Foodie）"
    },
    {
        "domain": ".eco",
        "entity": "专注于可持续性的公司、非营利实体和专家。[70]"
    },
    {
        "domain": ".education",
        "entity": "教育机构"
    },
    {
        "domain": ".email",
        "entity": "电子邮件"
    },
    {
        "domain": ".energy",
        "entity": "能源工业和销售"
    },
    {
        "domain": ".engineer",
        "entity": "工程师和工程公司"
    },
    {
        "domain": ".engineering",
        "entity": "工程公司"
    },
    {
        "domain": ".edeka",
        "entity": "埃德卡超市"
    },
    {
        "domain": ".enterprises",
        "entity": "商业协会"
    },
    {
        "domain": ".equipment",
        "entity": "设备相关商业"
    },
    {
        "domain": ".esq",
        "entity": "律师、法律事务所、法律专家"
    },
    {
        "domain": ".estate",
        "entity": "真实存在商业"
    },
    {
        "domain": ".events",
        "entity": "事件"
    },
    {
        "domain": ".exchange",
        "entity": "普通贸易"
    },
    {
        "domain": ".expert",
        "entity": "通用专家意见"
    },
    {
        "domain": ".exposed",
        "entity": "通用兴趣"
    },
    {
        "domain": ".express",
        "entity": "货运"
    },
    {
        "domain": ".fail",
        "entity": "通用"
    },
    {
        "domain": ".faith",
        "entity": "宗教和教堂"
    },
    {
        "domain": ".family",
        "entity": "家庭"
    },
    {
        "domain": ".fan",
        "entity": ""
    },
    {
        "domain": ".fans",
        "entity": "通用"
    },
    {
        "domain": ".farm",
        "entity": "农场和农业"
    },
    {
        "domain": ".fashion",
        "entity": "服装工业"
    },
    {
        "domain": ".fast",
        "entity": ""
    },
    {
        "domain": ".feedback",
        "entity": ""
    },
    {
        "domain": ".film",
        "entity": ""
    },
    {
        "domain": ".final",
        "entity": ""
    },
    {
        "domain": ".finance",
        "entity": "金融"
    },
    {
        "domain": ".financial",
        "entity": "金融"
    },
    {
        "domain": ".fire",
        "entity": ""
    },
    {
        "domain": ".fish",
        "entity": "渔业公司、体育和爱好者"
    },
    {
        "domain": ".fishing",
        "entity": "渔业公司、体育和爱好者"
    },
    {
        "domain": ".fit",
        "entity": "健身锻炼"
    },
    {
        "domain": ".fitness",
        "entity": "健身锻炼"
    },
    {
        "domain": ".flights",
        "entity": "航空公司和旅行"
    },
    {
        "domain": ".florist",
        "entity": "花匠"
    },
    {
        "domain": ".flowers",
        "entity": "花匠和花园"
    },
    {
        "domain": ".fly",
        "entity": "旅行"
    },
    {
        "domain": ".foo",
        "entity": "互联网开发"
    },
    {
        "domain": ".food",
        "entity": ""
    },
    {
        "domain": ".foodnetwork",
        "entity": ""
    },
    {
        "domain": ".football",
        "entity": "英式和美式足球"
    },
    {
        "domain": ".forsale",
        "entity": "互联网零售"
    },
    {
        "domain": ".forum",
        "entity": ""
    },
    {
        "domain": ".foundation",
        "entity": "慈善机构"
    },
    {
        "domain": ".free",
        "entity": ""
    },
    {
        "domain": ".frontdoor",
        "entity": ""
    },
    {
        "domain": ".fun",
        "entity": ""
    },
    {
        "domain": ".fund",
        "entity": "金融"
    },
    {
        "domain": ".furniture",
        "entity": "家具企业"
    },
    {
        "domain": ".futbol",
        "entity": ""
    },
    {
        "domain": ".fyi",
        "entity": "仅供参考"
    },
    {
        "domain": ".gallery",
        "entity": "照片和艺术画廊"
    },
    {
        "domain": ".game",
        "entity": ""
    },
    {
        "domain": ".games",
        "entity": ""
    },
    {
        "domain": ".garden",
        "entity": "园艺"
    },
    {
        "domain": ".gay",
        "entity": "gay"
    },
    {
        "domain": ".gdn",
        "entity": "none, anyone"
    },
    {
        "domain": ".gift",
        "entity": "gift-giving"
    },
    {
        "domain": ".gifts",
        "entity": "gift-giving"
    },
    {
        "domain": ".gives",
        "entity": "charities and gift-giving"
    },
    {
        "domain": ".glass",
        "entity": "window sales and repairs"
    },
    {
        "domain": ".global",
        "entity": "general"
    },
    {
        "domain": ".gold",
        "entity": "gold and luxury"
    },
    {
        "domain": ".golf",
        "entity": "golf"
    },
    {
        "domain": ".google",
        "entity": "Google"
    },
    {
        "domain": ".gop",
        "entity": "Republican Partypolitics"
    },
    {
        "domain": ".graphics",
        "entity": "graphics"
    },
    {
        "domain": ".green",
        "entity": "the environmentally-focused"
    },
    {
        "domain": ".gripe",
        "entity": "opinion sites"
    },
    {
        "domain": ".grocery",
        "entity": ""
    },
    {
        "domain": ".group",
        "entity": ""
    },
    {
        "domain": ".guide",
        "entity": "help sites"
    },
    {
        "domain": ".guitars",
        "entity": "Guitars"
    },
    {
        "domain": ".guru",
        "entity": "generic expertise"
    }
]

ALI_TOPDOMAIN = [
    {
        "domain": ".com"
    },
    {
        "domain": ".asia"
    },
    {
        "domain": ".net"
    },
    {
        "domain": ".info"
    },
    {
        "domain": ".biz"
    },
    {
        "domain": ".pro"
    },
    {
        "domain": ".mobi"
    },
    {
        "domain": ".cn"
    },
    {
        "domain": ".tv"
    },
    {
        "domain": ".cc"
    },
    {
        "domain": ".co"
    },
    {
        "domain": ".art"
    },
    {
        "domain": ".beer"
    },
    {
        "domain": ".band"
    },
    {
        "domain": ".company"
    },
    {
        "domain": ".chat"
    },
    {
        "domain": ".city"
    },
    {
        "domain": ".cool"
    },
    {
        "domain": ".cloud"
    },
    {
        "domain": ".club"
    },
    {
        "domain": ".center"
    },
    {
        "domain": ".design"
    },
    {
        "domain": ".email"
    },
    {
        "domain": ".fund"
    },
    {
        "domain": ".fans"
    },
    {
        "domain": ".fun"
    },
    {
        "domain": ".fit"
    },
    {
        "domain": ".group"
    },
    {
        "domain": ".guru"
    },
    {
        "domain": ".gold"
    },
    {
        "domain": ".games"
    },
    {
        "domain": ".host"
    },
    {
        "domain": ".icu"
    },
    {
        "domain": ".ink"
    },
    {
        "domain": ".kim"
    },
    {
        "domain": ".ltd"
    },
    {
        "domain": ".love"
    },
    {
        "domain": ".live"
    },
    {
        "domain": ".life"
    },
    {
        "domain": ".law"
    },
    {
        "domain": ".luxe"
    },
    {
        "domain": ".market"
    },
    {
        "domain": ".news"
    },
    {
        "domain": ".online"
    },
    {
        "domain": ".press"
    },
    {
        "domain": ".plus"
    },
    {
        "domain": ".pub"
    },
    {
        "domain": ".ren"
    },
    {
        "domain": ".run"
    },
    {
        "domain": ".red"
    },
    {
        "domain": ".space"
    },
    {
        "domain": ".store"
    },
    {
        "domain": ".shop"
    },
    {
        "domain": ".site"
    },
    {
        "domain": ".social"
    },
    {
        "domain": ".show"
    },
    {
        "domain": ".studio"
    },
    {
        "domain": ".top"
    },
    {
        "domain": ".today"
    },
    {
        "domain": ".tech"
    },
    {
        "domain": ".team"
    },
    {
        "domain": ".vip"
    },
    {
        "domain": ".video"
    },
    {
        "domain": ".wang"
    },
    {
        "domain": ".work"
    },
    {
        "domain": ".world"
    },
    {
        "domain": ".wiki"
    },
    {
        "domain": ".website"
    },
    {
        "domain": ".xyz"
    },
    {
        "domain": ".xin"
    },
    {
        "domain": ".yoga"
    },
    {
        "domain": ".zone"
    }
]

TENCENT_TOPDOMAIN = [
    {
        "domain": ".cn"
    },
    {
        "domain": ".com"
    },
    {
        "domain": ".net"
    },
    {
        "domain": ".xyz"
    },
    {
        "domain": ".wang"
    },
    {
        "domain": ".ac.cn"
    },
    {
        "domain": ".com.cn"
    },
    {
        "domain": ".net.cn"
    },
    {
        "domain": ".中国"
    },
    {
        "domain": ".网址"
    },
    {
        "domain": ".在线"
    },
    {
        "domain": ".top"
    },
    {
        "domain": ".club"
    },
    {
        "domain": ".vip"
    },
    {
        "domain": ".beer"
    },
    {
        "domain": ".work"
    },
    {
        "domain": ".fashion"
    },
    {
        "domain": ".luxe"
    },
    {
        "domain": ".yoga"
    },
    {
        "domain": ".love"
    },
    {
        "domain": ".online"
    },
    {
        "domain": ".mobi"
    },
    {
        "domain": ".中文网"
    },
    {
        "domain": ".ltd"
    },
    {
        "domain": ".chat"
    },
    {
        "domain": ".group"
    },
    {
        "domain": ".pub"
    },
    {
        "domain": ".run"
    },
    {
        "domain": ".city"
    },
    {
        "domain": ".live"
    },
    {
        "domain": ".info"
    },
    {
        "domain": ".pro"
    },
    {
        "domain": ".red"
    },
    {
        "domain": ".网店"
    },
    {
        "domain": ".kim"
    },
    {
        "domain": ".blue"
    },
    {
        "domain": ".pet"
    },
    {
        "domain": ".移动"
    },
    {
        "domain": ".space"
    },
    {
        "domain": ".tech"
    },
    {
        "domain": ".host"
    },
    {
        "domain": ".site"
    },
    {
        "domain": ".fun"
    },
    {
        "domain": ".store"
    },
    {
        "domain": ".ski"
    },
    {
        "domain": ".pink"
    },
    {
        "domain": ".design"
    },
    {
        "domain": ".ink"
    },
    {
        "domain": ".wiki"
    },
    {
        "domain": ".email"
    },
    {
        "domain": ".video"
    },
    {
        "domain": ".company"
    },
    {
        "domain": ".plus"
    },
    {
        "domain": ".center"
    },
    {
        "domain": ".cool"
    },
    {
        "domain": ".fund"
    },
    {
        "domain": ".gold"
    },
    {
        "domain": ".guru"
    },
    {
        "domain": ".life"
    },
    {
        "domain": ".show"
    },
    {
        "domain": ".team"
    },
    {
        "domain": ".today"
    },
    {
        "domain": ".world"
    },
    {
        "domain": ".zone"
    },
    {
        "domain": ".social"
    },
    {
        "domain": ".bio"
    },
    {
        "domain": ".black"
    },
    {
        "domain": ".green"
    },
    {
        "domain": ".lotto"
    },
    {
        "domain": ".organic"
    },
    {
        "domain": ".poker"
    },
    {
        "domain": ".promo"
    },
    {
        "domain": ".vote"
    },
    {
        "domain": ".archi"
    },
    {
        "domain": ".voto"
    },
    {
        "domain": ".网站"
    },
    {
        "domain": ".商店"
    },
    {
        "domain": ".企业"
    },
    {
        "domain": ".娱乐"
    },
    {
        "domain": ".游戏"
    },
    {
        "domain": ".fit"
    },
    {
        "domain": ".website"
    },
    {
        "domain": ".press"
    },
    {
        "domain": ".icu"
    },
    {
        "domain": ".art"
    },
    {
        "domain": ".asia"
    },
    {
        "domain": ".org.cn"
    },
    {
        "domain": ".biz"
    },
    {
        "domain": ".集团"
    },
    {
        "domain": ".我爱你"
    },
    {
        "domain": ".games"
    },
    {
        "domain": ".sale"
    },
    {
        "domain": ".media"
    },
    {
        "domain": ".studio"
    },
    {
        "domain": ".band"
    },
    {
        "domain": ".fyi"
    },
    {
        "domain": ".cab"
    },
    {
        "domain": ".market"
    },
    {
        "domain": ".news"
    },
    {
        "domain": ".vin"
    },
    {
        "domain": ".tax"
    },
    {
        "domain": ".shopping"
    },
    {
        "domain": ".mba"
    },
    {
        "domain": ".cash"
    },
    {
        "domain": ".cafe"
    },
    {
        "domain": ".technology"
    },
    {
        "domain": ".ren"
    },
    {
        "domain": ".fans"
    },
    {
        "domain": ".co"
    },
    {
        "domain": ".cloud"
    },
    {
        "domain": ".shop"
    },
    {
        "domain": ".law"
    },
    {
        "domain": ".link"
    },
    {
        "domain": ".bj.cn"
    },
    {
        "domain": ".tj.cn"
    },
    {
        "domain": ".sh.cn"
    },
    {
        "domain": ".cq.cn"
    },
    {
        "domain": ".he.cn"
    },
    {
        "domain": ".ha.cn"
    },
    {
        "domain": ".sx.cn"
    },
    {
        "domain": ".nm.cn"
    },
    {
        "domain": ".ln.cn"
    },
    {
        "domain": ".jl.cn"
    },
    {
        "domain": ".hl.cn"
    },
    {
        "domain": ".js.cn"
    },
    {
        "domain": ".zj.cn"
    },
    {
        "domain": ".ah.cn"
    },
    {
        "domain": ".fj.cn"
    },
    {
        "domain": ".jx.cn"
    },
    {
        "domain": ".sd.cn"
    },
    {
        "domain": ".hb.cn"
    },
    {
        "domain": ".hn.cn"
    },
    {
        "domain": ".gd.cn"
    },
    {
        "domain": ".gx.cn"
    },
    {
        "domain": ".hi.cn"
    },
    {
        "domain": ".sc.cn"
    },
    {
        "domain": ".gz.cn"
    },
    {
        "domain": ".yn.cn"
    },
    {
        "domain": ".xz.cn"
    },
    {
        "domain": ".sn.cn"
    },
    {
        "domain": ".gs.cn"
    },
    {
        "domain": ".qh.cn"
    },
    {
        "domain": ".nx.cn"
    },
    {
        "domain": ".xj.cn"
    },
    {
        "domain": ".tw.cn"
    },
    {
        "domain": ".hk.cn"
    },
    {
        "domain": ".mo.cn"
    },
    {
        "domain": ".fan"
    },
    {
        "domain": ".cn"
    },
    {
        "domain": ".com"
    },
    {
        "domain": ".net"
    },
    {
        "domain": ".ac.cn"
    },
    {
        "domain": ".com.cn"
    },
    {
        "domain": ".net.cn"
    },
    {
        "domain": ".org.cn"
    },
    {
        "domain": ".中国"
    },
    {
        "domain": ".bj.cn"
    },
    {
        "domain": ".tj.cn"
    },
    {
        "domain": ".sh.cn"
    },
    {
        "domain": ".cq.cn"
    },
    {
        "domain": ".he.cn"
    },
    {
        "domain": ".ha.cn"
    },
    {
        "domain": ".sx.cn"
    },
    {
        "domain": ".nm.cn"
    },
    {
        "domain": ".ln.cn"
    },
    {
        "domain": ".jl.cn"
    },
    {
        "domain": ".hl.cn"
    },
    {
        "domain": ".js.cn"
    },
    {
        "domain": ".zj.cn"
    },
    {
        "domain": ".ah.cn"
    },
    {
        "domain": ".fj.cn"
    },
    {
        "domain": ".jx.cn"
    },
    {
        "domain": ".sd.cn"
    },
    {
        "domain": ".hb.cn"
    },
    {
        "domain": ".hn.cn"
    },
    {
        "domain": ".gd.cn"
    },
    {
        "domain": ".gx.cn"
    },
    {
        "domain": ".hi.cn"
    },
    {
        "domain": ".sc.cn"
    },
    {
        "domain": ".gz.cn"
    },
    {
        "domain": ".yn.cn"
    },
    {
        "domain": ".xz.cn"
    },
    {
        "domain": ".sn.cn"
    },
    {
        "domain": ".gs.cn"
    },
    {
        "domain": ".qh.cn"
    },
    {
        "domain": ".nx.cn"
    },
    {
        "domain": ".xj.cn"
    },
    {
        "domain": ".tw.cn"
    },
    {
        "domain": ".hk.cn"
    },
    {
        "domain": ".mo.cn"
    },
    {
        "domain": ".cn"
    },
    {
        "domain": ".ac.cn"
    },
    {
        "domain": ".com.cn"
    },
    {
        "domain": ".net.cn"
    },
    {
        "domain": ".org.cn"
    },
    {
        "domain": ".中国"
    },
    {
        "domain": ".cc"
    },
    {
        "domain": ".tv"
    },
    {
        "domain": ".bj.cn"
    },
    {
        "domain": ".tj.cn"
    },
    {
        "domain": ".sh.cn"
    },
    {
        "domain": ".cq.cn"
    },
    {
        "domain": ".he.cn"
    },
    {
        "domain": ".ha.cn"
    },
    {
        "domain": ".sx.cn"
    },
    {
        "domain": ".nm.cn"
    },
    {
        "domain": ".ln.cn"
    },
    {
        "domain": ".jl.cn"
    },
    {
        "domain": ".hl.cn"
    },
    {
        "domain": ".js.cn"
    },
    {
        "domain": ".zj.cn"
    },
    {
        "domain": ".ah.cn"
    },
    {
        "domain": ".fj.cn"
    },
    {
        "domain": ".jx.cn"
    },
    {
        "domain": ".sd.cn"
    },
    {
        "domain": ".hb.cn"
    },
    {
        "domain": ".hn.cn"
    },
    {
        "domain": ".gd.cn"
    },
    {
        "domain": ".gx.cn"
    },
    {
        "domain": ".hi.cn"
    },
    {
        "domain": ".sc.cn"
    },
    {
        "domain": ".gz.cn"
    },
    {
        "domain": ".yn.cn"
    },
    {
        "domain": ".xz.cn"
    },
    {
        "domain": ".sn.cn"
    },
    {
        "domain": ".gs.cn"
    },
    {
        "domain": ".qh.cn"
    },
    {
        "domain": ".nx.cn"
    },
    {
        "domain": ".xj.cn"
    },
    {
        "domain": ".tw.cn"
    },
    {
        "domain": ".hk.cn"
    },
    {
        "domain": ".mo.cn"
    },
    {
        "domain": ".cn"
    },
    {
        "domain": ".ac.cn"
    },
    {
        "domain": ".com.cn"
    },
    {
        "domain": ".net.cn"
    },
    {
        "domain": ".org.cn"
    },
    {
        "domain": ".bj.cn"
    },
    {
        "domain": ".tj.cn"
    },
    {
        "domain": ".sh.cn"
    },
    {
        "domain": ".cq.cn"
    },
    {
        "domain": ".he.cn"
    },
    {
        "domain": ".ha.cn"
    },
    {
        "domain": ".sx.cn"
    },
    {
        "domain": ".nm.cn"
    },
    {
        "domain": ".ln.cn"
    },
    {
        "domain": ".jl.cn"
    },
    {
        "domain": ".hl.cn"
    },
    {
        "domain": ".js.cn"
    },
    {
        "domain": ".zj.cn"
    },
    {
        "domain": ".ah.cn"
    },
    {
        "domain": ".fj.cn"
    },
    {
        "domain": ".jx.cn"
    },
    {
        "domain": ".sd.cn"
    },
    {
        "domain": ".hb.cn"
    },
    {
        "domain": ".hn.cn"
    },
    {
        "domain": ".gd.cn"
    },
    {
        "domain": ".gx.cn"
    },
    {
        "domain": ".hi.cn"
    },
    {
        "domain": ".sc.cn"
    },
    {
        "domain": ".gz.cn"
    },
    {
        "domain": ".yn.cn"
    },
    {
        "domain": ".xz.cn"
    },
    {
        "domain": ".sn.cn"
    },
    {
        "domain": ".gs.cn"
    },
    {
        "domain": ".qh.cn"
    },
    {
        "domain": ".nx.cn"
    },
    {
        "domain": ".xj.cn"
    },
    {
        "domain": ".tw.cn"
    },
    {
        "domain": ".hk.cn"
    },
    {
        "domain": ".mo.cn"
    },
    {
        "domain": ".com"
    },
    {
        "domain": ".cn"
    },
    {
        "domain": ".ac.cn"
    },
    {
        "domain": ".com.cn"
    },
    {
        "domain": ".net.cn"
    },
    {
        "domain": ".org.cn"
    },
    {
        "domain": ".bj.cn"
    },
    {
        "domain": ".tj.cn"
    },
    {
        "domain": ".sh.cn"
    },
    {
        "domain": ".cq.cn"
    },
    {
        "domain": ".he.cn"
    },
    {
        "domain": ".ha.cn"
    },
    {
        "domain": ".sx.cn"
    },
    {
        "domain": ".nm.cn"
    },
    {
        "domain": ".ln.cn"
    },
    {
        "domain": ".jl.cn"
    },
    {
        "domain": ".hl.cn"
    },
    {
        "domain": ".js.cn"
    },
    {
        "domain": ".zj.cn"
    },
    {
        "domain": ".ah.cn"
    },
    {
        "domain": ".fj.cn"
    },
    {
        "domain": ".jx.cn"
    },
    {
        "domain": ".sd.cn"
    },
    {
        "domain": ".hb.cn"
    },
    {
        "domain": ".hn.cn"
    },
    {
        "domain": ".gd.cn"
    },
    {
        "domain": ".gx.cn"
    },
    {
        "domain": ".hi.cn"
    },
    {
        "domain": ".sc.cn"
    },
    {
        "domain": ".gz.cn"
    },
    {
        "domain": ".yn.cn"
    },
    {
        "domain": ".xz.cn"
    },
    {
        "domain": ".sn.cn"
    },
    {
        "domain": ".gs.cn"
    },
    {
        "domain": ".qh.cn"
    },
    {
        "domain": ".nx.cn"
    },
    {
        "domain": ".xj.cn"
    },
    {
        "domain": ".tw.cn"
    },
    {
        "domain": ".hk.cn"
    },
    {
        "domain": ".mo.cn"
    }
]

# 集合所有顶级域名确保
all_top_domain = [{'domain': _['domain']} for _ in WIKI_TOPDOMAIN] + ALI_TOPDOMAIN + TENCENT_TOPDOMAIN + SELF_DOMAIN_LIST
TOP_DOMAIN = list({d['domain']: d for d in all_top_domain}.values())


if __name__ == '__main__':
    print("域名个数: ", len(TOP_DOMAIN))
    print("所有域名: ", TOP_DOMAIN)

    # 找到重复的域名
    duplicates = set([domain for domain in TOP_DOMAIN if TOP_DOMAIN.count(domain) > 1])

    if duplicates:
        print("重复的域名:", duplicates)
    else:
        print("没有重复的域名")