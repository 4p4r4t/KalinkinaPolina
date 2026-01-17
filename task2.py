def find_common_participants(a, b, sep=','):
    s1 = set(a.split(sep)) if a else set()
    s2 = set(b.split(sep)) if b else set()
    return sorted(s1 & s2)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
