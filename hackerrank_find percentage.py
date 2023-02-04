if __name__ == '__main__':
    n = int(input().strip())
    student_marks = {} #using dictionary
    for _ in range(n):
        name, *line = input().strip().split()
        # spliting  the line into separate scores and converting the each score into a float
        scores = list(map(float, line)) 
        student_marks[name] = scores
    query_name = input().strip()
    marks = student_marks[query_name]
    
    # to print the average of the marks rounded to 2 decimal places
    print("{:.2f}".format(sum(marks) / len(marks)))
