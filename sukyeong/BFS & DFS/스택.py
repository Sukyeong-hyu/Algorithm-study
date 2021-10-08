# 스택은 선입후출의 구조
# 오른쪽으로 삽입하고 오른쪽으로 꺼내기 위해 리스트의 append와 pop을 사용하여 표현할 수 있음

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 최하단 원소부터 출력
print(stack)  # 최상단 원소부터 출력
