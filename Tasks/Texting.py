k2t = {
    "0": " ",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

t2k = {}
for k in k2t:
    coef = 1
    for alp in k2t[k]: t2k[alp] = k*coef;coef+=1


def text2keys(text):
    text = text.replace('.', '').lower()
    return " ".join(list(map(lambda x : t2k[x], text)))
def keys2text(keys):
    return "".join(list(map(lambda x : k2t[x[0]][len(x)-1], keys.split())))

exec(input().strip())
