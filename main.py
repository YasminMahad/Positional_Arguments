def student_details(*args,**kwargs):
        students= 1
        for x in args:
            students*= x
            print(students)
        print(f"Hello {kwargs}")



