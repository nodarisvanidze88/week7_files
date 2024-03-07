import string
def count_word(input_file, output_file):
    word_dict = {}
    with open(input_file, "r") as in_file:
        for line in in_file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()
                word_dict[word] = word_dict.get(word,0)+1
    
    sorted_word_dict = sorted(word_dict.items(), key=lambda x:x[0])

    with open(output_file, "w") as out_file:
        for word, qty in sorted_word_dict:
            out_file.write(f"{word} - {qty}\n")

count_word("text.txt", "result.txt")
