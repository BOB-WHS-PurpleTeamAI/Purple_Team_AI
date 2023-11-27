파이썬 데이터셋 https://www.kaggle.com/datasets/veeralakrishna/python-code-data/data 을 이용해서 
토크나이져를 학습하고 인코딩 디코딩 메소드 작성해서 작동하는지 테스트 
데이터셋 형태 
# write a python program to add two numbers 
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print(f'Sum: {sum}')


# write a python function to add two user provided numbers and return the sum
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


# write a program to find and print the largest among three numbers

num1 = 10
num2 = 12
num3 = 14
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print(f'largest:{largest}')
