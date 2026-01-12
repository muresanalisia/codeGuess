import random

class Game:
    def __init__(self):
        pass

    def generate_secret_number(self):
        mii=random.randint(1,9)
        while True:
            sute=random.randint(0,9)
            if sute!=mii:
                break
        while True:
            zeci = random.randint(0,9)
            if zeci!=mii and zeci!=sute:
                break
        while True:
            unitati = random.randint(0,9)
            if unitati!=mii and unitati!=sute and unitati!=zeci:
                break
        secret_number=mii*1000+sute*100+zeci*10+unitati
        return secret_number

    def digits(self, number):
        number_digits = []
        copie_number = number
        for i in range(4):
            number_digits.append(copie_number % 10)
            copie_number = copie_number // 10
        return number_digits

    def validate_code(self, number):
        if number>9999 or number<1000:
            return False
        digits = self.digits(number)
        for i in range(0, 3):
            j=i+1
            while j<=3:
                if digits[i]==digits[j]:
                    return False
                else:
                    j=j+1
        return True


    def count_runners(self, number, secret_number):
        runners_contor = 0
        secret_number_digits = self.digits(secret_number)
        number_digits = self.digits(number)
        for i in range(4):
            if number_digits[i] in secret_number_digits:
                if number_digits[i]!=secret_number_digits[i]:
                    runners_contor+=1
        return runners_contor

    def count_codes(self, number, secret_number):
        codes_contor = 0
        secret_number_digits = self.digits(secret_number)
        number_digits = self.digits(number)
        for i in range(4):
            if number_digits[i] in secret_number_digits:
                if number_digits[i]==secret_number_digits[i]:
                    codes_contor+=1
        return codes_contor





