import json
with open("C://Users//srijan.tirunagari//Downloads//words.json", "r",encoding="utf-8") as file:
    data_1=file.read()
data = json.loads(data_1)
dict={}
dict_1={}
for i in data:    
    key=i["word"]
    temp=i["meanings"]
    for j in temp:
        list=[]
        key_2=j["partOfSpeech"]
        value_2=j["definitions"]

        for l in value_2:
            list.append(l["definition"])
        print(list)
        dict[key_2]=list
        print(dict)
    

    dict_1[key]=dict
    print(dict_1)
with open("C://Users//srijan.tirunagari//Downloads//word_details.json","w") as file:
    val0=file.write(json.dumps(dict_1))
    print(val0)

