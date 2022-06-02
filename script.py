
from flask import Flask,request,jsonify
#model = pickle.load(open('model.pkl','rb'))









import string
import pandas as pd
import pyarabic.araby as araby
from pyarabic.araby import is_arabicrange
import nltk
# nltk.download('stopwords')
# from gensim.models import Word2Vec , KeyedVectors
from nltk.corpus import stopwords
df = pd.read_json('/app/arabicPresidentJson.json')
arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations

def remove_punctuations(text):
  for c in punctuations_list:
    text = text.replace(c," ")
  #translator = str.maketrans('', '', punctuations_list)
  return text


df.loc[:,"post_text"] = df.post_text.apply(lambda x : remove_punctuations(x))
from farasa.stemmer import FarasaStemmer
stemmer = FarasaStemmer()

def lemmatization(text):
  # stemmed=stemmer.stem(text)
  
  return stemmer.stem(text)


# df.loc[0:5,"post_text"] = df.post_text.apply(lambda x : lemmatization(x))
# df.head()
s=" عرفت بالمدرسة الوطنية للعلوم التطبيقية على غرار وكلية الطب و الصيدلة مجموعة من الانشطة. المدرسة الوطنية للعلوم التطبيقية"
s=lemmatization(s)

def remove_stopWords(s):
    stopwords_arabic = set(stopwords.words('arabic'))

    s = ' '.join(word for word in s.split() if word not in stopwords_arabic)
    return s

df.loc[:,"post_text"] = df.post_text.apply(lambda x: remove_stopWords(x))

tokenized_postes = [araby.tokenize(post_text, conditions=is_arabicrange) for post_text in df['post_text'].values]

import itertools

flat_list = list(itertools.chain(*tokenized_postes))

# flat_list
new_list=[]
for s in flat_list:
  if s in ["ووجدة","بوجدة","وجدة"]:
    new_list.append("oujda")
  elif s in ["وفاس","بفاس","فاس"]:
    new_list.append("fes")
  elif s in ["وبركان","ببركان","بركان"]:
    new_list.append("berkan")
  else:
    new_list.append(s)
# print(new_list)

text = ' '.join(a for a in new_list)


d={
    "المدرسة الوطنية للعلوم التطبيقية":"ensa",
   "كلية الطب والصيدلة":"fmp",
   "المدرسة الوطنية للتجارة و التسيير":"encg",
   "المدرسة العليا للتكنلوجيا":"est",
   " الكلية متعددة التخصصات بالناظور":"fpn",
   "لكلية متعددة التخصصات بتاوريرت":"fpt",
   "كلية العلوم":"fso",
   "كلية الاداب والعلوم الانسانية":"flsh",
   "كلية العلوم القانونية والاقتصادية والاجتماعيية":"fsjes"
}
for i in d:
    text=text.replace(i,d[i])

text=stemmer.stem(text)
stopwords_arabic = set(stopwords.words('arabic'))
stopwords_arabic
s = ' '.join(word for word in text.split() if word not in stopwords_arabic)
# for i in stopwords_arabic:
#   text=text.replace(i,"")
# text
import random
s=s.split()
s = random.choices(s, k=len(s))
s = ' '.join(a for a in s)
d={
    "المدرسة الوطنية للعلوم التطبيقية":"ensa",
   "كلية الطب والصيدلة":"fmp",
   "المدرسة الوطنية للتجارة و التسيير":"encg",
   "المدرسة العليا للتكنلوجيا":"est",
   " الكلية متعددة التخصصات بالناظور":"fpn",
   "لكلية متعددة التخصصات بتاوريرت":"fpt",
   "كلية العلوم":"fso",
   "كلية الاداب والعلوم الانسانية":"flsh",
   "كلية العلوم القانونية والاقتصادية والاجتماعيية":"fsjes",
   "فاس":"fes",
   "وجدة":"oujda"

}
for i in d:
    s=s.replace(d[i],i)
    # cgpa = request.form.get('cgpa')
    # iq = request.form.get('iq')
    # profile_score = request.form.get('profile_score')
    # input_query = np.array([[cgpa,iq,profile_score]])
    # result = model.predict(input_query)[0]
    # return jsonify({'placement':str(result)})












app = Flask(__name__)
@app.route('/predict',methods=['POST'])
# @app.route('/')
def index():
    a="hello "
    b="world!"
    return s
#     return "Hello world"
# @app.route('/predict',methods=['POST'])
@app.route('/')
def predict():
    # cgpa = request.form.get('cgpa')
    # iq = request.form.get('iq')
    # profile_score = request.form.get('profile_score')
    # input_query = np.array([[cgpa,iq,profile_score]])
    # result = model.predict(input_query)[0]
    # return jsonify({'placement':str(result)})
    return "s"
if __name__ == '__main__':
    app.run(debug=True)
