
from flask import Flask,request,jsonify
import string
import pandas as pd
import pyarabic.araby as araby
from pyarabic.araby import is_arabicrange
from farasa.stemmer import FarasaStemmer
import itertools
import random
import json
import requests
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import json
#model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)









#@app.route('/predict',methods=['POST'])
@app.route('/')
def index():
    a="hello "
    b="world!"
    return "lah yn3l xitan"
#     return "Hello world"
@app.route('/test',methods=['POST'])
def test():
    json={"a":"B"}
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
    #return json
    return predict()
@app.route('/predict',methods=['POST'])
#@app.route('/')
def predict():
    df=pd.read_json("arabicPresidentJson.json")
    arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
    english_punctuations = string.punctuation
    punctuations_list = arabic_punctuations + english_punctuations
    def remove_punctuations(text):
        for c in punctuations_list:
            text = text.replace(c," ")
        return text
    df.loc[:,"post_text"] = df.post_text.apply(lambda x : remove_punctuations(x))
#     def remove_stopWords(s):
#         stopwords_arabic = set(stopwords.words('arabic'))

#         s = ' '.join(word for word in s.split() if word not in stopwords_arabic)
#         return s


    def remove_stopWords(s):
        with open('list.txt', 'r') as f:
            listl = []
            for line in f:
                strip_lines = line.strip()
                listli = strip_lines.split()
                m = listl.append(listli)

        new_list =[word for sublist in listl for word in sublist]
        stopwords_arabic = set(new_list)

        s = ' '.join(word for word in s.split() if word not in stopwords_arabic)
        return s






    df.loc[:,"post_text"] = df.post_text.apply(lambda x: remove_stopWords(x))
    stemmer = FarasaStemmer()

#     def lemmatization(text):
#         return stemmer.stem(text)
    tokenized_postes = [araby.tokenize(post_text, conditions=is_arabicrange) for post_text in df['post_text'].values]
    flat_list = list(itertools.chain(*tokenized_postes))
    new_list=[]
    for s in flat_list:
        if s in ["ووجدة","بوجدة","وجدة"]:
            new_list.append("oujda")
        elif s in ["وفاس","بفاس","فاس"]:
            new_list.append("fes")
        elif s in ["وبركان","ببركان","بركان"]:
            new_list.append("berkan")
        elif s in ["وتاوريرت","بتاوريرت","تاوريرت"]:
            new_list.append("TAOURIRT")
        elif s in ["والناظور","بالناظور","الناظور"]:
            new_list.append("NADOR")
        elif s in ["والناضور","بالناضور","الناضور"]:
            new_list.append("NADOR")
        elif s in ["ومكناس","بمكناس","مكناس"]:
            new_list.append("MEKNES")  
        elif s in ["وإفران","بإفران","إفران"]:
            new_list.append("IFRANE")  
        elif s in ["وسلا","بسلا","سلا"]:
            new_list.append("SALE")  
        elif s in ["والرباط","بالرباط","الرباط"]:
            new_list.append("RABAT")  
        elif s in ["والدار البيضاء","بالدار البيضاء","الدار البيضاء"]:
            new_list.append("CASABLANCA") 
        elif s in ["والمحمدية","بالمحمدية","المحمدية"]:
            new_list.append("MOHAMMEDIA") 
        elif s in ["وسطات","بسطات","سطات"]:
            new_list.append("SETTAT") 
        else:
            new_list.append(s)
    text = ' '.join(a for a in new_list)
    d={
        "المدرسة الوطنية للعلوم التطبيقية":"ENSA",
        "كلية الطب والصيدلة":"FMP",
        "المدرسة الوطنية للتجارة و التسيير":"ENCG",
        "المدرسة العليا للتكنلوجيا":"EST",
        " الكلية متعددة التخصصات بالناظور":"FPN",
        "لكلية متعددة التخصصات بتاوريرت":"FPT",
        "كلية العلوم":"FS",
        "كلية الاداب والعلوم الانسانية":"FLSH",
        "كلية العلوم القانونية والاقتصادية والاجتماعيية":"FSJES",
        "جامعة الأخوين":"FFRERES"
        }
    for i in d:
        text=text.replace(i,d[i])
    text=stemmer.stem(text)

#     url = 'https://farasa.qcri.org/webapi/lemmatization/'
#     api_key = "MtYakbZGWQfPUoObzk"
#     payload = {'text': text, 'api_key': api_key}
#     data = requests.post(url, data=payload)
#     text = json.loads(data.text)['text']
    
    
    
#     s=text.split()
#     s = random.choices(s, k=len(s))
#     s = ' '.join(a for a in s)
#     d={
#         "المدرسة الوطنية للعلوم التطبيقية":"ensa",
#         "كلية الطب والصيدلة":"fmp",
#         "المدرسة الوطنية للتجارة و التسيير":"encg",
#         "المدرسة العليا للتكنلوجيا":"est",
#         " الكلية متعددة التخصصات بالناظور":"fpn",
#         "لكلية متعددة التخصصات بتاوريرت":"fpt",
#         "كلية العلوم":"fso",
#         "كلية الاداب والعلوم الانسانية":"flsh",
#         "كلية العلوم القانونية والاقتصادية والاجتماعيية":"fsjes",
#         "فاس":"fes",
#         "وجدة":"oujda"
#         }
#     for i in d:
#          s=s.replace(d[i],i)
    # return jsonify({'placement':str(result)})
    stopwords_arabic = set(stopwords.words('arabic'))
    stopwords_arabic
    s = ' '.join(word for word in text.split() if word not in stopwords_arabic)
    t=s.split()
    nlp_words=nltk.FreqDist(t)
    dictionnary=dict(nlp_words)
    sort_data = sorted(dictionnary.items(), key=lambda x: x[1], reverse=True)
    new_dict={}
    for i in range(len(sort_data)):
        new_dict[sort_data[i][0]]=sort_data[i][1];
    json_object=json.dumps(new_dict,ensure_ascii=False,indent=4)
    with open("/app/sample.json","w") as outfile:
        outfile.write(json_object)
    inp=open("/app/sample.json","r")
    lines=inp.readlines()
    with open("/app/clean.json","w") as output:
#         output.write("{\n")
        for line in lines[1:-1]:
            if line[-2]!=",":
                line=line+","
            i=line.index(":")
            key=line[:i]
            value=line[i+1:-2]
            txt=f'"text":{key},\n"frequency":{value}'
            text="{\n"+txt+"},\n"
            output.write(text)
#         output.write("}")
    inp=open("/app/clean.json","r")
    lines=inp.read()  
    #return jsonify([lines])
    return lines
#     return s





if __name__ == '__main__':
    app.run(debug=True)
