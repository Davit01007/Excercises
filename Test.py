# 1. Զույգ թե՞ կենտ (even or odd) Ներմուծեք console-ից մի թիվ և այն պահեք փոփոխականում։ Գրեք ծրագիր,որը
# 1. Կորոշի այդ թիվը զույգ է, թե՞ կենտ։ (Հուշում։ օգտագործեք % օպերատորը և ճյուղավորող կառուցվածք )
# 2. Կորոշի այդ թիվը 3 ին բազմապատիկ է, թե՞ ոչ։
# 3. Կորոշի այդ թիվը բաժանվու՞մ է 2ի և 3ի միաժամանակ։


# def even_or_odd(number):
#     if number % 2 == 0 and number % 3 == 0:
#         return "Number divide 2 and 3"
#     elif number % 3 == 0:
#         return "Number is odd"
#     elif number % 2 == 0:
#         return "Number is even"
#     else:
#         return "The number you entered is incorrect:"
#
#
# num = even_or_odd(int(input("Input number:\t")))
# print(num)

# 2. Թվերից առավելագույնը Ստեղծեք 2 փոփոխական և այդ փոփոխականներին թվային արժեքներ տվեք։
# Գրեք ծրագիր, որը
# 1. Կհամեմատի այդ փոփոխականները և կարտածի դրանցից մեծը։
# 2. Ձևափոխեք ծրագիրը այնպես, որ փոփոխականները ներմուծի օգտատերը։


# def compare_numbers(num1, num2):
#     return f"Max number is {max(num1, num2)}"
#
#
# n = compare_numbers(5, 10)
# n2 = compare_numbers(int(input("Input number 1\t")), int(input("Input number 2\t")))
# print(n)
# print("Inputed number:\t", n2)

# 3. Տպել բոլոր այն երկնիշ թվերի գումարը, որոնք 4-ի բաժանելիս կմնա 1 մնացորդ։


# for i in range(10, 100):
#     if i % 4 == 1:
#         print(i)

# 4. Արտածիր համապատասխանաբար ցուրտ է (t <= 18 °C), հաճելի է (18 °C < t < 24 °C), շոգ է (t>= 24 °C)
# կախված սենյակի ջերմաստիճանից:
# t ջերմաստիճանը վերցնել օգտատիրոջից input-ի միջոցով։


# temp = int(input("Input temperature for room:\t"))
# if temp <= 18:
#     print("It's coldly:\t")
# elif 18 < temp < 24:
#     print("In's nice:\t")
# elif temp > 24:
#     print("It's hotly:\t")

# 5. Տպել 100-ից 600 միջակայքում գտնվող բոլոր այն թվերը, որոնք բաժանվում են 3-ի և 11-ի, սակայն չեն բաժանվում 7-ի։


# for num in range(100, 600):
#     if num % 3 == 0 and num % 11 == 0 and num % 7 != 0:
#         print("Numbers:\t", num)

# 6. Հաշվել և տպել user- ի կողմից մուտքագրված միջակայքի 7- ի բաժանվող թվերի քանակը:


# def num_div_by_seven(n, n2):
#     for i in range(n, n2):
#         if i % 7 == 0:
#             print(i)
#
#
# num_div_by_seven(int(input("Input start number:\t")), int(input("Input stop number:\t")))

# 7. Որոշել console-ից մուտքագրված String-ը Palindrome է, թե՞ ոչ։


# def palindrome(word):
#     if word == word[::-1]:
#         print("The word is palindrome")
#     else:
#         print("The word is not palindrome")
#
#
# palindrome(input("Input word and know is this palindrome or not:\t").lower())

# 8. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the
# given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less
# than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


# def word(inputed_word):
#     length = len(inputed_word)
#     if length <= 2:
#         pass
#     elif inputed_word[-3:] == "ing":
#         inputed_word += "ly"
#     else:
#         inputed_word += "ing"
#
#     return inputed_word
#
#
# print(word(input("Input the word\t")))

