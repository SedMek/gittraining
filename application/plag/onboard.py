from time import sleep
from random import randint

def main(tenant):
    '''Onboarding a new customer has never been easier'''
    print(f'Onboarding {tenant}...')
    sleep(randint(1, 3))
    print(f'Onboarding {tenant} done!')

if __name__ == "__main__":
    main('plag')
