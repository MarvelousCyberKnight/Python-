# a python program to calculate the average marks if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if 2 <= n <= 10:
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        if len(student_marks[query_name]) == 3:
            re = student_marks[query_name]
            tot = 0
            for i in re:
                if 0 <= i <=100: 
                    tot += i
            avg = tot/len(re)
            print("%.2f"%avg)
  #code written by siddarda gowtham
