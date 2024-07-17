import pandas as pd

new = pd.read_csv("data/french_words.csv")
lst=[]
for value in new["French"]:
    lst.append(value)
print(lst)