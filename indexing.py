credit_card = "1234-5678-9012-3456"

print("First 4 digits:", credit_card[:4])
print(credit_card[5:9])
print("remainder:", credit_card[10 :])

#using step - it is used to skip characters
print("Every second digit:", credit_card[::2])

#last 4 digits
print(f"xxxx-xxxx-xxxx-{credit_card[-4:]}")

#reversing a string we set the step to -1
print("Reversed credit card number:", credit_card[::-1])