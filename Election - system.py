

# This is a sample Python script.

import time

import random

import datetime

candidate_1_biography = '\nDonald John Trump was a real - estate developer and businessman who licensed'\
                        '\nhis name to several hotels, casinos, golf courses, resorts, and residential properties in' \
                        '\nNew City and around the world. From the 1980s Trump also lent his name to scores of retail' \
                        '\nventures including branded lines of clothing, cologne,and furniture and to his University' \
                        '\nWhich offered real-estate education from 2005 to 2010. Trump got married to super model' \
                        '\nMelania Trump, who later gave birth a year later.'

candidate_2_biography = 'Joseph Robinette Biden Jr was raised in Scranton Pennsylvania and New Castle, Delaware. ' \
                        '\nHe received a bachelors degree from the University of Delaware in 1965 and a law degree ' \
                        '\nfrom Syracuse University in New York in 1968.During this time, he married Neila Hunter' \
                        '\nand the couple later had three children. After graduating from high school, Biden returned' \
                        '\nto Delaware to work as an attorney before quickly turning to politics, serving on the New' \
                        '\nCastle country council from 1970 to 1972.'

born = 'Born : June 14, 1946 (New York City, New York)'
spouse = 'Spouse : Melanie Trump'
political_affiliation = 'Political Affiliation : Republican Party'
Notable_works = 'Notable Works : Crippled America, Trump : The Art of the Deal, Billionaires club'
record = 'Record : Owner of second largest yacht'
Children = 'Children : Donald jr, Ivanka, Eric, Tiffany, Barron'
net_worth = 'Net Worth 2.7 Billion dollars as at 2021'
source = 'Source : www.washingtonPost.com'

born_2 = 'Born : November 20, 1942 (Scranton pennsylvania)'
political_affiliation_2 = 'Political Affiliation : Dominican Party'
net_worth_2 = 'Net worth : unknown'
Award = 'Award and Honours : Presidential Medal of Freedom'
spouse_2 = 'Spouse : Jill Biden'
source_2 = 'www.washingtonPost.com'

time.sleep(2)
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\tWELCOME TO MY VOTING PROJECT!')
vote_count = 1

null = ''

pin = 25200615

party_1 = 'Republican'
party_2 = 'Dominican'

candidate_1 = 'Donald Trump'
candidate_2 = 'Joe Biden'

option_1 = 'A. VOTE'
option_2 = 'B. CREATE VOTERS ACCOUNT'
option_3 = 'C. CHANGE CURRENT PARTY'
option_4 = 'D. CREATE VOTERS CARD'
option_5 = 'E. VIEW ELECTION COUNTS'

time.sleep(3)

print(option_1)
time.sleep(2)
print(option_2)
time.sleep(2)
print(option_3)
time.sleep(2)
print(option_4)
time.sleep(2)
print(option_5)

time.sleep(2)
print('\nCandidate Names : ')
time.sleep(2)
print('\n1.', candidate_1)
time.sleep(1)
print('2.', candidate_2)

time.sleep(3)
user_input = input('\nWhat Would You Like To Do Today? : ')

