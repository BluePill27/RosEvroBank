dict = {}
dict[1] = {2: {3: {4: 5}}}
#print(dict[1][2][3])

test_list = [1, 2, 3, 4, 5]
filter_test_list = list(filter(lambda x: x > 2, test_list))
#print(filter_test_list) #[3, 4, 5]

map_test_list = list(map(lambda x: x**3, test_list))
#print(map_test_list) #[1, 8, 27, 64, 125]

from functools import reduce
reduce_test_list = reduce((lambda x, y: x*y), test_list)
#print(reduce_test_list) #120


