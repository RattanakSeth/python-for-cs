import json

class File:
    def read_json_file(file_path):
        with open(file_path, "r") as file:
            FileContent = json.load(file)
            # print(FileContent)
            file.close()
        return FileContent["data"]
    
data = File.read_json_file('data/data.json')

"""
Using raw_text.txt to answer the following questions:
"""
def read_json_file_and_ans():
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


"""
❖ Using raw_text.txt to answer the following questions:
Using RegEx to:
1. Extract all sentences which contain English alphabets?
2. Extract only Khmer sentences (no English alphabets)?
3. Extract only English words?
4. Remove all English words from the text?
5. Find all Khmer numbers (ex. ២០២១, ២០…)
"""

