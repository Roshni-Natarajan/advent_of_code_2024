# input
with open("sample_input", "r") as f:
    input = f.read()

input_list = input.strip().split("\n")
# print(input_list)

rev_list = [''.join(i) for i in list(zip(*input_list))]
# print(rev_list)

XMAS_STR = "XMAS"
REV_STR = "SAMX"

def parse_input():
    final_count = 0
    print("actual matrix")
    # find the horizontal occurences (actual and backwards)
    for line in input_list:
        # find the horizontal and backwards occurences
        final_count += line.count(XMAS_STR)
        final_count += line.count(REV_STR)

    print("transposed matrix")
    # find the vertical occurences (actual and backwards)
    for line in rev_list:
        final_count += line.count(XMAS_STR)
        final_count += line.count(REV_STR)


    # find the diagonal occurences from left to right
    print("diagonal occurences")
    for i in range(len(input_list) - 3):
        for j in range(len(input_list[i]) - 3):
            chr_str = input_list[i][j] + input_list[i+1][j+1] + input_list[i+2][j+2] + input_list[i+3][j+3]
            # print(chr_str)
            if XMAS_STR  == chr_str:
                # print(input_list[i])
                final_count += 1

            if REV_STR == chr_str:
                # print(input_list[i])
                final_count += 1

    # find the diagonal occurences from right to left
    print("reverse check for diagonal")
    for i in range(len(input_list) - 3):
        for j in range(len(input_list[i]) - 1, 2, -1):
            chr_str = input_list[i][j] + input_list[(i+1)][(j-1)] + input_list[(i+2)][(j-2)] + input_list[(i+3)][(j-3)]
            # print(chr_str)
            if XMAS_STR  == chr_str:
                # print(input_list[i])
                final_count += 1

            if REV_STR == chr_str:
                # print(input_list[i])
                final_count += 1
    return final_count


count = parse_input()
print(count)