# 9. Write a Python script that takes input from the user and
# displays that input back in upper and lower cases.


# def up_and_low(word):
#     if word.isupper():
#         print("Inputed word is Upper case and i return Lower\t", word.lower())
#     else:
#         print("Inputed word is Lower case and i return Upper:\t", word.upper())
#
#
# up_and_low(input("Input the word\t"))

# 10. Write a Python program to get the largest number from a list.


# empty_list = []
# empty_list.append(int(input("Make a list and know largest number:\t")))
# empty_list.append(int(input("Input first number:\t")))
# empty_list.append(int(input("Input second number:\t")))
# empty_list.append(int(input("Input third number:\t")))
# print(f"List numbers {empty_list} and max number is {max(empty_list)}")

# 11. You have given a Python list. Write a program to find value 20 in the list, and if it is
# present, replace it with 200. Only update the first occurrence of an item.

# def finding_num_20(*args):
#     empty_list = list(args)
#     for num in range(len(empty_list)):
#         if empty_list[num] == 20:
#             empty_list[num] = 200
#             break
#     print(empty_list)
#
#
# finding_num_20(int(input("Make a list:\t")), int(input("Input first number:\t")), int(input("Input second number:\t")), int(input("Input third number:\t")))

# 12. Given a list of numbers. write a program to turn every item of a list into its square.


# def square_of_numbers(a, b, c, d):
#     list1 = [a, b, c, d]
#     for i in range(len(list1)):
#         list1[i] *= list1[i]
#     print(list1)
#
#
# square_of_numbers(int(input("Input first number:\t")), int(input("Input second number:\t")), int(input("Input third number:\t")), int(input("Input fourth number:\t")))

# 13. Ստեղծել int թվերի ցուցակ: Հաշվել ցուցակի բոլոր տարրերի արտադրյալը:


# def sum_of_numbers(a, b, c, d):
#     numbers = [a, b, c, d]
#     return "Summary of numbers", sum(numbers)
#
#
# num = sum_of_numbers(int(input("Input first number:\t")), int(input("Input second number:\t")), int(input("Input third number:\t")), int(input("Input fourth number:\t")))
# print(num)

# 14. Ստեղծել  թվերի ցուցակ: Ցուցակից ջնջել բոլոր բացասական տարրերը: Տպել ցուցակը:


# def del_negative_numbers(a, b, c, d, e):
#     numbers = [a, b, c, d, e]
#     numbers.sort()
#     print("Numbers is sorted:\t", numbers)
#     for num in numbers:
#         if num > 0:
#             print(f"Printed only positive numbers {num}:")
#
#
# del_negative_numbers(int(input("Input first number:\t")), int(input("Input second number:\t")), int(input("Input third number:\t")), int(input("Input fourth number:\t")), int(input("Input the fifth number:\t")))

# 15. Ստեղծել թվերի ցուցակ: Ցուցակից ջնջել բոլոր կենտ տարրերը: Տպել ցուցակը:


# def deleting_odd_numbers(*args):
#     list_of_numbers = [*args]
#     print(f"Printed list of numbers {list_of_numbers}")
#     for num in list_of_numbers:
#         if num % 2 == 0:
#             print(f"Printed only positive numbers {num}:")
#
#
# deleting_odd_numbers(int(input("Input first number:\t")), int(input("Input second number:\t")), int(input("Input third number:\t")), int(input("Input fourth number:\t")), int(input("Input the fifth number:\t")))

# 16. # Գրեք ծրագիր օգտագործելով random մոդուլը, որը կստեղծի (0,20) տիրույթում գտնվող արժեքներ պարունակող A[] և B[] ցուցակները:
# Ծրագիրը օգտատիրոջից ցիկլով 10 անգամ պետք է վերցնի int տիպի արժեքներ և ավելացնի դրանք A-ցուցակի մեջ: Նույնը կատարել B-ցուցակի համար (ցուցակները չպարունակեն ամբողջությամբ նույն արժեքները):
# Convert արեք  A[] և B[] ցուցակները, որպեսզի դրանք դառնան set-եր:
# 1.1 Տպեք A{} և B{} բազմությունները էկրանին:
# 1.2 Ստուգեք A{} == B{} պայմանը:
# 1.3 Ստուգեք A{} (union) B{} պայմանը:
# 1.4 Ստուգեք A{} (intersection) B{} պայմանը:
# 1.5 Ստուգեք A{} (difference) B{} պայմանը և հակառակը:


