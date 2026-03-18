# # from school.manager import manager_info, manager_salary as m_salary
# # from school.employee import employee_info, employee_salary as e_salary
# # from school.student import student_info, student_grade as s_grade  

# # # def manager_salary():
# # #     return 5000

# # int=manager_info()
# # print(int)

# # man_salary=m_salary()
# # print(man_salary)


# if 1==1:
#     try:
#         print(500/1)
#     except:
#         print('division by zero error')
#     else :
#         print('no error')
#     finally:
#         print('done')
# else :
#     print('not found')
    
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

print("The end")