def verify_card_number(card_number):
    sum_of_odd_numbers = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        digit = int(digit)
        sum_of_odd_numbers += digit

    sum_of_even_numbers = 0
    even_numbers = card_number_reversed[1::2]

    for digit in even_numbers:
        digit = int(digit)
        number = digit * 2 
        if number >= 10:
            number = (number // 10) + (number % 10)
        
        sum_of_even_numbers += number

    total = sum_of_even_numbers + sum_of_odd_numbers
    print(total)
    return total % 10 == 0


    
def main():
    card_number = "837-133-64"
    card_translation = str.maketrans({"-": " "})
    card_translated = card_number.translate(card_translation)

    if not card_translated.isdigit():
        print("Invalid Card!")
        return

    if verify_card_number(card_translated):
        print("Valid!")
    else:
        print("Invalid!")
    

main()