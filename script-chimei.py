import markovify
import MeCab

# Load file
text_file = open("chimei.txt", "r", encoding="utf-8")
text = text_file.read()

def n_gram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]
# Parse text using MeCab
parsed_text = n_gram(text, 1)
parsed_text = ' '.join(parsed_text)

# Build model
text_model = markovify.NewlineText(parsed_text, state_size=2, well_formed=False)


# Output
for _ in range(10):
    sentence = None
    while sentence == None:
        sentence = text_model.make_short_sentence(7).replace(' ', '')
    print(sentence)