if user_input == 'A':
    time.sleep(2)
    vote_input = input('\nEnter the name of the Candidate : ')

    while vote_input == null:
        time.sleep(2)
        print('sorry, your input has to contain a name.')
        time.sleep(2)
        print('Restart program to input a name!')
        exit()

    time.sleep(2)
    choice_input = input('Are You Sure Of Your Option, YES or NO : ')

    if choice_input == 'YES':
        time.sleep(2)
        print('Alright')
        time.sleep(2)
        print('Casting Vote...')
        time.sleep(6)
        print('Vote successful!')
        time.sleep(2)
        print('You Just Voted for', vote_input)

        time.sleep(2)
        bio_input = input('Do you want to read his biography, YES or NO : ')

        if bio_input == 'YES':

            while vote_input == candidate_1:
                time.sleep(2)
                print('Preparing Biography...')
                time.sleep(4)
                print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;36mDONALD TRUMP BIOGRAPHY')
                time.sleep(2)
                print(candidate_1_biography)
                time.sleep(2)
                print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tADDITIONAL INFORMATION')
                time.sleep(2)
                print(born)
                time.sleep(2)
                print(spouse)
                time.sleep(2)
                print(political_affiliation)
                time.sleep(2)
                print(Notable_works)
                time.sleep(2)
                print(record)
                time.sleep(2)
                print(Children)
                time.sleep(2)
                print(net_worth)
                time.sleep(2)
                print(source)
                exit()

            while vote_input == candidate_2:
                time.sleep(2)
                print('Preparing Biography...')
                time.sleep(4)
                print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;36mJOE BIDEN BIOGRAPHY')
                time.sleep(1)
                print(candidate_2_biography)
                time.sleep(2)
                print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tADDITIONAL INFORMATION')
                time.sleep(2)
                print(born_2)
                time.sleep(2)
                print(political_affiliation_2)
                time.sleep(2)
                print(Award)
                time.sleep(2)
                print(net_worth_2)
                time.sleep(2)
                print(source_2)
                exit()

        elif bio_input == 'NO':
            time.sleep(2)
            print('Alright, Thank you for voting!')
            time.sleep(2)
            exit_input = input('Press x to exit : ')
            if exit_input == 'x':
                print('exiting...')
                time.sleep(2)
                exit()

        elif bio_input == null:
            time.sleep(2)
            print('Input Bar Empty!')
            time.sleep(2)
            print('exiting...')
            time.sleep(2)
            exit()

        else:
            time.sleep(2)
            exit()

    elif choice_input == 'NO':
        time.sleep(2)
        print('exiting...!')
        time.sleep(2)
        print('Program Terminated!')
        exit()

    elif choice_input == null:
        time.sleep(2)
        print('Input Bar empty!')
        time.sleep(2)
        print('exiting...')
        time.sleep(2)
        exit()

    else:
        time.sleep(2)
        print('Invalid Input')
        time.sleep(2)
        exit()


if user_input == 'B':
    time.sleep(2)
    name_input = input('Enter Your Name : ')
    time.sleep(2)
    age_input = int(input('Enter Your age : '))

    while age_input < 18:
        time.sleep(2)
        print('detecting error...')
        time.sleep(4)
        print('sorry, You are not eligible to vote!')
        exit()

    while age_input > 120:
        time.sleep(2)
        print('Invalid age input')
        time.sleep(2)
        exit()

    time.sleep(2)
    party_id = input('Enter Political Affiliation (Republican or Dominican) : ')
    time.sleep(2)

    while party_id == null:
        time.sleep(2)
        print('Input bar empty')
        time.sleep(2)
        print('program terminated!')
        exit()

    print('\nCreating account...')
    time.sleep(6)
    print('Account created successfully!')
    time.sleep(2)
    print('You are now a verified voter!')
    time.sleep(2)
    print('\nPreparing account details...')
    time.sleep(4)
    print('\nName : ', name_input)
    time.sleep(2)
    print('Age : ', age_input)
    time.sleep(2)
    print('Political Affiliation : ', party_id)
    time.sleep(2)
    print('Date : ', datetime.datetime.now())

    time.sleep(3)
    id_input = input('\nPress 0 to get your Id number : ')

    if id_input == '0':
        time.sleep(2)
        print('\nFetching user id...')
        time.sleep(5)
        print('\nYour Id - number is ', random.randint(1, 90000000))
        time.sleep(2)
        print('Notice : ensure not to forget your Id - number')
        time.sleep(3)
        print('\nThank You for using our service!')
        time.sleep(2)

    elif id_input == null:
        time.sleep(2)
        print('Input bar empty!')
        time.sleep(2)
        print('restart process to get id - number.')

    else:
        time.sleep(2)
        print('Invalid input')
        time.sleep(2)
        print('exiting by default...')
        time.sleep(2)
        exit()

    exit_input = input('\npress x to exit : ')

    if exit_input == 'x':
        time.sleep(2)
        print('exiting...')
        time.sleep(1)
        exit()

    elif exit_input == null:
        time.sleep(2)
        print('Invalid input!')
        time.sleep(2)
        print('program terminated!')

    else:
        time.sleep(2)
        print('Invalid Input')
        time.sleep(2)
        exit()

