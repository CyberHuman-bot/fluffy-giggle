lower = int(input("enter your lower limit"))
upper = int(input("enter your upper limit"))
for num in range(lower, upper+1):
        if 1<num:
            for denominator in range(2,num):
                  if num % denominator == 0:
                        break
            else :
                  print(num)