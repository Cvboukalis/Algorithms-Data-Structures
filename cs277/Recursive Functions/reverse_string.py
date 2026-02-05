def reverse(s):
  
    if len(s) <2:
        return s
    return s[-1] + reverse(s[1:-1]) + s[0]

# test cases
print(reverse("x")) # should print x
print(reverse("whale")) # should print elahw
print(reverse("icemountain")) # should print niatnuomeci