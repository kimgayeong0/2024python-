def sum(*numbers):
    sume_value=0
    for number in numbers:
        sume_value=sume_value+number
    return sume_value

result=sum(1,3)
print("1+3=", result)
print("1+3+5+7=", sum(1,3,5,7))

# sum함수를 가변 인자를 받도록 하여 다양한 수를 입력받게 한다.
# numbers로 전달 받은 값들으 합을 저장한다.
# result변수에 저장한 후 출력한다.
# 다른 한수의 매개 변수로 함수 호출을 넘길 수도 있다.