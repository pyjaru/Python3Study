print("몇 살이죠?", end=' ')
나이 = input()
print("키는 몇이죠?", end = ' ')
키 = input()
print("몸무게는 얼마죠?", end=' ')
몸무게 = input()

formatter = "네, 나이는 {}살, 키는 {}, 몸무게는 {}이네요."
print(formatter.format(나이, 키, 몸무게))