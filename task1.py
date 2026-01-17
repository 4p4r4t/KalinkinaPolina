import json

def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    s = 0.0
    for d in data:
        s += d['score'] * d['weight']
    return round(s, 3)

print(task())