# import random                                              # Part 1
#
#
# def random_numbers(length):
#     a = []
#     b = []
#     for i in range(length):
#         a.append(random.randint(0, 20))
#         b.append(random.randint(0, 20))
#     set1 = set(a)
#     set2 = set(b)
#     print(set1)                                            # Part 1.1
#     print(set2)
#     to_check = set1 == set2                                # Part 1.2
#     print(f"Result of checking {to_check}:")
#     check_union = set1.union(set2)                         # Part 1.3
#     print(f"Checking 'a' union 'b' {check_union}:")
#     check_intersection = set1.intersection(set2)           # Part 1.4
#     print(f"Checking 'a' intersection 'b' {check_intersection}:")
#     check_difference = set1.difference(set2)               # Part 1.5
#     check_difference_2 = set2.difference(set1)
#     print(f"Checking 'a' difference 'b' {check_difference}:")
#     print(f"Checking 'b' difference 'a' {check_difference_2}:")
#
#
# random_numbers(int(input("Input number for list length:\t")))

# 17. Գրել ծրագիր-բառարան, որը թարգմանում է անգլերեն տերմինները և ցուցադրում
# դրանց հայերեն տարբերակները: Օգտատերը input-ով ներմուծում է բառը
# 1․ եթե բառը նկարագրված է ծրագրում, ապա տպում է թարգմանությունը։
# 2․ եթե բառը գոյություն չունի, տպում է “Տվյալ բառը բացակայում է բառարանում” արտահայտությունը։


# def dictionary(word):
#     dict1 = {"variable": "Փոփոխական",
#               "declaration": "Հայտարարում",
#               "assignment": "Վերագրում",
#               "data types": "Տվյալների տիպեր",
#               "integer": "Թվային տիպ",
#               "string": "Տողային տիպ",
#               "boolean": "Բուլյան տիպ",
#               "true": "Ճշմարիտ",
#               "else": "Հակառակ դեպքում",
#               "array": "Զանգված",
#               "if": "Եթե",
#               "false": "Կեղծ"}
#     if word in dict1.keys():
#         print(dict1[word])
#     else:
#         print("Inputed word is not exist")
#
#
# dictionary(input("Transleator:\t").lower())

# 18. Write a programm to print the following number pattern using loop.
#                                   1
#                                   1 2
#                                   1 2 3
#                                   1 2 3 4
#                                   1 2 3 4 5


# def number(num):
#     for i in range(1, num + 1):
#         for j in range(1, i):
#             print(j, end=" ")
#         print(" ")
#
#
# number(int(input("Input the length of numbers:\t")))

# 19. Write a programm to display only thoes numbers from a list that satisfy the following condition.
# 1. The number must be divide by five.
# 2. If the number greather than 150, then skip it and move to the next number.
# 3. If the number greather than 500, then stop the loop.


# def five_divide(*args):                # Part 1
#     list1 = list(args)
#     for i in list1:
#         if i % 5 == 0:                 # Part 2, part 3
#             if i >= 500:
#                 break
#         print(i)
#
#
# five_divide(int(input("Input first number:\t")), int(input("Input second number:\t")), int(input("Input third number:\t")), int(input("Input fourth number:\t")), int(input("Input the fifth number:\t")))

# 20. Write a programm to display all prime numbers within range

# def prime_numbers(start, stop):
#     for num in range(start, stop):
#         if num % 2 == 1:
#             print(num, end=", ")
#
#
# prime_numbers(int(input("Input 'Start' number for loop range:\t")), int(input("Input 'Stop' number for loop range:\t")))

