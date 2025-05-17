import random


# Create virables 

jokes = [
    "Why do programmers prefer dark mode? Because light  attracts bugs",
    "Why do programmers prefer coffes ☕? Because it's the only constant in their lives.",
    "Ek aadmi ne apne dost se poocha, 'Tumhare paas kitne phone hain?'Dost ne kaha, 'Mere paas sirf ek pho hai, aur usse main tumhe nahin doonga, kyunki main usse nahin chalta!"
    "Ek aadmi ne apne dost se poocha, 'Tumhare paas kitne kapde hain?' Dost ne kaha, 'Mere paas sirf ek kapda hai, aur usse main tumhe nahin doonga, kyunki main usse nahin nikalta!'"
    "Ek aadmi ne apne dost se poocha, 'Tumhare paas kitne paise hain?' Dost ne kaha, 'Mere paas sirf ek rupya hai, lekin main usse tumhe nahin doonga!'"
]
prompt = "What you want : "
sorry = "Sorry I only tell jokes"


# Function

def bot():

    # user input
    user_inpt = input(prompt)


    #condition
    if "joke" in user_inpt:
        print(random.choice(jokes))

    else:
        print(sorry)


# cell function
bot()

