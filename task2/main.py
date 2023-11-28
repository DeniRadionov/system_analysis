import csv

def task(graph: str) -> list:

    result = [[], [], [], [], []]

    reader = csv.reader(graph.split('\n'))
    save = []
    for i in reader:

        s1, s2 = map(int, i)

        save.append((s1, s2))

        result[0].append(s1)

        result[1].append(s2)

    for i in save:
        s1, s2 = i

        if s2 in result[0]:
            result[2].append(s1)

        if s1 in result[1]:
            result[3].append(s2)

        if result[0].count(s1) > 1:
            result[4].append(s2)

    for i in range(5):
        result[i] = list(set(result[i]))

    return result

# Пример 
csv_string = "1,2\n1,3\n3,4\n3,5"
result = task(csv_string)
print(result)
