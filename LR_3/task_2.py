participants_first_group= "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(group1, group2, d=','):
    list1 = group1.split(d)
    list2 = group2.split(d)
    participant = set(list1).intersection(set(list2))
    result = sorted(list(participant))
    return result