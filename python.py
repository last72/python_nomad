# choice = input('Enjoying the course? (y or n)')

# while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
#   choice = input("Sorry, I didn't catch that. Enter again: ")

text = input("Put string: ")

def reverse(text):
  lst = list(text)
  tmp = []
  for i in lst:
    tmp = lst[len(lst)-1-i]
    lst.append(tmp)
    del(lst[len(lst)-1-i])
  print (lst)
  print (tmp)
  return "".join(lst)

reverse(text)