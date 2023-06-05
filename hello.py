from flask import Flask
import random
app = Flask(__name__)

wrong_images_list = ["https://media1.giphy.com/media/GwskZm1jXg8cDvuZJ6/giphy.webp?cid=ecf05e47va13s49755g704t2vxag00it72glofik5twrpl1a&ep=v1_gifs_search&rid=giphy.webp&ct=g", "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzJkMWY4YWE4YzI0MzZiYzRiYzc0ZjFjYzFhYTcwNGI5NjFmOTZhMiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/HSvpy6Jk396SI/giphy.gif", "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTkxNTcwMTQyNGJjODljMzE3YzUzNGZhMGE2MjVhYmQ4MDA5ZWQ2NyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/fqst7AVqF6AVLlYklE/giphy.gif", "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMThlZjQ0YTZlNzFjOTdhZGIxMzY3ZmJhMTJlYWYzZjRhZDhlNWJiZCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/3OhXBaoR1tVPW/giphy.gif"]
wrong_image = ''
right_image = '"https://media1.giphy.com/media/QIlIdyDvueHQ85rABg/200w.webp?cid=ecf05e477kpp91434qzhdyvsen8icxl7rf1errlyvw48hb4e&ep=v1_gifs_search&rid=200w.webp&ct=g"'
number = random.randint(0, 9)

@app.route('/')
def hello_world():
    global number
    number = random.randint(0, 9)
    print(number)
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media2.giphy.com/media/9PrqNHPAdWyJVOXntF/200w.webp?cid=ecf05e47y9zg9t528pwahw8dh0sn0e3ih03rd496qsci7oa6&ep=v1_gifs_search&rid=200w.webp&ct=g">'

hello_world()

@app.route('/<int:number_guess>')
def guess_number(number_guess):
    if number_guess < number:
        wrong_image = wrong_images_list[random.randint(0, 3)]
        return f'<h1>Higher</h1>' \
            f'<img src={wrong_image}>'
    elif number_guess > number:
        wrong_image = wrong_images_list[random.randint(0, 3)]
        return f'<h1>Lower</h1>' \
            f'<img src={wrong_image}>'
    elif number_guess == number:
        return f'<h1>You got the right number</h1>' \
        f'<img src={right_image}>'

if __name__ == "__main__":
    app.run(debug=True)
    