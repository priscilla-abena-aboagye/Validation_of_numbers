def verify_card_number(card_number):
    sum_of_odd_numbers = 0
    card_number_reversed = card_number[-1:-5:-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        digit = int(digit)
        sum_of_odd_numbers += digit

    sum_of_even_numbers = 0
    even_numbers = card_number_reversed[1::2]

    for even in even_numbers:
        even = int(even)
        sum_of_even_numbers += even


    
def main():
    card_number = "837-133-64"
    card_translation = str.maketrans({"-": "", "": " "})
    card_translated = card_number.translate(card_translation)
    

main()