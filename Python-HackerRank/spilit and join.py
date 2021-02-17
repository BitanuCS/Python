def split_and_join(line):
    # write your code here
    line = line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    s = input()
    res = split_and_join(s)
    print(res)