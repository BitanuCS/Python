def mutate_string(string, position, character):

    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    print(mutate_string(s, int(i), c))
