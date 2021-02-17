def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        line = string[i:i+k]
        seen = ''
        for j in line:
            if j not in seen:
                seen += j
                print(j, end='')
        print()
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)