def main():

  # ask user

  curr_value = int(input("Enter a number:  "))

  # keep doubling the number and print result
  while curr_value < 100:
    curr_value *= 2 # this will double the value
    print(curr_value, end= " ") # result

if __name__ == '__main__':
  main()