# 21. Print the following pattern
# *            First pattern
# * *
# * * *
# * * * *
# * * * * *    Second pattern
# * * * *
# * * *
# * *
# *


# def stars(length):
#     for i in range(1, length):
#         for j in range(1, i):
#             print("*", end=" ")
#         print(" ")
#     for a in range - 6, 1):
#         for b in range(1, - a):
#             print("*", end=" ")
#         print(" ")
#
#
# stars(6)

# 22. Write a Python programm to find the length of a given dictionary values.


# dict1 = {1: "Black", 2: "Red", 3: "Yellow", 4: "White"}
# dict2 = {}
# for i in dict1.values():
#     dict2[i] = len(i)
# print(dict2)

# 23. Write a Python function to check whether a number is perfect or not.
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the
# sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a
# perfect number is a number that is half the sum of all of its positive divisors (including itself).


# def perfect_number(num):
#     sum = 0
#     for x in range(1, num):
#         if num % x == 0:
#             sum += x
#     return sum == num
#
#
# print(perfect_number(int(input("Input number and check is this perfect:\t"))))

# 24.1.1 Գրել ֆունկցիա, որը կհաշվի և կվերադարձնի ուղղանկյան պարագիծը(perimeter of rectangle):
#    1.2 Գրել ֆունկցիա, որը հաշվում և վերադարձնում է քառակուսու պարագիծը(perimeter of square):
#    1.3 Գրել ֆունկցիա, որը կհաշվի և կվերադարձնի ուղղանկյան մակերեսը(area of rectangle):
#    1.4 Գրել ֆունկցիա, որը հաշվում և վերադարձնում է քառակուսու մակերեսը(area of square):


# class MathExcersises:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def perimetr_of_rectangle(self):
#         return f"Perimetr of rectangle: ({self._length} + {self._width}) * 2 = {(self._length + self._width) * 2}"
#
#     def perimetr_of_square(self):
#         return f"Perimetr of quare: {self._length} * 4 = {self._length * 4}"
#
#     def area_of_rectangle(self):
#         return f"Area of rectangle: {self._length} * {self._width} = {self._length * self._width}"
#
#     def area_of_square(self):
#         return f"Area of square: {self._length} * {self._length} = {self._length * self._length}"
#
#
# maths = MathExcersises(int(input("Input first number:\t")), int(input("Input second number:\t")))
# print(maths.perimetr_of_rectangle())
# print(maths.perimetr_of_square())
# print(maths.area_of_rectangle())
# print(maths.area_of_square())

# 25. Write a Python function that accepts a string and calculate the number of upper case
# letters and lower case letters.Sample String:


# def upper_letters(word):
#     upper = 0
#     lower = 0
#     for i in word:
#         if i.isupper():
#             upper += 1
#         else:
#             lower += 1
#     print(f"Upper case's\t {upper}", f"\nlower case's\t {lower}", f"\nLength of sentence\t {len(word)}")
#
#
# upper_letters(input("Input the word and count how many upper case letters in:\t"))


# 26. Write a Python function that takes a list and returns a new list with unique elements of the first list:


# def unique_list():
#     list1 = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
#     return set(list1)
#
#
# print(list(unique_list()))

# 27. Write a Python function to check whether a number is in a given range:


# def number(num):
#     if num in range(100):
#         return "The number is in range"
#     else:
#         return "The number out of range"
#
#
# print(number(int(input("Input number:\t"))))

# 28. Write a python program to create a lambda function that adds 15 to
# a given number passed in as an argument, also crate a lambda function
# that muliplies argument x with argument y and print the result


# def lambda_func(num):
#     return lambda a: a * num
#
#
# x = lambda_func(int(input("Input first number and Multiplies with lambda function:\t")))
# print(x(int(input("Input second number:\t"))))

# 29 Write a Python program to calculate the sum of a list of numbers using recursion.


