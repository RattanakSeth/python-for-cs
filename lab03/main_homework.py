"""
Homework
Download a zip file from:
https://github.com/phylypo/khmer-text-data/tree/master/oscar/seg_data
1. Count the words of each file
2. Count the unique keyword of each file
3. Find the common keywords of two files (intersection)
4. Find the unique keywords of two files (Union)
5. Find the keywords of each file doesn’t not exist in another file.
"""

import re
import collections

class File:
    def read_raw_text_file(file_path):
        with open(file_path, 'r') as file: 
            FileContent = file.read()
            file.close()
        return FileContent
    
    def write_text_file(file_path, text: str):
        print("write text with string")
        with open(file_path, 'w') as writefile:
            writefile.write(text)
            writefile.close()
    
    def write_text_file(file_path, texts: list):
        txt: str = ''
        for tx in texts:
            txt += (tx + '\n')

        with open(file_path, 'w') as writefile:
            writefile.write(txt)
            writefile.close()


khmer_text_rar_1 = File.read_raw_text_file("data/oscar_kh_1.txt")

KH_SIGN_REG = r"^[!@#$%^&*()_+.><?។១២៣៤៥៦៧៨៩០:0-9+«»៕]+$"

def extract_word_and_count(word_split) -> tuple:
    words = []
    count: int = 0
    for word in word_split:
        # skip is pattern
        if not re.match(KH_SIGN_REG, word):
            count += 1
            words.append(word)
    
    return (words, count)

# 1. Count the words of the file
word_split = khmer_text_rar_1.split()
words, count = extract_word_and_count(word_split)
File.write_text_file("output/oscar_kh_1_word.txt", words)


# 2. count unique keyword of each file

# cover list to set
unique_set = set(words)
File.write_text_file("output/oscar_kh_1_unique_word.txt", unique_set)

# 3. The common keywords of two files
khmer_text_rar_2 = File.read_raw_text_file("data/oscar_kh_2.txt")
word_split_2 = khmer_text_rar_2.split()
# word_, count = extract_word_and_count(word_split)
File.write_text_file("output/oscar_kh_2_word.txt", word_split_2)

# cover list to set
unique_set_2 = set(words)
File.write_text_file("output/oscar_kh_2_unique_word.txt", unique_set_2)


result = collections.Counter(word_split) & collections.Counter(word_split_2)

intersected_list = list(result.elements())

def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

unionWords = Union(word_split, word_split_2)
uniqueUnion = set(unionWords)

File.write_text_file('output/union_words.txt', unionWords)
File.write_text_file('output/unique_union_words.txt', uniqueUnion)


print("1. Total of the word is %d" % (count))
print("2. Unique word %d" %(len(unique_set)))
print("3. intersect list ============")
print(intersected_list)
print("4. Union -> see in output")
# print(unionWords)
print("5. Unique of union -> see in output")
# print(uniqueUnion)



