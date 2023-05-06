student_new = [{'name':'Jack', 'age':29},{'name':'Rose', 'age':33},{'name':'Tom', 'age':11}]
print(student_new)
for i in student_new:
    print(i)
    for j in i:
        print(i.get(j), end=' ')
        

print('=============================')

student_new.sort(key=lambda x : int(x['age']), reverse=True)
print(student_new)

