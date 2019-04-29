
from S01C03 import main, calculate_text_score
f = open("text.txt", "r")

text = str(f.read())
list = []
temp = ""

for t in text:
    if t == ' ' or t == '\n':
        continue
    temp+=t
    if len(temp) == 60:
        list.append(temp)
        temp=""


result = []
for l in list:
    result.append(main(l))

m = 0
i = 0
for r in result:
    if m < calculate_text_score(r):
        m = calculate_text_score(r)

print(m)
print(result[i])