# def count_sum_of_list(num):
#     if len(num) == 0:
#         return 0
#     else:
#         return num[0] + count_sum_of_list(num[1:])
#
#
# x = [2, 4, 6, 8]
# print("Sum of list", count_sum_of_list(x))


# ------------------------------------------------------Bubble sort Algorithm-------------------------------------------------------


# def bubble_sort_algorithm(list1):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(list1) - 1):
#             if list1[i] > list1[i + 1]:
#                 list1[i], list1[i + 1] = list1[i + 1], list1[i]
#                 swapped = True
#     print("Bubble sort Algorithm:\t", list1)
#
#
# a = [5, 6, 8, 1, 2, 10, 3, 7, 4, 9]
# print(bubble_sort_algorithm(a))

# ------------------------------------------------------Selection sort Algorithm----------------------------------------------------
# Using for small data types. Aveli qich ram e ogtagorcum


# def selection_sort_algorithm(list1):
#     marker = 0
#     while marker < len(list1):
#         for i in range(marker, len(list1)):
#             if list1[marker] > list1[i]:
#                 list1[marker], list1[i] = list1[i], list1[marker]
#         marker += 1
#     print("Selection sort algorithm:\t", list1)
#
#
# b = [5, 8, 1, 6, 2, 3, 10, 7, 4, 9]
# selection_sort_algorithm(b)

# 30. Write a Python program to get the factorial of a non-negative integer using recursion.


# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# x = factorial(int(input("Input the number and count factorial:\t")))
# print(x)

# 31. Write a Python program to calculate the harmonic sum of n-1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers..


# def harmonic_numbers(num):
#     if num == 0:
#         return "Coul'd not divide by 0:"
#     elif num == 1:
#         return num
#     else:
#         return 1/num + harmonic_numbers(num-1)
#
#
# print(harmonic_numbers(int(input("Input number and count fibonacci:\t"))))

# -------------------------------------Calculator---------------------------------------


# class Calculator:
#
#     def display_menu(self):
#
#         if self.operation == "+":
#             return self.add_numbers()
#         elif self.operation == "-":
#             return self.subtract_numbers()
#         elif self.operation == "*":
#             return self.count_numbers()
#         elif self.operation == "/":
#             return self.div_numbers()
#         else:
#             return "You entered wrong operation. Please try again:"
#
#     def __init__(self, operation, num, num2):
#         self.operation = operation
#         self.num = num
#         self.num2 = num2
#
#     def add_numbers(self):
#         return f"{self.num} + {self.num2} = {self.num + self.num2}"
#
#     def subtract_numbers(self):
#         return f"{self.num} - {self.num2} = {self.num - self.num2}"
#
#     def count_numbers(self):
#         return f"{self.num} * {self.num2} = {self.num * self.num2}"
#
#     def div_numbers(self):
#         return f"{self.num} // {self.num2} = {self.num / self.num2}"
#
#
# calc = Calculator(input("Input operation (+ - * /):\t"), int(input("Input first number:\t")), int(input("Input second number:\t")))
# print(calc.display_menu())

# 32. Write a Python function to read the content from a text file "poem.txt" line by line and display the
# same on screen.


# def read_file():
#     with open('poem.txt', 'r', encoding='utf-8') as file:
#         x = file.read()
#         z = x.split(" ")
#         for i in z:
#             print(i)
#
#
# read_file()

# 33. Write a Python function to count and display the total number of words in a text file.


# def count_length_of_words():
#     with open('poem.txt', 'r', encoding='utf-8') as file:
#         word = file.read()
#         text = word.split(" ")
#         count = 0
#         for i in text:
#             print(i)
#             if len(i) >= 2:
#                 count += 1
#         print("Count of words is", count)
#
#
# count_length_of_words()

# 34. Write a Python program to add text to a file and display the text in python.txt file.


# def write_and_display():
#     with open('python.txt', 'a', encoding='utf-8') as append_file:
#         append_file.write(input("Write a word:\t"))
#         print("Inputed word appended in 'python.txt' file:")
#
#
# write_and_display()

