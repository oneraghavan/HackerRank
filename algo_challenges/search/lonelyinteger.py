N = raw_input()
integers = raw_input().split()
result = 0
integers = [int(x) for x in integers]
for i in integers:
	result = result ^ i
print result
