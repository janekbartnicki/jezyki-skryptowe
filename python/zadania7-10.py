# zadanie 7
list1 = [[1, 2], {"uni": "polsl"}, ('a', 'b')]
list1.append('hello world')
list1.append(1)
list1.append((0.12, 1))

print(list1)

# zadanie 8
list2 = [{"uni": "polsl"}, ('c', 'd'), [5, 1]]
list2.append('abcdefg')
list2.append(1)
list2.append((3.14, 3))

for element in list2:
    print(element, end='\n')

# zadanie 9
reccuring_elements = [item for item in list1 if item in list2]
print(f'Powtarzające się elementy w obu listach to: {reccuring_elements}')


# zadanie 10

def check_for_element(element):
    appearances_in_list1 = list1.count(element)
    appearances_in_list2 = list2.count(element)

    if (element in list1) and (element in list2):
        return
    elif element in list1:
        print(f'Element {element} pojawia się w liście "list1" {appearances_in_list1} razy.')
    elif element in list2:
        print(f'Element {element} pojawia się w liście "list2" {appearances_in_list2} razy.')


check_for_element((3.14, 3))
