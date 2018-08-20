import random

class Dictionary:
    def __init__(self):
        self.synonym_dict = {}

        thesaurusfile = open("thesaurustext.txt", "r")
        for line in thesaurusfile:
            # print(line)
            def_close_bracket_idx = None
            def_open_bracket_idx = None
            for index, char in enumerate(line):
                # print(char, end="")
                if char == "]":
                    def_close_bracket_idx = index
                    # print("close_bracket", index)
                elif char == "[":
                    def_open_bracket_idx = index
                    # print("open_bracket", index)

            if def_open_bracket_idx is None or def_close_bracket_idx is None:
                continue

            word_name = line[def_open_bracket_idx+1:def_close_bracket_idx]
            synonyms_text = line[def_close_bracket_idx+1:]
            synonyms = []
            for synonym_str in synonyms_text.split(","):
                synonyms.append(synonym_str.strip())

            synonyms.append(word_name)

            # print(word_name, synonyms)

            if word_name not in self.synonym_dict:
                self.synonym_dict[word_name] = []

            self.synonym_dict[word_name] += synonyms

    def contains(self, word):
        return word in self.synonym_dict

    def synonyms(self, word):
        return self.synonym_dict[word]

def replace_synonyms(text, frequency):
    dict = Dictionary()
    separated_text = []
    flag = "word"
    current = ""
    for char in text:
        if char.isalnum():
            if flag == "word":
                current += char
            else:
                separated_text.append(current)
                current = char
                flag = "word"
        else:
            if flag == "word":
                separated_text.append(current)
                current = char
                flag = "not word"
            else:
                current += char
    separated_text.append(current)

    for index, section in enumerate(separated_text):
        if section.isalnum() and dict.contains(section.lower()):
            if random.uniform(0, 1) < frequency:
                separated_text[index] = random.choice(dict.synonyms(section.lower()))

    return "".join(separated_text)

if __name__ == "__main__":
    print(replace_synonyms(input(), 1))
