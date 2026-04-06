list=[1,3,3,4,2,1,1,1]
print("Original list:", list)
def cmn_element(list):
    common_elements = set()
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                common_elements.add(list[i])
    return common_elements

print("Common element:", cmn_element(list))

