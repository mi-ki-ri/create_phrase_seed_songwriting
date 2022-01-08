import random
import sys

oto_list = [
    "ド",
    "レ♭",
    "レ",
    "ミ♭",
    "ミ",
    "ファ",
    "ソ♭",
    "ソ",
    "ラ♭",
    "ラ",
    "シ♭",
    "シ"
]

natural_list = [
    0,
    2,
    4,
    5,
    7, 
    9,
    11,
]

alter_list = [
    1,
    3,
    6,
    8,
    10,
]

major_list = [
    0,
    4,
    7,
]

minor_list = [
    9,
    0,
    4,
]


def main(is_major, ans_num):
    my_list = []
    ans = []
    if is_major:
        my_list.extend(major_list)
        my_list.extend(major_list)

    else:
        my_list.extend(minor_list)
        my_list.extend(minor_list)

    my_list.extend(natural_list)
    my_list.extend(natural_list)
    my_list.extend(alter_list)

    while len(ans) != ans_num:
        ans = random.sample(my_list, ans_num)
        ans = list(set(ans))

    ans.sort()

    ans_str = []
    for a in ans:
        ans_str.append( oto_list[a] )

    print(ans_str)

    with open("log.txt", mode="a") as f:
        f.write(str(ans_str)+ "\n")


my_arg = sys.argv

if len(my_arg) == 1:
    main(is_major=True, ans_num=4)

if len(my_arg) == 2:
    if my_arg[1]:
        main(is_major=True, ans_num=4)
    else:
        main(is_major=False, ans_num=4)

if len(my_arg) >= 3:
    if my_arg[1]:
        main(is_major=True, ans_num=int(my_arg[2]))
    else:
        main(is_major=False, ans_num=int(my_arg[2]))
