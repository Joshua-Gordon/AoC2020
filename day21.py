import sys
import re
from constraint import *

def parse_food(food):
    if "(" in food:
        pos = food.find("(")
        ingr = food[:pos-1].split(" ")
        allergenstring = food[pos+1+len("contains "):-1].split(", ")
        return ingr,allergenstring
    else:
        return food.split(" "),None

def part2(data):
    pass

def day21(data):
    allergens = set()
    ingredients = set()
    freq = {}
    foods = []
    for food in data:
        ingr,allerg = parse_food(food)
        print(ingr)
        print(allerg)
        foods.append((ingr,allerg))
        for a in allerg:
            allergens.add(a)
        for i in ingr:
            ingredients.add(i)
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    allergy_candidates = {}
    for a in allergens:
        allergy_candidates[a] = set()
        candidates = None
        for (ingr,alls) in foods:
            if a in alls:
                if candidates is None:
                    candidates = set(ingr)
                else:
                    ingrset = set(ingr)
                    candidates = candidates.intersection(ingrset)
        print(a)
        print(candidates)
        for c in candidates:
            allergy_candidates[a].add(c)
    total = 0
    for i in ingredients:
        if i not in allergy_candidates.values():
            total += freq[i]
    print(total)
    p = Problem()
    for a in allergy_candidates:
        p.addVariable(a,list(allergy_candidates[a]))
    p.addConstraint(AllDifferentConstraint())
    sol = p.getSolutions()[0]
    s = ""
    for a in sorted(list(allergens)):
        print(a)
        s += sol[a]+","
    print(s)

if __name__ == "__main__":
    data = [s.strip() for s in open(sys.argv[1]).readlines()]
    day21(data)
