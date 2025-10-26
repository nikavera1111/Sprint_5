import random
import string

class Helpers:
    def make_random_email():
        letters_and_digits = string.ascii_letters + string.digits
        letters = string.ascii_letters
        rand_string = ''.join(random.sample(letters_and_digits, 8))
        rand_mail = ''.join(random.choice(letters) for i in range(5))
        rand_end = ''.join(random.choice(letters) for i in range(3))
        rand_email = rand_string + '@' + rand_mail + '.' + rand_end
        
        return rand_email
    
    def make_random_wrong_email():
        letters_and_digits = string.ascii_letters + string.digits
        rand_wrong_email = ''.join(random.sample(letters_and_digits, 8))
        
        return rand_wrong_email

    def make_random_product_name():
        letters_and_digits = string.ascii_letters + string.digits
        rand_name = ''.join(random.sample(letters_and_digits, 8))
        
        return rand_name
