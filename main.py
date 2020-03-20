#author @imOmesh
# s = input().split(' ')
# str1 = s[0]
# # str2 = s[1]
# str1 = 'aaaaabbccdd'
# str2 = 'yyyyyyxxxxx'

def checkMapping(str_dict_1, str_dict_2):
    if not str_dict_1 and not str_dict_2:
        return True

    sorted_dict = sorted(list(str_dict_1.items()), key=lambda x: -x[1])
    if not sorted_dict:
        return False
    lar_occ = sorted_dict[0]
    get_possible = [(item[1], item[0]) for item in str_dict_2.items() if item[1] >= lar_occ[1]]
    if not get_possible:
        return False
    def getMin(elements):
        minimum = float('inf')
        for element in elements:
            if element[0] < minimum:
                out = element
                minimum = element[0]
        return out


    element = getMin(get_possible)

    new_str_dict_1 = str_dict_1.copy()
    del new_str_dict_1[lar_occ[0]]
    new_str_dict_2 = str_dict_2.copy()
    new_str_dict_2[element[1]] -= lar_occ[1]
    if new_str_dict_2[element[1]] == 0:
        del new_str_dict_2[element[1]]
    temp = checkMapping(new_str_dict_1, new_str_dict_2)
    if temp:
        return True
    return False
if __name__ == '__main__':
    import sys
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    from collections import defaultdict

    def makeDict(string):
        str_map = defaultdict(int)
        for char in string:
            str_map[char] += 1
        return str_map

    str_dict_1 = makeDict(s1)
    str_dict_2 = makeDict(s2)
    if checkMapping(str_dict_1, str_dict_2) :
        print ('true')
    else :
        print ('false')