# 35. Write a Python function display_words() to read lines from a text file "story.txt",
# and display those words, which are less than 4 characters.


# def display_words():
#     with open('story.txt', 'r', encoding='utf-8') as file:
#         line = file.read()
#         word = line.split(" ")
#         count = 0
#         for i in word:
#             if len(i) <= 4:
#                 count += 1
#                 print(i, end=" ")
#         print("\nSum of words than less 4 characters\t", count)
#
#
# display_words()


# 36. Write a python program to read a file, a.txt line by line and write it to another b.txt file.

#
# with open('a.txt', 'r', encoding='utf-8') as a:
#     text = a.read()
#     sort_line = text.split(" ")
#     for i in sort_line:
#         with open('b.txt', 'a', encoding='utf-8') as b:
#             b.write(i)
#             b.write("\n")

# 37 . In a given text you need to sum the numbers while excluding any digits that form part of a word.


# def sum_numbers(text):
#     return sum(int(text) for text in text.split() if text.isdigit())
#
#
# print(sum_numbers("Hello world 15 25"))


# 38. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# class Cars:
#     #Writing a private constructor
#     def __init__(self, max_speed, milage):
#         self.__max_speed = max_speed
#         self.__milage = milage
# #Making available private members for using
#     def get_private_members(self):
#         return self.__max_speed, self.__milage
# #Setting members and returns a result
#     def set_members(self):
#         return f"The max speed of {self.__max_speed}, and the milage of {self.__milage}:"
#
#
# cars_atributes = Cars(input("Input the max speed of your car\t"), input("Input the max range milage of your car\t"))
# print(cars_atributes.set_members())


# 39. Write a Python class named Student with two attributes student_name, marks. Modify the attribute
# values of the said class and print the original and modified values of the said attributes


# class Students:
#
#     def __init__(self, student_name, marks):
#         self.student_name = student_name
#         self.marks = marks
#
#     def show_input_parameters(self):
#         return f"The student name is {self.student_name}, {self.marks}:"
#
#     def default_student(self):
#         student_name = "Mark"
#         marks = "good student"
#         print("Default parameters")
#         return f"The student name is {student_name}, {marks}:"
#
#
# students = Students(input("Input student name\t"), input("Write your opinion about the student\t"))
# print(students.show_input_parameters())
# print(students.default_student())


# 40. From (py.checkio.org) You should return a given string in reverse order.

# def backward_string(val):
#     x = val[::-1]
#     return x
#
#
# print(backward_string("val"))


# 41. From (py.checkio.org) try to find out how many zeros a given number has at the end.

# def end_zeros(num):
#     x = str(num)
#     z = x[::-1]
#     count = 0
#     for i in z:
#         if i != "0":
#             break
#         count += 1
#     return count
#
#
# print(end_zeros(1000))


# 42. From (py.checkio.org) You are given a list of integers. Your task in this mission is to duplicate
# (..., 🍩, ... --> ..., 🍩, 🍩, ...) all zeros (think about donuts ;-P) and return the result as any Iterable.
# Let's look on the example:

# def duplicate_zeros(zero):
#     z = 0
#     l = []
#     for i in zero:
#         l.append(i)
#         if i == 0:
#             z += 0
#             l.append(i)
#     return l
#
#
# print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))


# 43. From (py.checkio.org) You have to split a given list into two lists inside an Iterable.
# If input sequence has an odd amount of elements, then the first list inside result Iterable should have more elements.
# If input sequence has no elements, then two empty lists inside result Iterable should be returned.

# def split_list(list1):
#     i = (len(list1) + 1) // 2
#     return [list1[:i], list1[i:]]
#
#
# print(split_list([1, 2, 3, 4, 5]))


# 44 From (py.checkio.org) in this mission you should check if all elements in the given list are equal.

# def all_the_same(list1):
#     if list1.count(list1[0]) == len(list1):
#         return True
#
#     return False
#
#
# print(all_the_same([1, 1, 1]))


