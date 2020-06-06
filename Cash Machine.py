## Cash Machine ##
# Objective: the cash machine will give you the value desired in dollar banknotes
# Input: value you want to withdraw from the cash machine
# Output: banknotes from the cash machine

# 1) Input

# 1.1) Definition of the currency and banknotes
bank_notes = [100, 50, 20, 10, 5, 2, 1]

# 1.2)  Definition of the value to be drawn from the cash machine
value = input('Type the value you would like to withdraw: $ ').strip()

# 1.3) Checking if value is an integer
while True:
    try:
        value = int(value)
    except:
        value = input('Error found, please type valid value: $ ').strip()
        continue
    else:
        value = int(value)
        break

# 2) Output

# 2.1) Determination of the number of banknotes
while True:
    for note in bank_notes:
        if value >= note:
            if value % note == 0:
                print(f'{int(value / note)} banknotes of $ {note}')

            elif value % note != 0:
                print(f'{value // note} banknotes of $ {note}')

            value = value - int(value / note) * note

        if value - note == 0:
            break
    break