N = raw_input()
integers = raw_input().split()
integers = map(int,integers)
integers.sort()
diffs = []
for i in range(len(integers)-1):
	diffs.append(integers[i+1] - integers[i])
indices = [i for i, x in enumerate(diffs) if x == min(diffs)]
results = []
for i in indices:
	results.append(integers[i])
	results.append(integers[i+1])
print " ".join(map(str, results))