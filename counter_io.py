import os

emoji_digits = [
    "0️⃣",
    "1️⃣",
    "2️⃣",
    "3️⃣",
    "4️⃣",
    "5️⃣",
    "6️⃣",
    "7️⃣",
    "8️⃣",
    "9️⃣"
]

def get_digits_as_emojis(number):
    digits = []
    digits_as_emojis = []
    if number != 0:
        while number > 0:
            digits.append(number % 10)
            number = number // 10
    else:
        digits.append(0)
    for digit in digits:
        digits_as_emojis.append(digit)
    # reverse the list
    digits_as_emojis.reverse()
    # return list as string
    return ' '.join(emoji_digits[i] for i in digits_as_emojis)

# if file lifetime_counter.txt doesn't exist, create it
def check_file():
    if not os.path.exists('/data/lifetime_counter.txt'):
        with open('/data/lifetime_counter.txt', 'w') as f:
            f.write(str(0))

# get the number from a file
def get_lifetime_counter():
    check_file()
    with open('/data/lifetime_counter.txt', 'r') as f:
        number = int(f.read())
    return number

# update the number in a file
def set_lifetime_counter(number):
    with open('/data/lifetime_counter.txt', 'w') as f:
        f.write(str(number))
