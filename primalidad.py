while 1:

    def primo(num):

        count = 0

        if num == 1: return False
        elif num == 2: return True
        elif num % 2 == 0: return False
        else:
            for i in range(1, num+1):
                if i == 1 or i == num:
                    continue
                if num % i == 0:
                    count += 1
        
        if count == 0: return True
        else: return False

    def run():
        num = int(input('num:\n'))
        if primo(num): print(f'{num} es primo')
        else: print(f"{num} es primon't")

    if __name__ == '__main__': run()