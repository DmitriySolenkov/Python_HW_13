# ???????? ???, ??????? ??????????? ????? ? ???????? ???????? ?? ??? ??????? ??? ?????????.
# ??????????? ??????? ??? ????????: �????? ???????? ???????, ???? ??????? ?????? ?????? ?? ??????? ? ?? ????�.
# ???????? ??????????? ?? ???? ????????????? ????? ? ????? ?????? 100 ?????.

from Exceptions import NotNumberException, NotInBordersException


res = input("Enter your number (1 - 100.000): ")
try:
    num = int(res)
    if (num <= 0 or num >= 100000):
        raise NotInBordersException(num, 0, 100000)
except ValueError:
    raise NotNumberException(res)
if num == 1:
    print("This number is neither prime nor complex")
elif num == 2:
    print("This number is prime")
else:
    check = False
    for i in range(2, num):
        if num % i == 0:
            print("This number is complex")
            check = True
            break
if check == False:
    print("This number is prime")