# 45. From (py.checkio.or) Check if a given string has all symbols in upper case. If the string is empty or doesn't
# have any letter in it - function should return True.

# def is_all_upper(text):
#     if text.upper() == text:
#         return True
#     elif len(text) == 0:
#         return True
#     else:
#         return False
#
#
# print(is_all_upper("15"))


# 46. From (py.checkio.org) You are given a non-empty list of integers (X).
# For this task, you should return a list consisting of only the non-unique elements in this list.
# To do so you will need to remove all unique elements (elements which are contained in a given list only once).
# When solving this task, do not change the order of the list. Example:
# [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

# def checkio(data):
#     list1 = []
#     for i in data:
#         if data.count(i) > 1:
#             list1.append(i)
#     return list1
#
#
# print(checkio([1, 2, 3, 1, 2, 4, 5]))


# Fibonnaci numbers
# class Fibonacci:
#     def __init__(self, max_num):
#         self.max_num = max_num
#         self.a = 0
#         self.b = 1
#
#     def generate(self):
#         fib_list = []
#         while self.b < self.max_num:
#             fib_list.append(self.b)
#             self.a, self.b = self.b, self.a + self.b
#         return fib_list
#
#
# fib = Fibonacci(200)
# print(fib.generate())


# 47 From (py.checkio.org) You are given a string with words and numbers separated by whitespaces (one space).
# The words contains only letters. You should check if the string contains three words in succession. For example,
# the string "start 5 one two three 7 end" contains three words in succession

# def checkio(words):
#     count = 0
#     for i in words.split():
#         if i.isalpha():
#             if count == 3:
#                 return True
#         else:
#             count = 0
#
#     return False
#
#
# print(checkio("He is 123 man"))


# 48 In this mission you should check if all elements in the given list are equal.

# def all_the_same(list1):
#     try:
#         if list1.count(list1[0]) == len(list1):
#             return True
#
#         return False
#
#     except Exception:
#         print("Input number is False")
#
#
# print(all_the_same([1, 1, 1]))


# 49 You need to count the number of digits in a given string.

# def count_digits(text):
#     count = 0
#     for i in text:
#         if i.isdigit():
#             count += 1
#
#     return count
#
#
# print(count_digits("hi"))
# print(count_digits("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"))


# 50 In a given list the first element should become the last one.
# An empty list or list with only one element should stay the same.

# def replace_first(num):
#     x = num[0]                        #Assign the value of index 0 to the variable
#     if len(num) >= 2:
#         num.remove(num[0])            #Deleting the 0 index of list
#         num.extend([x])               #Adding the number at the end
#         return num
#     elif len(num) == 1:
#         return num
#
#
# print(replace_first([1, 2, 3, 4]))
# print(replace_first([1]))
# print(replace_first([3, 5, 8, 11]))


# 51 You have a string that consist only of digits.
# You need to find how many zero digits ("0") are at the beginning of the given string.

# def beginning_zeros(zero):
#     count = 0
#     for i in zero:
#         if i != "0":
#             break
#         count += 1
#     return count
#
#
# print(beginning_zeros("10"))
# print(beginning_zeros("001"))


# 53 For the illustration we have a list [1, 2, 3, 4, 5] and we need to remove
# all elements that go before 3 - which is 1 and 2.
# We have two edge cases here: (1) if a cutting element cannot be found,
# then the list shoudn't be changed. (2) if the list is empty, then it should remain empty.

# def remove_all_before(lst, target):
#     try:
#         index = lst.index(target)
#         return lst[index:]
#     except ValueError:
#         return lst
#
#
# lst1 = [1, 2, 3, 4, 5]
# lst2 = []
#
#
# print(remove_all_before([1, 2, 3, 4, 5], 3))

# class Drivers:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get(self):
#         return self.__name, self.__age
#
#     def show(self, name, age):
#         self.__name = name
#         self.__age = age
#         return f"Name {name}\nAge {age}"
#
#
# a = Drivers(input("Write your name:\t"), input("Write your age:\t"))
# print(a.show())