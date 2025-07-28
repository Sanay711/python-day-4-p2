Amt = int(input("Please Enter the Amount for the Withdrawal : "))

note_1 = Amt//100
note_2 = (Amt%100)//50
note_3 = ((Amt%100)%50)//10



print("Notes of 100 rupees", note_1)
print("Notes of 50 rupees", note_2)
print("Notes of 10 rupees", note_3)