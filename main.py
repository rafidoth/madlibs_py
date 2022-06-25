# variables will be filled from users
name = input("name : ")
institute = input("institute : ")
dept_name = input("department : ")
permanent_address = input("Permanent address : ")
present_address = input("Present Address : ")
hobby = input("Hobby : ")



# main paragraph
madlib = f"My name is {name}, a student of {institute}. Currently I'm studying in the department of {dept_name}. My permanent address is {permanent_address} and my present addess is {present_address}. I'm interested in {hobby}."

print(madlib)