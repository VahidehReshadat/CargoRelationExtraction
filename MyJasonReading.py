import json
from pprint import pprint
import re
from nltk.tokenize import word_tokenize

'''

with open('./data/fewrel/train_wiki.json') as json_data:
    d = json.load(json_data)
    print(d)
'''

data_path = './data/fewrel/Train-Test-SCR(LM).TXT'

with open(data_path, 'r', encoding='utf8') as f:
    text = f.readlines()

relations, comments, blanks = [], [], []
sents = list()

#Train next Test
Train_relations_list= ['Arranges', 'Decreses', 'Designate', 'HasCertification', 'HasCharacteristics', 'HasDestination', 'HasOrigin', 'IncludesCapability', 'HasTemperatureRange', 'HasTemperatureRange', 'Hires', 'Increases', 'IsLocatedIn', 'IsPackedIn', 'PartOf', 'Ships', 'IsStoredIn', 'OfferSolution', 'RequiresCapability']
#Train_relations_list= ['Ships', 'IsStoredIn', 'OfferSolution', 'RequiresCapability']
all_relation = dict()
print("Len",len(Train_relations_list))
for m in range (len(Train_relations_list)):  #if Train_relations_list[i]
    each_relationType = list()
    for i in range(int(len(text) / 4)):
        indx=i
        relation = text[4 * indx + 1]
        relation = relation.strip()
        #print(type(relation))
        #print(relation)
        #print(Train_relations_list)

        if (Train_relations_list[m]==relation):

            print("yessss")
            sent = text[4 * indx]
            sent = re.findall("\"(.+)\"", sent)[0]  # Regx101 haechizi e beine "" ast
            # print(sent)


            E1 = re.search('<e1>(.*)</e1>', sent).group(1)
            print(E1)

            E2 = re.search('<e2>(.*)</e2>', sent).group(1)
            print(E2)

            sent = sent.replace('<e1>', '')
            sent = sent.replace('</e1>', '')
            sent = sent.replace('<e2>', '')
            sent = sent.replace('</e2>', '')
            print(sent)
            #sent=sent.split()
            sent=word_tokenize(sent)
            print(sent)

            E1_indx = []
            E1_lis = word_tokenize(E1)
            print(E1_lis)
            for item in E1_lis:
                E1_indx.append(sent.index(item))
                #print("e1", item)

            E2_indx=[]
            E2_lis = word_tokenize(E2)
            print(E2_lis)
            for item in E2_lis:
                E2_indx.append(sent.index(item))
                #print(sent.index(item))




            #sents.append(sent)

            print(relation)
            #relations.append(relation)
            #comment = text[4 * i + 2]
            #blank = text[4 * i + 3]

            #s = 'asdf=5;iwantthis123jasd'


            each_relationType.append({"tokens": sent, "h": [E1.lower(), E1.lower(), [E1_indx]], "t":[E2.lower(), E2.lower(), [E2_indx]]})
            print(each_relationType)

    all_relation.update({Train_relations_list[m].strip(): each_relationType})


print(json.dumps(all_relation))

with open('Test_data.json', 'w') as f:
    json.dump(all_relation, f)


