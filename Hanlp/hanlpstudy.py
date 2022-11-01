from pyhanlp import *

# 分词和词性标注
sentence = "我爱自然语言处理技术！"
s_hanlp = HanLP.segment(sentence)
# for term in s_hanlp:
#     print(term.word, term.nature)
# 我 rr
# 爱 v
# 自然语言处理 nz
# 技术 n
# ！ w

# 依存句法分析
s_dep = HanLP.parseDependency(sentence)
# print(s_dep)
# 1	我	我	r	r	_	2	主谓关系	_	_
# 2	爱	爱	v	v	_	0	核心关系	_	_
# 3	自然语言处理	自然语言处理	nz	nz	_	4	定中关系	_	_
# 4	技术	技术	n	n	_	2	动宾关系	_	_
# 5	！	！	wp	w	_	2	标点符号	_	_

# 关键词提取
document = '自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。它研究能实现人与计算机之间\
用自然语言进行有效通信的各种理论和方法。自然语言处理是一门融语言学、计算机科学、数学于一体的科学。因\
此，这一领域的研究将涉及自然语言，即人们日常使用的语言，所以它与语言学的研究有着密切的联系，但又有重\
要的区别。自然语言处理并不是一般地研究自然语言，而在于研制能有效地实现自然语言通信的计算机系统，特别\
是其中的软件系统。因而它是计算机科学的一部分。'
# 第一个参数：需要处理的文字  第二个参数：需要输出的关键字个数
doc_keyword = HanLP.extractKeyword(document, 5)
# for word in doc_keyword:
#     print(word)
# 研究
# 自然语言
# 自然语言处理
# 计算机
# 语言学

# 摘要提取
# 第一个参数：需要处理的文字  第二个参数：需要输出的关键字个数
doc_keysentence = HanLP.extractSummary(document, 3)
# for keysentence in doc_keysentence:
#     print(keysentence)
# 自然语言处理并不是一般地研究自然语言
# 自然语言处理是计算机科学领域与人工智能领域中的一个重要方向
# 它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法

# 感知机词法分析器
# PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp/model.perceptron.PerceptronLexicalAnalyzer')
# analyzer = PerceptronLexicalAnalyzer()
# print(analyzer.analyze("上海华安工业（集团）公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观"))
# [上海/ns 华安/nz 工业/n （/w 集团/n ）/w 公司/n]/nt 董事长/n 谭旭光/nr 和/c 秘书/n 胡花蕊/nr 来到/v [美国纽约/ns 现代/ntc 艺术/n 博物馆/n]/ns 参观/v


# 中国人名识别器
# NER = HanLP.newSegment().enableNameRecognize(True)
# p_name = NER.seg('王国强、高峰、汪洋、张朝阳光着头、韩寒、小四')
# print(p_name)
# [王国强/nr, 、/w, 高峰/n, 、/w, 汪洋/n, 、/w, 张朝阳/nr, 光着头/l, 、/w, 韩寒/nr, 、/w, 小四/nr]


# 音译人名识别
sentence = '微软的比尔盖茨、Facebook的扎克伯格跟桑德博格、亚马逊的贝索斯、苹果的库克，这些硅谷的科技人'
# person_ner = HanLP.newSegment().enableTranslatedNameRecognize(True)
# p_name = person_ner.seg(sentence)
# print(p_name)
# [微软/ntc, 的/ude1, 比尔盖茨/nrf, 、/w, Facebook/nx, 的/ude1, 扎克伯格/nrf, 跟/p, 桑德博格/nrf, 、/w, 亚马逊/nrf, 的/ude1, 贝索斯/nrf, 、/w, 苹果/nf, 的/ude1, 库克/nrf, ，/w, 这些/rz, 硅谷/ns, 的/ude1, 科技/n, 人/n]

# 短语提取
# phraseList = HanLP.extractPhrase(document, 3)
# print(phraseList)
# [计算机科学, 一领域, 中的重要]

# 拼音转换
s = '重载不是重任'
pinyinList = HanLP.convertToPinyinList(s)
for pinyin in pinyinList:
    print(pinyin.getPinyinWithoutTone(), pinyin.getTone(), pinyin,
pinyin.getPinyinWithToneMark())
# chong 2 chong2 chóng
# zai 3 zai3 zǎi
# bu 2 bu2 bú
# shi 4 shi4 shì
# zhong 4 zhong4 zhòng
# ren 4 ren4 rèn

# 声母、韵母
for pinyin in pinyinList:
    print(pinyin.getShengmu(), pinyin.getYunmu())
# ch ong
# z ai
# b u
# sh i
# zh ong
# r en


# 繁简转换
Fanti = HanLP.convertToTraditionalChinese('我爱自然语言处理！')
Jianti = HanLP.convertToSimplifiedChinese(Fanti)
print(Jianti)
print(Fanti)
# 我爱自然语言处理！
# 我愛自然語言處理！




