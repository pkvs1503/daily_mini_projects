import random
# this will give randomness to our data what we have, here i have a list which contains some quotes. and i want to print it randomly so i m using random module.

def get_quote():
    quotes = [
        "Push yourself, because no one else is going to do it for you.",
        "Success doesn’t come from what you do occasionally.",
        "Dream big. Start small. Act now.",
        "Consistency is more important than intensity.",
        "Small progress is still progress."
    ]
    return random.choice(quotes)
# i want this method to return the quotes from the list randomly, so i m using random.choice() , which is built in method inside of random module.
#from this mini project i learnt use of random module and its method called choice()

def main():
    print("🔥 Welcome to Daily Motivation Generator 🔥")
    
    while True:
        print("\nHere is your quote:")
        print(get_quote())
        
        again = input("\nDo you want another quote? (yes/no): ").lower()
        # i did a input check here, by coverting all input which is by defualt a string to lower case, so all YES or yes will be yes only fo the program.
        if again != "yes":
            print("Keep Grinding 💪 See you tomorrow!")
            break

if __name__ == "__main__":
    main()
