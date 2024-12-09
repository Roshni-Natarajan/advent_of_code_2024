# input
with open("sample_input", "r") as f:
    input = f.read()

input_list = input.strip().split("\n")
# print(input_list)

rev_list = [''.join(i) for i in list(zip(*input_list))]
# print(rev_list)

XMAS_STR = "MAS"
REV_STR = "SAM"

def parse_input():
    final_count = 0

    # find the diagonal occurences from left to right
    print("diagonal occurences")
    for i in range(len(input_list) - 2):
        for j in range(len(input_list[i]) - 2):
            chr_str = input_list[i][j] + input_list[i+1][j+1] + input_list[i+2][j+2]
            if chr_str == XMAS_STR or chr_str == REV_STR:
                across_str = input_list[i][j+2] + input_list[i+1][j+1] + input_list[i+2][j]
                if across_str == XMAS_STR or across_str == REV_STR:
                    final_count += 1

    return final_count


count = parse_input()
print(count)