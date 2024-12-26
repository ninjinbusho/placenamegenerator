import random

text_file = open("input.txt", "r", encoding="utf-8")
text = text_file.read()

def n_gram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]

export = n_gram(text, 1)

for _ in range(10):
    a = "\n"
    b = "\n"
    while a == "\n":
       a = export[random.randint(1, len(export))]
    while b == "\n":
        b = export[random.randint(1, len(export))]
    print(a + b)