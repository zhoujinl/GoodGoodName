# 强烈建议修改
LAST_NAME = '周'  # 姓氏
SEX = '女'  # 孩子性别，男 或者 女
year = 2022  # 出生的时间：年
month = 8  # 出生的时间：月
date = 3  # 出生的时间：日
hour = 8  # 出生的时间：小时
minute = 40  # 出生的时间： 分钟

# 选择性修改
MIN_SINGLE_NUM = 2  # 单个字最少笔画过滤
MAX_SINGLE_NUM = 20  # 单个字最多笔画过滤
THRESHOLD_SCORE = 85  # 三才五格测试最低能接受的得分，结果记录在RESULT_FILE
SELECTED_XITONGSHEN = None  # 已知的喜用神，或者次喜用神。None表示没关系。这个喜用神自己在网站查查，选填，填了可能没有最佳匹配结果

# 尽量别改，除非你知道是什么意思
debug = False
my_write_num_list = [(7, 10)]  # 经过第一轮测试后笔画的结果， 自己记录下来
true_request = True  # 真实请求测试
# 名字固定要的字
fix_write_word = ''
SELECTED_SANCAI = ['大吉', '中吉']  # 三才中，如果为None就不特意选最好的
quming_dafen_url = 'http://www.qimingzi.net/simpleReport.aspx?'

# 可直接测试
quming_dafen_url2 = 'https://www.threetong.com/ceming/baziceming/'
# 首先在http://www.qimingzi.net/ 网站提交基本信息，点击开始起名，F12查看请求信息把Cookie复制下来
#headers = {"Cookie": "__51cke__=; Hm_lvt_1f1b125fd1b03fdb6cac5abdd0f5d306=1660446110; ASP.NET_SessionId=15ypbzw01bd404fvqagi5qme; __tins__5033285={\"sid\": 1660446109329, \"vd\": 9, \"expires\": 1660448937029}; 53gid2=12395362411005; 53gid0=12395362411005; 53gid1=12395362411005; 53revisit=1660447147569; 53kf_72241622_from_host=www.qimingzi.net; 53kf_72241622_land_page=http%3A%2F%2Fwww.qimingzi.net%2FsimpleReport.aspx; kf_72241622_land_page_ok=1; 53uvid=1; onliner_zdfq72241622=0; visitor_type=old; 53kf_72241622_keyword=http://www.qimingzi.net/simpleReport.aspx; __tins__20674741={\"sid\": 1660452910072, \"vd\": 1, \"expires\": 1660454710072}; __51laig__=15; Hm_lpvt_1f1b125fd1b03fdb6cac5abdd0f5d306=1660452910",
#           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}

#__51cke__=; Hm_lvt_1f1b125fd1b03fdb6cac5abdd0f5d306=1660446110; ASP.NET_SessionId=15ypbzw01bd404fvqagi5qme; __tins__5033285=%7B%22sid%22%3A%201660446109329%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201660448141201%7D; __51laig__=5; Hm_lpvt_1f1b125fd1b03fdb6cac5abdd0f5d306=1660446341