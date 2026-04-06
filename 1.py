from pandas import DataFrame

# true if that travler is telling the truth
a: bool
b: bool
c: bool
d: bool
e: bool
f: bool

# translating the statements of each traveler to prepositional logic

def statement_a():
    return not b

def statement_b():
    return c and d

def statement_c():
    return not a or not e

def statement_d():
    return (a and b) or (not a and not b)

def statement_e():
    return ((not a and not b) or (not a and not c) or (not a and not d) or (not a and not e) or (not a and not f) 
            or (not b and not c) or (not b and not d) or (not b and not e) or (not b and not f) 
            or (not c and not d) or (not c and not e) or (not c and not f) 
            or (not d and not e) or (not d and not f) 
            or (not e and not f))

def statement_f():
    return d and not e


# first element of tuple represents combination of truth-teller
# and lying travelers, while the second element represents wheather
# the system is consistant
truth_and_lie_record: list[tuple[list[bool], bool]] = []


# nested loops to generate all combinations of lying and 
# truth-telling travelers
for a in (True,False):
    for b in (True,False):
        for c in (True,False):
            for d in (True, False):
                for e in (True, False):
                    for f in (True, False):
                        
                        # if the statement a traveler sais is true, then
                        # he must be truthful, and vice versa
                        traveler_consistancies =[
                            statement_a() == a,
                            statement_b() == b,
                            statement_c() == c,
                            statement_d() == d,
                            statement_e() == e,
                            statement_f() == f
                        ]
                        
                        truth_and_lie_record.append((
                            [a, b, c, d, e, f],
                            False not in traveler_consistancies
                        ))
                        
                        
truth_table = DataFrame(
    {
        "a": [travelers[0][0] for travelers in truth_and_lie_record],
        "b": [travelers[0][1] for travelers in truth_and_lie_record],
        "c": [travelers[0][2] for travelers in truth_and_lie_record],
        "d": [travelers[0][3] for travelers in truth_and_lie_record],
        "e": [travelers[0][4] for travelers in truth_and_lie_record],
        "f": [travelers[0][5] for travelers in truth_and_lie_record],
        "door is opened": [x[1] for x in truth_and_lie_record]
    }
)

print (truth_table)
truth_table.to_csv("1 truth table.csv")

print ("the unque solution to open the door is: ")
working_solutions = truth_table[truth_table["door is opened"]]
print (working_solutions)
