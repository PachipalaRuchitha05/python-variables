#python variables#
print("****************")
print("hello world")
string_variables="Hello tuplis good morning"
print(string_variables)
print("Netherlands :" +" ",string_variables)
mixed_letter_variables="This Me veRy ConFused GurL"
print(mixed_letter_variables)
print(mixed_letter_variables.lower())
print(mixed_letter_variables.upper())
Slicing_of_variables="Effil Tower"[3]
print(Slicing_of_variables)
print(len(Slicing_of_variables))
print(len(mixed_letter_variables))
repalce_of_variables="ruchi"
print(repalce_of_variables)
first_serial_number="ABC123"
print("changed serial number :"+first_serial_number.replace('123' ,'234'))
first_name="ruchitha"
last_name="pachipala"
print(first_name+last_name)
print("change of firstname :"+first_name.replace('itha' ,'uluu'))
windows_serial_number="abc_def_ghi_jkl"
print(windows_serial_number)
windows_serial_number_1="abc"
windows_serial_number_2="def"
windows_serial_number_3="ghi"
windows_serial_number_4="jkl"
print(windows_serial_number_1)
print(windows_serial_number_2)
print(windows_serial_number_3)
print(windows_serial_number_4)
print("repalce of windows_serial_number_1 :"+windows_serial_number_1.replace('abc' ,'aaa'))
print("repalce of windows_serial_number_2 :"+windows_serial_number_2.replace('def' ,'bbb'))
print("repalce of windows_serial_number_3 :"+windows_serial_number_3.replace('ghi' ,'ccc'))
print("repalce of windows_serial_number_4 :"+windows_serial_number_4.replace('jkl' ,'ddd'))
print(windows_serial_number_1)
windows_serial_number_a="abc_def_ghi_jkl"[0:3]
print(windows_serial_number_a)
windows_serial_number_b="abc_def_ghi_jkl"[4:7]
print(windows_serial_number_b)
windows_serial_number_c="abc_def_ghi_jkl"[8:11]
print(windows_serial_number_c)
windows_serial_number_d="abc_def_ghi_jkl"[12:15]
print(windows_serial_number_d)
print("encoded_window_serial_number:"+windows_serial_number_a+"-",windows_serial_number_b+"-",windows_serial_number_c+"-",windows_serial_number_d)
summery_number_a=10
summery_number_b=20
summery_result = summery_number_a + summery_number_b
print("summery :"+str(summery_result))
numeric_variable=10
print("integer variable value :"+str(numeric_variable))
summery_variable_a=10
summery_varibale_b=5
summery_result = summery_variable_a + summery_varibale_b
print("summery :"+str(summery_result))
summery_variable_a=10
summery_varibale_b=5
summery_result = summery_variable_a * summery_varibale_b
print("summery :"+str(summery_result))
print("casting integer into string")
integer_variable=5
integer_variable_casted_to_string=str(integer_variable)
print(type(integer_variable_casted_to_string))
print("casting integer into float")
integer_variable=29
integer_variable_casted_to_float=float(integer_variable)
print(type(integer_variable_casted_to_float))
a=7
print(type(a))

################################################################################
my_age=30
sister_age=30
mothers_age=60
my_name="drimty"
phone_name="oneplust 5T"
my_best_friends_name="drimty"
print(my_age)
print(mothers_age)
print(sister_age)
print(my_name)
print(phone_name)
print(my_best_friends_name)
print(sister_age == my_age)
print(sister_age != my_age)
print(sister_age > my_age)
print(my_name != phone_name)
print(my_best_friends_name == my_name)

################################################################################

print("******************************************************")
print("my_list_collections")
cars_list=['bwn','toyota','tesla','kia']
print("list_of_cars :"+str(cars_list))
print("list_of_cars :"+str(cars_list[-2]))
print("list_of_cars :"+str(cars_list[1]) == "toyota")
mixed_values_list=['jim',3500,'alex',2.53,'true']
print("mixed_values_of_list :"+str(mixed_values_list))
print("mixed_values_of_list :"+str(mixed_values_list[0:4]))
print("mixed_values_of_list :"+str(mixed_values_list[2]))


cars_list=['bwn','toyota','tesla','kia']
cars_list.append('alpha romeo')
print("append alpha romeo to the end of the cars list :"+str(cars_list))

####################################################################################

print("***************************************************************")
employee_list=['adam','john','greg','danna','ashly']
print("list of the employess :"+str(employee_list))
print("length of the employees list is :"+str(len(employee_list)))
employee_list[1]="jack"
print("replace john and insert jack :"+str(employee_list))
employee_list.insert(3,'marvik')
print("insert marvik in the index of 3 :"+str(employee_list))
employee_list.remove('marvik')
print("print the list where marvik was removed :"+str(employee_list))
employee_list.append('marvik')
print("print the list where marvik was added :"+str(employee_list))
employee_list.pop(5)
print("print the list :"+str(employee_list))
my_list=[2,5,4,3,7]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
employee_list.sort()
print("print the sorted employee list :"+str(employee_list))
employee_list.sort(reverse=True)
print("print the sorted employee list :"+str(employee_list))