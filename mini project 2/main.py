from english_to_predicate import english_to_predicate
from predicate_to_english import predicate_to_english

print("for english choose e | for logic choose l")
choice = input("choose ")

if choice == "e":
    sentance = input("enter english: ")
    logic = english_to_predicate(sentance)
    print(logic)
elif choice == "l":
    sentance = input("enter logic: ")
    english = predicate_to_english(sentance)
    print(english)
else:
    print("invalid choice")