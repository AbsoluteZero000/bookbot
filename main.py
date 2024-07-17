
def main():
    with open("books/frankenstein.txt") as f:
        return f.read()
def countwords(filename):
    with open(filename) as f:
        print(len(f.read().split()))

def countCharacters(text):
    text = text.lower()
    dic = {}
    for char in text:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    return dic

def printCount(dic):
    for k, v in dic.items():
        print(f"the '{k}' character was found {v} times")

if __name__ == "__main__":
    countwords("books/frankenstein.txt")
    printCount(countCharacters(main()))
