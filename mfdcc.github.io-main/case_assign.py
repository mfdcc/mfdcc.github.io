import random
from statistics import mode

# Variables
judges = ["Albert","Krabz","Nomadity","Enneat"]
trial_amount = 50
freq = 6

# Frequent Assignment
def assign(judge, trials, title):
    empl = []
    
    for i in range(1, trials+1):
        # print(f'Trial {i}')
        selected = random.choice(judge)
        empl.append(selected)
    
    # print(f'The trial judge for {title} is {selected}.')
    # return selected
    judge_select = mode(empl)
    print(empl)
    print(f"Method 1: The trial judge for {title} is {judge_select} based on {trials} frequent trials.")

# assign(judges, trial_amount, case)

# def freqtry(value, judgelist, trials, casename):
#     results_list = []
#     # print(judgelist)
#     
#     for i in range(1, value+1):
#         results = assign(judgelist, trials, casename)
#         # print(results)
#         results_list.append(results)
#     
#     judge_select = mode(results_list)
#     print(results_list)
#     print(f"The trial judge for {casename} is {judge_select} based on frequent trials.")
# 
# freqtry(freq, judges, trial_amount, case)

# Weight Assignment (preferable, written by Nomadity)

case = "clutch,faze"

cases_assigned = {
    "Albert": 3,
    "Nomadity": 4,
    "Krabzatonin": 4,
    "SOURCED_V": 4,
    "Arthur_Chen": 5, 
    "shah_khaled": 3
}

def calculate_weights(cases_assigned):
    total_cases = max(cases_assigned.values()) + 1
    return [total_cases - cases_assigned[judges] for judges in cases_assigned]
    
names = list(cases_assigned.keys())
weights = calculate_weights(cases_assigned)
print(f'Weights: {weights}')

# assign = random.choices(names, weights=weights, k=1)[0] - nomadity's first element method
assign = random.choices(names, weights=weights, k=1)[0]
print(f"Method 2: Assign case {case} to: {assign}")












    
    
    