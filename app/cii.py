from flask import Flask, request, render_template

app = Flask(__name__)


answers = ['Government', 'Transport (Land, Aviation, Maritime)', 'Healthcare',
           'Security and Emergency Services', 'Banking and Finance', 'Energy',
           'Water', 'Infocomm', 'Media']
correct = []

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method=='POST':
        guess = request.form['guess']
        
        if len(correct) == len(answers):
            message = 'Congratulations! You have gotten all the CIIs.'
        elif len(guess) < 4:
            message = 'Your guess is too short. Type at least 4 characters.'
        else:
            message = 'The guess is incorrect. Please try again'
            for answer in answers:
                if guess.lower() in answer.lower():
                    if answer in correct:
                        message = f'You have already guessed {answer}. Please try again.'
                    else:
                        correct.append(answer)
                        if len(correct) == len(answers):
                            message = 'Congratulations! You have gotten all the CIIs.'
                        else:
                            message = 'That is correct. Can you guess the other CIIs?'
                    break            
    else:
        message=''
    return render_template('main.html', message=message, table=correct)

if __name__ == '__main__':
    app.run()
