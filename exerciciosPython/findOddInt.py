# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def define_dic(seq):
    dic = {}
    for number in seq:
        if number not in dic:
            dic[number] = 1
        else: 
            dic[number] += 1
    return dic
            
def find_it(seq):
    dic = define_dic(seq)
    for x in dic:
        if dic[x] % 2 != 0:
            return x

# melhor prática
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i