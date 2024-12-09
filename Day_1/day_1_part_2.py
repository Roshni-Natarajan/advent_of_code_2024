# input = """
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# """
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

count_dict = {}

for i in right:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1


similarity_score = 0
for i in left:
    if i in count_dict:
        similarity_score += i * count_dict[i]

print(similarity_score)
