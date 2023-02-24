def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    score = 0

    for key in questions:
        print('-------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)

        answer = input('Your answer is: ').upper()
        guesses.append(answer)
        check = check_answer(questions.get(key),answer,score)
        #if (check_answer(questions.get(key),answer,score)):
        if check:
            score += 1
            display_score(score)
        else:
            display_score(score)
        question_num += 1
    final_score(score,guesses)

def check_answer(right_answer,your_answer,score):
    if right_answer == your_answer:
        print('Correct!')
        return 1
    else:
        print('Incorrect!')
        return 0
def display_score(score):
    print ('Your socre is: '+str(score*2))

def final_score(score,guesses):
    print('----------------')
    print('Result: ')
    print('Right Answer: ',end='')
    print()
    for i in questions:
        print(questions.get(i),end=' ')
    print()
    print ('----------------')
    print ('Your answer: ',end='')
    print()
    for i in guesses:
        print(i,end=' ')
    print()
    print("You 've ace "+str(score)+'/5')
    print('Your final score is '+str(score*2))
def play_again():
    check_play = input('Do you want to play again? (YES/NO)').upper()
    if check_play == 'YES':
        return True
    else:
        return False
questions = {
    '1+1 = ? ':'A',
    '2+2 = ? ':'B',
    '0x5 = ? ':'D',
    '8x10 = ? ':'C',
    '1+9 = ?': 'B'
}
options = [['A.2','B.3','C.6','D.7'],
            ['A.2','B.4','C.6','D.7'],
            ['A.2','B.3','C.6','D.0'],
            ['A.2','B.3','C.80','D.7'],
           ['A.2','B.10','C.6','D.7']]
new_game()
while play_again():
    new_game()
print('Byeeeeeee! See you again!')