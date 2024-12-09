with open("sample_input", "r") as f:
    input = f.read()

left = []
right = []
input_list = input.strip().split("\n")
for line in input_list:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))

left.sort()
right.sort()
distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)
