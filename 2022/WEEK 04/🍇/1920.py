def two(num):
  change = ''
  if(num > 2):
    num = int(num/2)
    # print(num)
    change = change + str(num)
    # print(change)
    two(num)
  elif(num == 2):
    change = change + 1
  else:
    change = change + str(num)
    # print(change)
    return change


num = int(input())
chage_num = two(num)    # None 에러

print(int(chage_num))