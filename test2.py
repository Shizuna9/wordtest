import re
import random

#単語ソース
chinese='china.txt'
japanese='japan.txt'

with open(chinese) as f:
    data1=f.read()
    ch=re.findall('.+',data1)
with open(japanese) as f:
    data2=f.read()
    ja=re.findall('.+',data2)

chinese=[]
for word in ch:
    m=re.sub('\n','',word)
    chinese.append(m)

japanese=[]
for word in ja:
    n=re.sub('\n','',word)
    japanese.append(n)

word_dict=dict(zip(chinese, japanese))

#テスト内容
n_test=50
n_question=30

for test_num in range(n_test):
    with open('中国語単語テスト_{:02d}.txt'.format(test_num + 1),'w') as f:
         f.write('第{}回単語テスト\n\n'.format(test_num + 1
                 ))

    #問題生成
         for question_num in range(n_question):

            question_word=random.choice(ch)
            answer=word_dict[question_word]

            ja_copy = ja.copy()
            ja_copy.remove(answer)
            worng_answers=random.sample(ja_copy,3)

            answer_options = [answer]+worng_answers
            random.shuffle(answer_options)
    
    #問題表示法
            f.write('問{}.{}　　(答え  )\n'.format(question_num+1,question_word))

            for i in range(4):
                f.write('{}.{}\n'.format(i + 1, answer_options[i]))
            f.write('\n')
