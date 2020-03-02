
# CHecking palindrome

given = input()

rev = given[::-1]

print(rev)


if given == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