if user_input == 'C':
    time.sleep(2)
    c_input = input('\nAre you sure of your option, YES or NO : ')

    if c_input == 'YES':
        time.sleep(2)
        party_input = input('Enter your Current party - (Republican or Dominican): ')
        time.sleep(2)
        c_party_input = input('Enter the party you wish to change to - (Republican or Dominican) : ')
        time.sleep(2)
        v_name_input = input('Enter your name : ')

        if party_input == c_party_input:
            time.sleep(2)
            print('\ndetecting error...')
            time.sleep(4)
            print('sorry, you cannot switch within a single party.')
            time.sleep(2)
            print('exiting...')
            time.sleep(1)
            exit()

        elif party_input != c_party_input:
            time.sleep(2)
            print('\nProcessing...')
            time.sleep(6)
            print('\nChange successful!')
            time.sleep(3)
            print('You are now a certified member of the', c_party_input, 'Affiliation')
            time.sleep(2)
            print('Thank You for patronizing us!')

            c_exit_input = input('\nPress x to exit : ')

            if c_exit_input == 'x':
                time.sleep(2)
                print('exiting...')
                time.sleep(2)
                exit()

            elif c_exit_input == null:
                time.sleep(2)
                print('Input bar empty!')
                time.sleep(2)
                print('exiting program...')
                time.sleep(2)
                exit()

            else:
                time.sleep(2)
                print('Invalid input')
                time.sleep(2)
                print('Program terminated!')

        elif party_input == null:
            time.sleep(2)
            print('Invalid input')
            time.sleep(2)
            print('restart process!')
            time.sleep(2)
            exit()

        elif c_party_input == null:
            time.sleep(2)
            print('Invalid input')
            time.sleep(2)
            print('restart program!')
            time.sleep(2)
            exit()

        else:
            time.sleep(2)
            print('Error!')
            time.sleep(2)
            exit()

    elif c_input == 'NO':
        time.sleep(2)
        print('\nAlright, thank you for using our service! ')
        time.sleep(2)
        print('We appreciate your participation!')

        n_exit_input = input('Enter x to exit : ')

        if n_exit_input == 'x':
            time.sleep(2)
            print('exiting...')
            time.sleep(2)
            exit()

        elif n_exit_input == null:
            time.sleep(2)
            print('Invalid input')
            time.sleep(2)
            print('Program terminated by default')
            exit()

        else:
            time.sleep(2)
            print('Invalid input')
            time.sleep(2)
            print('Program terminated!')

    elif c_input == null:
        time.sleep(2)
        print('Input bar empty')
        time.sleep(2)
        print('exiting by default...')
        time.sleep(2)
        exit()

    else:
        time.sleep(2)
        print('Invalid input')
        time.sleep(2)
        print('Program terminated!')
        exit()


