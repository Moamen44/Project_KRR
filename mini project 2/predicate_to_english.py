from logic_keywords import logic_symbol_word_dict
import re


def replace_symbols(logic: str) -> str:
    new = logic
    for symbol, key_words in logic_symbol_word_dict.items():
        new = new.replace(symbol, " " + key_words[0] + " ")
    return new


def implication_to_english(logic: str) -> str:
    predicate_re = re.compile(r"(.+)→(.+)")
    matches = predicate_re.match(logic)
    if matches is not None:
        cause = matches.group(1)
        effect = matches.group(2)
        return f"if {cause} then {effect}"
    return logic


def special_case_all(logic: str) -> str:
    logic = logic.replace(" ", "")
    logic = logic.replace("(x)", "")
    special_case_re = re.compile(r"∀\w\((.+)→(.+)\)")
    matches = special_case_re.match(logic)
    if matches is not None:
        before_arrow = replace_symbols(matches.group(1))
        after_arrow = replace_symbols(matches.group(2))
        return f"All {before_arrow} are {after_arrow}"
    return logic


def predicate_to_english(logic: str) -> str:
    english = special_case_all(logic)
    if english != logic:
        return english
    else:
        english = implication_to_english(logic)
        english = replace_symbols(english)
        return english


if __name__ == "__main__":
    sentance = input("enter english: ")
    english = predicate_to_english(sentance)
    print(english)
