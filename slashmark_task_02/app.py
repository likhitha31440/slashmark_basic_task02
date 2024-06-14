from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Initialize variables
number_to_guess = random.randint(1, 100)
number_of_attempts = 0


@app.route('/', methods=['GET', 'POST'])
def guess_the_number():
    global number_to_guess, number_of_attempts

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            number_of_attempts += 1

            if guess < number_to_guess:
                feedback = "Too low! Try again."
            elif guess > number_to_guess:
                feedback = "Too high! Try again."
            else:
                feedback = f"Congratulations! You guessed the number in {number_of_attempts} attempts."
                #
                number_to_guess = random.randint(1, 100)
                number_of_attempts = 0
        except ValueError:
            feedback = "Invalid input. Please enter an integer between 1 and 100."

        return render_template('index.html', feedback=feedback)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
