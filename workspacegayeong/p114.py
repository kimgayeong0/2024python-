# nums=list(range(1,10,2))
# print(nums)
# print(type(nums))
# for i in range(2,11,2):
#     print(i)

# nums=(3,5,2,8,9)
# print(type(nums))
# for i in nums:
#     print(i)

# range는 시작 숫자와 마침 숫자가 있는데 시작 숫자 포함 마지막 숫자 전 까지 표현한다.
# 예 : range(1,6) =>1,2,3,4,5생성 ->list로 원소를 나타낼 수 있다.

def p(space,space_num,*args):
    str=""
    for i in args:
        str=str+(space*space_num)+i
    print(str)
p(",",3,"😊","😂")
p(",",3,"😊","😂","🤣","😘")