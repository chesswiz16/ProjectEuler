__author__ = 'Tiger'

to_text = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

count = 0
for n in range(1, 1001):
    as_text = ""
    hundreds = int(n/100)
    n %= 100
    tens = int(n/10)
    n %= 10
    ones = n
    tens *= 10
    remainder = tens + ones
    if 0 < hundreds < 10:
        as_text += to_text[hundreds] + " hundred"
        if remainder > 0:
            as_text += " and "
    elif hundreds == 10:
        as_text = "one thousand"

    if remainder <= 20:
        as_text += to_text[remainder]
    else:
        as_text += to_text[tens] + " " + to_text[ones]

    print(as_text)
    count += len(as_text.strip().replace(" ", ""))

print(count)