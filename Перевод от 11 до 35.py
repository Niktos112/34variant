def decimal_translator(number, base):
    letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in str(number):
        if i.isalpha():
            i = letters.find(i)
        if int(i) >= base:
            return None
    nums = []
    for i in str(number):
        nums.append(int(i))
    nums.reverse()
    answer = 0
    for i in range(len(nums)):
        answer += base ** i * nums[i]
    return answer
