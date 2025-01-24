def verify_card_number(card_number):
    pass


    
def main():
    card_number = "837-133-64"
    card_translation = str.maketrans({"-": "", "": " "})
    card_translated = card_number.translate(card_translation)
    

main()