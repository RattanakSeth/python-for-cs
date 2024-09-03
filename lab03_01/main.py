import json
import re

class File:
    def read_json_file(file_path):
        with open(file_path, "r") as file:
            FileContent = json.load(file)
            # print(FileContent)
            file.close()
        return FileContent["data"]
    
    def read_raw_text_file(file_path):
        with open(file_path, 'r') as file: 
            FileContent = file.read()
            file.close()
        return FileContent
    
    def write_text_file(file_path, text: str):
        with open(file_path, 'w') as writefile:
            writefile.write(text)
            writefile.close()


"""
Using raw_text.txt to answer the following questions:
"""
def read_json_file_and_ans():
    data = File.read_json_file('data/data.json')
    countries: list = []
    infected: int = 0
    recovered: int = 0
    the_most_effected_country: list = [data[0]]
    less_effected_country: list = [data[0]]
    # print(the_most_effected_country)

    for idx, item in enumerate(data):
        if (item["country"]):
            countries.append(item['country'])
        infected += item["infected"]
        recovered += item["recovered"]

        # print(data[idx]["infected"])
        if (the_most_effected_country[0]["infected"] < data[idx]["infected"]):
            the_most_effected_country[0] = item
        
        if (less_effected_country[0]["infected"] > data[idx]["infected"]):
            less_effected_country[0] = item

    avg_of_infected = infected / len(data)
    avg_of_recovered = recovered / len(data)

    print("========== Answer =========")
    print("1. There are %d countries in this data" % (len(countries)))
    print("2. Mean of infected is %f" % (avg_of_infected))
    print("3. Mean of recovered is %f" % (avg_of_recovered))
    print("4. The most effected country %s" % (the_most_effected_country[0]["country"]))
    print("5. The less effected country %s" % (less_effected_country[0]["country"]))

# read_json_file_and_ans()

"""
❖ Using raw_text.txt to answer the following questions:
Using RegEx to:
1. Extract all sentences which contain English alphabets?
2. Extract only Khmer sentences (no English alphabets)?
3. Extract only English words?
4. Remove all English words from the text?
5. Find all Khmer numbers (ex. ២០២១, ២០…)
"""


rawText = File.read_raw_text_file('data/raw_text.txt')

# Regular expression for Khmer character
CONSONANTS_SET = set("\u1780\u1781\u1782\u1783\u1784\u1785\u1786\u1787\u1788\u1789\u178a\u178b\u178c\u178d\u178e\u178f\u1790\u1791\u1792\u1793\u1794\u1795\u1796\u1797\u1798\u1799\u179a\u179b\u179c\u179d\u179e\u179f\u17a0\u17a1\u17a2") # \u1780-\u17a2
INDEPENDENT_VOWELS_SET = set("\u17a3\u17a4\u17a5\u17a6\u17a7\u17a8\u17a9\u17aa\u17ab\u17ac\u17ad\u17ae\u17af\u17b0\u17b1\u17b2\u17b3") # \u17a3-\u17b3
VOWELS_SET = set("\u17b6\u17b7\u17b8\u17b9\u17ba\u17bb\u17bc\u17bd\u17be\u17bf\u17c0\u17c1\u17c2\u17c3\u17c4\u17c5\u17c6\u17c7\u17c8") # \u17b6-\u17c8
COENG = "\u17d2"
US_SET = set("\u17c9\u17ca\u17cb\u17cc\u17cd\u17ce\u17cf\u17d0\u17d1")
PUNCT_SET = set("\u17d4\u17d5\u17d6\u17d8\u17d9\u17da\u17dc")
KM_SYMBOLS_SET = set("\u19e0\u19e1\u19e2\u19e3\u19e4\u19e5\u19e6\u19e7\u19e8\u19e9\u19ea\u19eb\u19ec\u19ed\u19ee\u19ef\u19f0\u19f1\u19f2\u19f3\u19f4\u19f5\u19f6\u19f7\u19f8\u19f9\u19fa\u19fb\u19fc\u19fd\u19fe\u19ff")
KM_LEK_ATTAK_SET = set("\u17F0\u17F1\u17F2\u17F3\u17F4\u17F5\u17F6\u17F7\u17F8\u17F9")

# print(rawText)
kh_text: str = ''
eng_text: str = ''

CONSONANTS_REGEX = r"\u1780\u1781\u1782\u1783\u1784\u1785\u1786\u1787\u1788\u1789\u178a\u178b\u178c\u178d\u178e\u178f\u1790\u1791\u1792\u1793\u1794\u1795\u1796\u1797\u1798\u1799\u179a\u179b\u179c\u179d\u179e\u179f\u17a0\u17a1\u17a2"

# print(re.match(CONSONANTS_REGEX, 'ក'.encode('utf-8')))
ENG_REGEX = r"^[A-Za-z][A-Za-z0-9]*$"
# KH_REGEX = r"^[ក-អ][ា-េាះ]"
KH_NUMBER = r"[០១២៣៤៥៦៧៨៩]+"

for txt in rawText:
    if re.match(ENG_REGEX, txt):
      eng_text += txt
    
    else:
       kh_text += txt

def getKhmerNumbers(str):
   array = re.findall(KH_NUMBER, str)
   return array

# khmer_numbers = re.search(KH_NUMBER, rawText)
print("============ Khmer number =========")
arrayText = getKhmerNumbers(rawText)
print(arrayText)

# print(kh_text)

File.write_text_file("output/english_text.txt", eng_text)
File.write_text_file("output/khmer_text.txt", kh_text)
      


# str_version = 'ការរក'
# unicode_version = str_version.encode('utf-8')
# print(unicode_version)
# print('ក'.encode('utf-8'))

def encode(text: str):
  
  if "\n" in text:
    raise Exception("Newline characters are not allowed.")
  
  for match in re.finditer(r"([\u1780-\u17ff ]+)|([^\u1780-\u17ff ]+)", text):
    
    if match.group(2) is not None:
      yield (match.group(2), "NS")
      continue
    
    for char in match.group(1):
      if char in CONSONANTS_SET:
        yield (char, "C")
        continue
      
      if char in INDEPENDENT_VOWELS_SET:
        yield (char, "IV")
        continue
      
      if char in VOWELS_SET:
        yield (char, "V")
        continue
    
      if char in US_SET:
        yield (char, "US")
        continue
      
      if char in PUNCT_SET:
        yield (char, "END")
        continue
        
      if char in KM_SYMBOLS_SET:
        yield (char, "LN")
        continue
      
      if char in KM_LEK_ATTAK_SET:
        yield (char, "AN")
        continue
      
      if char == " ":
        yield ("\u200b", "ZS")
        continue
      
      if char == COENG:
        yield (char, "SUB")
        continue
      
      yield (char, "NS")


# print(encode("តើអ្នកកំពុងគិតអ្វី?"))

# if char in CONSONANTS_SET:
#     print(char)
    # yield (char, "C")
# print('ក'.decode('utf-8'))

# for txt in rawText:
#     print("text: ", txt)