if user_input == 'D':
    time.sleep(2)
    print('\nYour Pin Number : ', pin)

    time.sleep(2)
    c_name_input = input('Enter Your Name : ')
    time.sleep(2)
    c_age_input = int(input('Enter Your age : '))
    time.sleep(2)

    while c_age_input < 18:
        time.sleep(2)
        print('sorry, You are not eligible to own a voters card')
        time.sleep(2)
        print('Your age should be at least eighteen and above!')
        time.sleep(2)
        exit()

    while c_age_input > 120:
        time.sleep(2)
        print('Invalid age input!')
        time.sleep(2)
        print('Restart process and enter a valid age')
        time.sleep(2)
        exit()

    state_id = input('Enter Your state of residence : ')
    time.sleep(2)
    pin_input = int(input('Enter Your Pin : '))

    while pin_input != pin:
        time.sleep(2)
        print('Error : your pin is incorrect!')
        time.sleep(2)
        print('Restart process')
        time.sleep(2)
        exit()

    while pin_input == pin:
        time.sleep(2)
        print('\nCreating voters card...')
        time.sleep(6)
        print('Creation successful!')
        time.sleep(2)

        print('\nPreparing account details...')
        time.sleep(4)
        print('\nName : ', c_name_input)
        time.sleep(2)
        print('Age : ', c_age_input)
        time.sleep(2)
        print('State of residence : ', state_id)
        time.sleep(2)
        print('Pin : ', pin_input)

        time.sleep(2)
        batch_input = input('\nPress 0 to get batch number : ')

        if batch_input == '0':
            time.sleep(2)
            print('\nFetching batch number...')
            time.sleep(5)
            print('Your batch number is ', random.randint(1, 90000000))

        elif batch_input == null:
            time.sleep(2)
            print('Input bar empty')
            time.sleep(2)
            print('Restart process to get batch number!')
            time.sleep(2)
            exit()

        else:
            time.sleep(2)
            print('Invalid input')
            time.sleep(2)
            print('exiting...')
            time.sleep(2)
            exit()

        time.sleep(3)
        print('\nThank You for using our service')

        v_exit_input = input('\nPress x to exit : ')

        if v_exit_input == 'x':
            time.sleep(2)
            print('exiting...')
            time.sleep(2)
            exit()

        elif v_exit_input == null:
            time.sleep(2)
            print('Input bar empty!')
            time.sleep(2)
            print('program terminating...')
            time.sleep(2)
            exit()

        else:
            time.sleep(2)
            print('Invalid Input')
            time.sleep(2)
            print('exiting by default...')
            time.sleep(2)
            exit()

if user_input == 'E':
    time.sleep(2)
    view_input = input('\nEnter party (Republican or Dominican): ')

    if view_input == party_1:
        time.sleep(2)
        print('\nName of party : ', party_1)
        time.sleep(2)
        print('Party Representative : ', candidate_1)
        time.sleep(2)
        print('Current vote count : ', random.randint(1, 100000000))

        time.sleep(2)
        view_exit = input('\nPress x to exit : ')

        if view_exit == 'x':
            time.sleep(2)
            print('exiting...')
            time.sleep(2)
            exit()

        elif view_exit == null:
            time.sleep(2)
            print('Input bar empty!')
            time.sleep(2)
            print('Program terminated')
            exit()

        else:
            time.sleep(2)
            print('Invalid input')
            time.sleep(2)
            print('exiting by default...')
            time.sleep(2)
            exit()

    elif view_input == party_2:
        time.sleep(2)
        print('Name of party : ', party_2)
        time.sleep(2)
        print('Party Representative : ', candidate_2)
        time.sleep(2)
        print('Current vote count : ', random.randint(1, 100000000))

        time.sleep(2)
        view_exit = input('Press x to exit : ')

        if view_input == 'x':
            time.sleep(2)
            print('exiting...')
            time.sleep(2)
            exit()

        elif view_input == null:
            time.sleep(2)
            print('Input bar empty!')
            time.sleep(2)
            print('Program terminated')
            exit()

        else:
            time.sleep(2)
            print('Invalid input')
            time.sleep(2)
            print('exiting by default...')
            time.sleep(2)
            exit()
    else:
        time.sleep(2)
        print('Invalid party input!')
        time.sleep(2)
        print('Tip : enter the correct party name!')
        time.sleep(2)
        print('Program terminated!')
        exit()

elif user_input == null:
    time.sleep(2)
    print('Input bar empty!')
    time.sleep(2)
    print('Tip : restart program and fill in all fields!')
    time.sleep(2)
    print('Terminating program...')
    time.sleep(3)
    print('Program terminated!')
    exit()






























