
from S01C03 import main, calculate_text_score
fp = open("text.txt", "r")
list = fp.read().split("\n") # create a list containing all lines
fp.close()

result = [main(l) for l in list]

m = 0
i = 0

for r in result:
    if m < calculate_text_score(r):
        m = calculate_text_score(r)
        i = result.index(r)

print(m)
print(result[i])
