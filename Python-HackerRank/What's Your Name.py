def print_full_name(a, b):
    print("Hello {} {}! You just delved into python." .format(a, b))

if __name__ == '__main__':
    a = input().capitalize()
    b = input().capitalize()
    print_full_name(a, b)