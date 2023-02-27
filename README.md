# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Milestone 1 
Setting up the environment
---
Milestone 2
The preliminary game logic for the overall project was established here. The main objective was to introduce control flows such as if else to help check user's input. The file milestone_2.py was created which contained the code for this milestone and  it contained random list called word_list wherein random choice of words can be selected at intervals. 


> Snapshot of Milestone 2

![](images/Screenshot%202023-01-21%20at%2010.25.45.png)


You should use an if statement to check if the letter entered by the user is in the word. Remember that the input should be stored in a variable called "guess" and the randomly picked word should be stored in a variable called "word". You can use the "in" operator to check if a character is in a string. If you think you have done it correctly, remember to use the right indentation for the if statement and just a single space between the "if" keyword and the condition

Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer. For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".

Step 1. Create an if statement that checks if the guess is in the word.

Step 2. In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.

Step 3. Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.





Milestone 2
Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

Example below:

/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:
"""Insert your code here"""
Insert screenshot of what you have built working.

Milestone n
Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

Conclusions
Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

Read through your documentation, do you understand everything you've written? Is everything clear and cohesive??