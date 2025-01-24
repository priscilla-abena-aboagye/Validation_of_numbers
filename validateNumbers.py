def verify_card_number(card_number):
    sum_of_odd_numbers = 0
    card_number_reversed = card_number[-1:-5:-1]
    odd_digits = card_number_reversed[::2]


    
def main():
    card_number = "837-133-64"
    card_translation = str.maketrans({"-": "", "": " "})
    card_translated = card_number.translate(card_translation)
    

main()