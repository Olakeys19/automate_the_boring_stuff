def collatz(number):
    if number % 2 == 0:
        answer = number // 2
        print(answer)
        return answer
    else:
        answer = 3 * number + 1
        print(answer)
        return answer

print("Enter 'q' to quit")
while True:
    try:
        num = input("Enter an integer: ")
        if (num == 'q'):
            break
        answer = collatz(int(num))
        while answer != 1:
            answer = collatz(answer)
    except ValueError:
        print('Please enter a valid integer!')
    



    



