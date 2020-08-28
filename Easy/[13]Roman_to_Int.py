s = 'IV'

roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
         'CD': 400, 'CM': 900}

i = 0
num = 0

for i in range(len(s)):
    if i + 1 <= len(s) and s[i:i + 2] in roman:
        num += roman[s[i:i + 2]]
        i += 2
    # else:
    #     num += roman[s[i]]
    #     i += 1

print(num)


# Difference between for & while
for j in range(5):
    print(j)
    j += 2

k = 0
while k < 5:
    print(k)
    k += 2