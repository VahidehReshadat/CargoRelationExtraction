import re
from nltk.tokenize import word_tokenize
import nltk

#sent="<e1>Dnata Ground Handler</e1> provides <e2>passenger, baggage, ramp, and cargo handling services</e2> to many major airlines from around the world."
#sent="<e1>IATA</e1> receives the cargo from forwarders, build up unit load devices and <e2>load or unload the airplane</e2>, break down unit load devices and ensure the transfer of the incoming cargo to the forwarder."
#sent="As part of UK airline strategy to offers customers with wider choice of special cargo solutions, <e1>UK airline</e1> approves the <e2>shipment of temperature-sensitive life-enhancing healthcare products</e2>, Perishable goods, live animals and gold."
#sent="Air Cargo Community Frankfurt, executive at Fraport and vice chairwoman, Anke Giesen says with this new concept of <e1>reliability and speed</e1>, we are able to decrease the <e2>complexity of ordering processes</e2> by steering the flow of information of all participants digitally."
#sent="The <e1>Free On Board</e1> of the shipments, is organized by <e2>Panalpina</e2> based on the user requirements they request from their shippers; therefore, shipper experts won’t be consulted."
#sent="The facility is located at <e1>Shanghai Pudong International Airport</e1> in <e2>China</e2> and FedEx says it applies cutting-edge technologies and innovation to enhance operational efficiency."
sent="Handling special cargo to the <e1>Netherlands</e1> is done via UPS Airlines <e2>RU12</e2> that connects sellers and buyers for any specific commodity."
e1_st = re.findall(r'<e1>\w+', sent)
e1_end = re.findall(r'\w+</e1>', sent)
e2_st = re.findall(r'<e2>\w+', sent)
e2_end = re.findall(r'\w+</e2>', sent)
print("len e1", len(e1_end))
print("len e2", len(e2_end))
e1_st=(''.join(str(x) for x in e1_st))
e1_end=(''.join(str(x) for x in e1_end))
e2_st=(''.join(str(x) for x in e2_st))
e2_end=(''.join(str(x) for x in e2_end))
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
print(e1_end)
print("Senttt", sent)
sub_ee1 = sent.find(e1_end)
print(sub_ee1)
sent = sent.replace('</e1>', '')
e1_end = e1_end.replace('</e1>', '')

#sub_ee1 = sub_ee1+(len(e1_end)+1)
sub_ee1 = sub_ee1+(len(e1_end))

sub_be2 = sent.find(e2_st)
print(sub_be2)
sent = sent.replace('<e2>', '')
sub_ee2 = sent.find(e2_end)
print(sub_ee2)
sent = sent.replace('</e2>', '')

print("Print len e2_len va khhodash", e2_end, len(e2_end))

e2_end = e2_end.replace('</e2>', '')

sub_ee2 = sub_ee2+(len(e2_end))

tokenizer = nltk.tokenize.TreebankWordTokenizer()

print(tokenizer.span_tokenize(sent))
#sub_b, sub_e = 4, 14  # substring begin and end

print("*******************************")
print()



print([i for i, (b, e) in enumerate(tokenizer.span_tokenize(sent)) if b >= sub_be1 and e <= sub_ee1])
print([i for i, (b, e) in enumerate(tokenizer.span_tokenize(sent)) if b >= sub_be2 and e <= sub_ee2])

#print(sent.index(str(m1)))
