import re

direct_logic_symbol_to_word = { 
    "∃": ["there exists", "there is", "there are", "for some", "there is at least one"],
    "∀": ["for all", "for every", "all"],
    "⟷": ["if and only if"],
    "^": ["and"],
    "v": ["or"],
    "¬": ["not", "it is not the case that", "n't", "nt"],
}

def english_to_predicate(predicate: str) -> str:
    all_blah_are_blah_re = re.compile(r"all ([\w ]+) (are|is)([\w ]+)")
    thing = all_blah_are_blah_re.match(predicate)
    
    if thing is not None:
        before_are = thing.group(1) # all [dogs] are friendly
        after_are = thing.group(3) # all dogs are [friendly]
        
        # sana3oodo ba3d kaleel        
        # before_are = english_to_predicate(before_are)
        # after_are = english_to_predicate(after_are) # are friendly and happy -> freindly ^ happy
        
        return f"∀x ({before_are}(x) → {after_are}(x))"
    else:
        return replace_keywords(predicate)

def replace_keywords(sentance: str) -> str:
    for symbol, key_words in direct_logic_symbol_to_word.items():
        for key_word in key_words:
            word_location = sentance.find(key_word)
            if word_location == -1:
                continue
            if word_location == 0 or sentance[word_location - 1] == " ":
                before_symbol = sentance[:word_location]
                after_symbol = sentance[word_location + len(key_word) :]
                sentance = before_symbol + symbol + after_symbol

    return sentance


if __name__ == "__main__":
    sentance = input("enter english: ")
    logic = english_to_predicate(sentance)
    print(logic)
