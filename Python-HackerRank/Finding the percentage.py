if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        avg = 0
        for i in range(len(student_marks[query_name])):
            avg += student_marks[query_name][i]
    
        avg /= i+1
        print("%.2f" %avg)
    else:
        print("not exists")