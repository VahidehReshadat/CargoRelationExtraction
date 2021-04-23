import json
from pprint import pprint
import re
from nltk.tokenize import word_tokenize
import nltk


'''

with open('./data/fewrel/train_wiki.json') as json_data:
    d = json.load(json_data)
    print(d)
'''

data_path = './data/fewrel/Bi-jahat/FewRel(SCR-L)/Train-Test-SCR(L).TXT'

with open(data_path, 'r', encoding='utf8') as f:
    text = f.readlines()

relations, comments, blanks = [], [], []
sents = list()

#Train next Test
#Train_relations_list= ['Arranges', 'Decreses', 'Designate', 'HasCertification', 'HasCharacteristics', 'HasDestination', 'HasOrigin', 'IncludesCapability', 'HasTemperatureRange', 'HasTemperatureRange', 'Hires', 'Increases', 'IsLocatedIn', 'IsPackedIn', 'Other', 'PartOf', 'Ships', 'IsStoredIn', 'OfferSolution', 'RequiresCapability']
#Train_relations_list= ['Arranges', 'Decreses', 'Designate', 'HasCertification', 'HasCharacteristics', 'HasDestination', 'HasOrigin', 'IncludesCapability', 'HasTemperatureRange', 'HasTemperatureRange', 'Hires', 'Increases', 'IsLocatedIn', 'IsPackedIn', 'Other']
Train_relations_list= ['PartOf', 'Ships', 'IsStoredIn', 'OfferSolution', 'RequiresCapability']

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

            e1_st = re.findall(r'<e1>\w+', sent)
            e1_end = re.findall(r'\w+</e1>', sent)
            e2_st = re.findall(r'<e2>\w+', sent)
            e2_end = re.findall(r'\w+</e2>', sent)
            print("len e1", len(e1_end))
            print("len e2", len(e2_end))
            e1_st = (''.join(str(x) for x in e1_st))
            e1_end = (''.join(str(x) for x in e1_end))
            e2_st = (''.join(str(x) for x in e2_st))
            e2_end = (''.join(str(x) for x in e2_end))
            print("len e1", len(e1_end))
            print("len e2", len(e2_end))

            print(type(sent))
            print(type(e2_st))
            print(e1_st)
            print(e2_st)
            print(e1_end)
            print(e2_end)

            sub_be1 = sent.find(e1_st)
            print(sub_be1)
            sent = sent.replace('<e1>', '')
            sub_ee1 = sent.find(e1_end)
            print(sub_ee1)
            sent = sent.replace('</e1>', '')
            #sub_ee1 = sub_ee1 + (len(e1_end) + 1)

            e1_end = e1_end.replace('</e1>', '')
            sub_ee1 = sub_ee1 + (len(e1_end))

            sub_be2 = sent.find(e2_st)
            print(sub_be2)
            sent = sent.replace('<e2>', '')
            sub_ee2 = sent.find(e2_end)
            print(sub_ee2)
            sent = sent.replace('</e2>', '')

            e2_end = e2_end.replace('</e2>', '')
            sub_ee2 = sub_ee2 + (len(e2_end))


            tokenizer = nltk.tokenize.TreebankWordTokenizer()

            print(tokenizer.span_tokenize(sent))
            # sub_b, sub_e = 4, 14  # substring begin and end
            E1_indx = [i for i, (b, e) in enumerate(tokenizer.span_tokenize(sent)) if b >= sub_be1 and e <= sub_ee1]
            E2_indx = [i for i, (b, e) in enumerate(tokenizer.span_tokenize(sent)) if b >= sub_be2 and e <= sub_ee2]

            print([i for i, (b, e) in enumerate(tokenizer.span_tokenize(sent)) if b >= sub_be1 and e <= sub_ee1])
            print([i for i, (b, e) in enumerate(tokenizer.span_tokenize(sent)) if b >= sub_be2 and e <= sub_ee2])

            #relations.append(relation)
            #comment = text[4 * i + 2]
            #blank = text[4 * i + 3]

            #s = 'asdf=5;iwantthis123jasd'v
            sent=word_tokenize(sent.lower())

            each_relationType.append({"tokens": sent, "h": [E1.lower(), E1.lower(), [E1_indx]], "t":[E2.lower(), E2.lower(), [E2_indx]]})
            print(each_relationType)

    all_relation.update({Train_relations_list[m].strip(): each_relationType})


print(json.dumps(all_relation))

with open('4New_Test.json', 'w') as f:
    json.dump(all_relation, f)


