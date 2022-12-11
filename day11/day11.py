import yaml
from yaml.loader import FullLoader
import operator
import math
from copy import deepcopy

ops = {
    '+' : operator.add,
    '*' : operator.mul
}

#Brute forced input yaml.TODO update the input into required yaml

# with open("input.yaml","r") as f, open("input_updated.yaml","w") as fup:
#     for line in f:
#         for word in ["throw to", "divisible by","If"]:
#             line=line.replace(word, "")
#             line=line.replace("new = old ","")
#         fup.write(line)


with open("input.yaml", "r") as f:
    file_dict = yaml.load(f,Loader=FullLoader)

part_2_dict= deepcopy(file_dict)

def monkey_business(file_dict,range_value,part="part_1"):
    # Big integer multiplication -- Consider product of all divisible by X
    part2_mod = math.prod([value["Test"] for value in file_dict.values()]) if part=="part_2" else 1

    for i in range(range_value):
        for key, value in file_dict.items():
            file_dict[key].setdefault("inspected",0)
            for original_worry in value["Starting items"]:
                worry_level=int(original_worry)
                operation_sign,operation_value=value["Operation"].split(" ")[3],value["Operation"].split(" ")[4]
                if operation_value =="old":
                    worry_level=ops[operation_sign](worry_level,worry_level)
                else:
                    worry_level=ops[operation_sign](worry_level,int(operation_value))
                worry_level=worry_level%part2_mod if part=="part_2" else worry_level//3
                if worry_level%int(value["Test"])==0:
                    file_dict[value[True]]["Starting items"].append(worry_level)
                else:
                    file_dict[value[False]]["Starting items"].append(worry_level)
                file_dict[key]["inspected"]+=1
            file_dict[key]["Starting items"].clear()

    return math.prod(
        sorted([v["inspected"] for v in file_dict.values()])[-2:]
    )
    

print(f"Part_1: {monkey_business(file_dict,20)}")
print(f"Part_2: {monkey_business(part_2_dict,10_000,'part_2')}")
