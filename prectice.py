nums = [1, 33, 55, 77]

names = ['navin', 'nahid', 'nadia']
plays=['football', 'cricket', 'ragbi' ]
loves=dict(zip(names,plays))
print(loves)
loves['monika']='hidenseek'
print(loves)
del loves['monika']
print(loves)
all = [nums, names]
nums.append(45)
nums.append(45)

names.pop()
nums.extend([22, 44, 56, 77, 89, 1])

print(max(nums))

nums.sort()

print(nums)
print(names)
print(all)

tup = (1, 22, 34, 22, 35, 66, 40)
print(tup.count(33))
print(tup)

data = {1: 'ornob', 2: 'mou', 5: 'trina'}
print(data.get(3, 'not found'))
