import jieba
with open('../jieba111/小米还没放弃印度？国内699神机准备中 还有“外星科技”！.txt', encoding='utf-8') as f:
    document = f.read()
    document_cut = jieba.cut(document)
    result = ' '.join(document_cut)
    print(result)
    with open('../jieba111/nlp_test1.txt', 'w', encoding='utf-8') as fp:
        fp.write(result)
f.close()
fp.close()
stpwrdpath = "./stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'rb')
stpwrd_content = stpwrd_dic.read()
#将停用词表转换为list
stpwrdlst = stpwrd_content.splitlines()
stpwrd_dic.close()
with open('../jieba111/nlp_test1.txt', 'r', encoding='utf-8') as fp:
    res1 = fp.read()
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [res1]
vector = TfidfVectorizer(stop_words=stpwrdlst)
tfidf = vector.fit_transform(corpus)
print(tfidf)
print(vector.get_feature_names())
print('----------------------------')
wordlist = vector.get_feature_names()
# 获取词袋模型中的所有词
# tf-idf矩阵 元素a[i][j]表示j词在i类文本中的tf-idf权重
weightlist = tfidf.toarray()
# 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
for i in range(len(weightlist)):
    print("-------第", i, "段文本的词语tf-idf权重------")
    for j in range(len(wordlist)):
        print(wordlist[j], weightlist[i][j])