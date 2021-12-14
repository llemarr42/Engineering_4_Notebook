# Engineering_4_Notebook
My notebook for engineering 4.


## Table of Contents
* [Basics](#Basics)
* [Python_Dice_Roller](#PythonDiceRoller)
* [Python_Calculator](#Python_Calculator)
---

### Assignment Description

Write your assignment description here. It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here.  You need to communicate what your thing does. For code only assignments like the Python calculator, include a screenshot of the output of the code.

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here.

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

** Don't forget to **COMMENT YOUR CODE** before you upload to Github!

## Python_Dice_Roller

Okay so I am giving you a freebie so you have an example of the kind of reflections that I want. I'll start you off with an example for dice_roller.py, then its up to you to start your reflections with the Python calculator and all subsequent assignments. You can delete this section from your personal readme. 

### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

Vanilla version:

![Screenshot 2021-09-10 3 15 26 PM](https://user-images.githubusercontent.com/89222808/133513775-a3eafb43-f836-4e4f-8aa6-e28ca584901f.png)

Spicy version:

![Screenshot 2021-09-10 3 18 38 PM](https://user-images.githubusercontent.com/89222808/133513750-727cdb6c-1c27-4c8a-83d4-50ea9136a221.png)

### Wiring

N/A

### Reflection

This assignment was relatively simple, but was challenging because I had not coded in Python for several months. I learned that I could import parts of toolboxes without importing the entire thing, but that changes the syntax of how I call the function later. I also learned about using a while loop to control whether a user wants to exit the program. For the spicy version, I needed to use nested loops. Python determines what is inside a loop by the indent level of each line of text, rather than brackets like some other coding styles. That means I need to be really careful with my tabs!


## Python_Calculator

### Assignment Description

The purpose of this assignment was to create a program, in which if you input two numbers it outputs the sum, difference, product, quotient, modulo. The spicy version would have you write code to find both factorials. The main feature in the code hat makes all of this work is a function.


### Evidence 

![spicy_calculator](https://user-images.githubusercontent.com/56924009/135490197-223c69d2-6950-4909-b681-342d041c2ea0.PNG)


### Wiring

N/A

### Reflection

While the code for the math itself was pretty easy I had trouble understanding functions and how they work in python. I learned that functions are basically peices of code that are seperated from the rest of the code and can be called to run the code anywhere on your program. This let's us write the code to do some math once and instead of retyping it everytime we want to use it i can just call the function.


## Quadratic Solver

### Assignment Description

In this assignment I need to make a code that lets someone type in three coeffecients then the code gives them standard form and vertex form for the numbers, as well as, printing all Real roots. If there are no real roots it will say "There are no real roots" and if there is only one real root then it will print that one root

### Evidence

![quadratic](https://user-images.githubusercontent.com/56924009/136056613-23a82fed-30a2-4504-a05a-32d4757a0d87.PNG)


### Wiring

N/A

### Reflection

This assignment was relatively difficult. The code used to find the roots was easy as I could just use the quadratic formula, but i still stuggled with functions and in order to print the quadratic and vertex forms I needed to explore the world of f.strings.  f.strings let me put in variable that I can change into the text. This means I can directly put the coeffecients that were entered into the formula. 


## Strings and loops

### Assignment Description

This assignment had me let someone enter text then the code would print there text with each character being on a new line. Another requirement is that I needed to find a way to replace all spaces with dashes. 

### Evidence

![strings and loops](https://user-images.githubusercontent.com/56924009/136058716-718568e6-1e3d-40b4-9003-3cce5b119881.PNG)

### Wiring

N/A

### Reflection

This assignment was extremely easy. I used input to have them type in their text then I used the .replace command to replace the spaces with dashes and "for x in txt:" to loop for each character then printed x to print each character on the lines. for the spicy version I realised I could instead of defining a variable I could use it directely and add .replace at the end of the input command in parenthesis. I can plug this direcely into the for loop and add the print at the end of this line after the colon instead of another line. This let's me bring it down to one line of code. 


## Man Shaped Piniata

### Assignment Discription

In this assignment we create a game of hangman. We need to write code that lets one person enter a word then clears the screen. The code needs to print dashes for each letter in the first persons word that replaces each dash with the corrasponding letter when the letter is correctly guessed by the second person. It also needs to slowly print a "Man Shaped Piniata" whenever the player guesses a wrong word.

### Evidence 

![MSP game over](https://user-images.githubusercontent.com/56924009/136997048-cbd18755-e192-4c27-91c7-5ad38b579570.PNG)

### Wiring

N/A

### Reflection

This assignment was much harder than the ones previous. The individual peices of code wasn't terribly bad once you found the proper commands for each situation. The hard part was finding those peices of code and the logic behind them. the hardest part for me was getting dashes for each character in the word then when a correct letter was guessed it would replace the corresponding dash with the letter so that it is in the correct position. Then it would keep the letter there even after another letter was guessed. I did this using
```python
    for place in range(len(word)):
        if word[place] in cguess: 
            PrettyDash = PrettyDash[:place] + word[place] + PrettyDash[place+1:]
    PrettyDash = " ".join(PrettyDash)
    print( PrettyDash+"\n")

```
The for loop repeats this for evey character in the word and the place variable increaces every run because it represents the number of runs. This lets us have a loop for each character and IF the correct guess is the same as the character in that place in the word it will replace the dash with the correct letter. It also uses a .join so that people can see individual dashes and letters instead of a single line or a line with a random letter in there.


## CAD_Swing_Arm 

### Assignment Description

This assignment asked me to replicate a swing arm part from a set of drawings. The assignment style is similar to a portion of the Onshape Associate Certification test.

### Evidence 

Configuration #1

![Screenshot 2021-10-13 10 10 05 PM](https://user-images.githubusercontent.com/89222808/137238893-1fb00671-a56e-4945-a0b9-d2524f2dbd67.png)

Configuration #2

![Screenshot 2021-10-13 10 09 47 PM](https://user-images.githubusercontent.com/89222808/137238944-1d552151-7784-423e-88ad-8f4976325d97.png)

### Part Link
[Swing Arm Part](https://cvilleschools.onshape.com/documents/560f518c7146c0afa18c51b2/w/1c9597ad9f27f3add1f7628a/e/a23b437cbbe6d280d9ae8147?renderMode=0&uiState=61679087c315473a0613d09d)


### Reflection
Creating this part from a drawing was more difficult than I expected. Combining the different drawing views with the various dimensions took several tries. Even though the part was made with simple extrudes, they were combined in relatively complex ways. Next time, I will spend more time analyzing the drawings before I actually start making the part!

## CAD Intro 2.1-2.4

### Assignment discription

This assignment had me follow a specific guide to learn about better ways to use onshape. The guide shows how to make a skateboard with annoyingly long discriptions of even the simplist of steps.

### Evidence

Above:

![skate_board_above](https://user-images.githubusercontent.com/56924009/138732188-a7bfc111-a888-41be-8d2f-eeb0c7b3db28.PNG)

Below:

![skate_board_below](https://user-images.githubusercontent.com/56924009/138732234-48271190-125d-44cf-bc39-e961e178d7ea.PNG)

### Part Link

[Skate Board](https://cvilleschools.onshape.com/documents/02a3bdb7560bbd6eba62ac0c/w/3826835c15a8a4d79458bd4e/e/116c7ba04daebba8b507582a?renderMode=0&uiState=6176d81ff3dc6f187fbba27c)

### Reflection

I had an easy time with this assignment but i still learned different things about onshape. I learned how to use onshape hotkeys in order to make navigating easier. For example pressing 'd' while in a sketch will let you diminsion without having to search for it in the tool bar. This assignment takes you through all of the essential tools of onshape giving intructions on how to use them and letting you use them.


## Intro to CAD - 3.1-3.4

### Part 1

### Assignment discription

This part of the assignment walks you through making a 2x4 lego. It uses variables and linear patterens to make the work much more efficient. The lego is shelled and has a interior circle to frition fit them together.

### Evidence


![lego_pt#1](https://user-images.githubusercontent.com/56924009/140966328-5f2b6ba5-fa4f-4abf-85b2-7e3bbd5a5208.PNG)

### Part Link

[link to onshape](https://cvilleschools.onshape.com/documents/d37b93323282622ca2243810/w/4092018e193b380a1a85fc93/e/171ec6c646bc5d45b9f77c64?configuration=List_4DD4kvPICY7y3l%3DYellow%3BList_Raq6P3Ugc5A5hj%3DBrick%3BList_e6K3ouphLFZ9dW%3DDefault&renderMode=0&rightPanel=variableTablePanel&uiState=618aa4779b6f281ec18cd63f)

### Reflection

I this part of the assignment I learned more about variables and ways they can be used. I had not previously known they could be used anything but sketches and extrudes, but this section showed me that variables can be used for so much more. Variables were used in linear patterns and for all the diminsions, but the biggest thing that i learned is that you can use math with the variable in each feature. For example there is a variable for the amount of studs in a row and by using math we can make the side length change for the amount of studs in a row.

### Part 2

### Assignment discription 

This part of the assignment teaches you how to use configuration and a lot of different ways to use them. It also shows how to add and use custom tools in onshape. We use these features to create a lego that we can change to a wide veriety of different shapes and sizes with a click of the button instead of changing every feature with a long process.

### Evidence

![lego_pt#2](https://user-images.githubusercontent.com/56924009/140973928-d8fd033b-c82e-4e3f-85f2-52a5d43d874c.PNG)

### Part Link

[link to onshape](https://cvilleschools.onshape.com/documents/d37b93323282622ca2243810/w/4092018e193b380a1a85fc93/e/171ec6c646bc5d45b9f77c64?configuration=List_4DD4kvPICY7y3l%3DYellow%3BList_Raq6P3Ugc5A5hj%3DBrick%3BList_e6K3ouphLFZ9dW%3DDefault&renderMode=0&rightPanel=variableTablePanel&uiState=618aa4779b6f281ec18cd63f)

### Reflection

This is the part of the assignment in which I learned the most. In this part I learned how to use configurations and how to combine them with variables to make changes to lego. Configurations let you change the values of the variables into predetermined numbers that you enter into the configurations table. This lets you change multiple variables at once by changing which configuration you are using at the top left. Configurations also let you supress certain features in certain configurations, which can be helpful to make some things not break as you change their size.

### part 3

### Assignment discription

This part of the assignment walks you through the assembly phase. It has you make a simple duck out of the legos you made in previous parts. The configurations that were previously made start to really shine because we can now import any configuration that we can set up letting us make our assembly with any lego we can think of and set up. We use snap mode to put the peices together then once it is done we find the ducks center of mass.

### Evidence

![DUCK](https://user-images.githubusercontent.com/56924009/141337377-29b2de7e-d1cb-4a32-b561-934f8a94a3d7.PNG)

### Part Link

[link to onshape](https://cvilleschools.onshape.com/documents/d37b93323282622ca2243810/w/4092018e193b380a1a85fc93/e/171ec6c646bc5d45b9f77c64?configuration=List_4DD4kvPICY7y3l%3DYellow%3BList_Raq6P3Ugc5A5hj%3DBrick%3BList_e6K3ouphLFZ9dW%3DDefault&renderMode=0&rightPanel=variableTablePanel&uiState=618aa4779b6f281ec18cd63f)

### Reflection

This part of the assignment taught me a few tricks I had no Idea about the main one being the snap feature. The snap feature lets you instantly "snap" two parts together when you drag them together. This speeds up the work by a lot and makes everything much easier, especially in this sort of assembly where you have a bunch of smaller, simular peices. Another thing that sped things up was the ability to insert any configuration combination diretly into the assembly. This lets you get a 2x4 yellow block the press two button and get a 1x3 red plate in a couple seconds instead of another time consuming prrocess to recreate every single variation.

### part 4

### Assignment discription

This part of the assingment focuses on making a instution manual for your assemblies. The manual is a relatively simple and easy way for someone to completely reconstruct your assembly, given that they have the tools to do so. We put our assemblies into a drawing with multible views of it as well as a list of all the materials with the materials labeled in one of the images.

### Evidence

![drawing](https://user-images.githubusercontent.com/56924009/142025783-1cdc4f87-32c8-49ba-a51a-1cea654d3e1e.PNG)

### Part Link

[link to onshape](https://cvilleschools.onshape.com/documents/d37b93323282622ca2243810/w/4092018e193b380a1a85fc93/e/171ec6c646bc5d45b9f77c64?configuration=List_4DD4kvPICY7y3l%3DYellow%3BList_Raq6P3Ugc5A5hj%3DBrick%3BList_e6K3ouphLFZ9dW%3DDefault&renderMode=0&rightPanel=variableTablePanel&uiState=618aa4779b6f281ec18cd63f)

### Reflection

I have not made anything like this before so i learned multiple things during this part of the assignment. I learned how to create a drawing of my assembly instantly by right clicking the assembly and hit create drawing. This lets you create a new tab for your drawing that you can choose to have a four view drawing or blank drawing for you to add your own stuff to. Another thing that i learned that was really useful was the BOM table or Bill Of Materials. We can set up the BOM table in the assembly tab and edit what we want it to display. After we do that we can add the BOM table to the drawing in a couple clicks. Then we can use the callout tool to label the different peices in the drawing of the assembly with numbers corresponding  to that on the BOM table.

## RPi GPIO Pin Introduction

### Assignment discription

In this assignment we get fimiliar with diffferent naming conventions for the pins and different peices of code that control them. The Python script we wrote was to blink two LEDs so that when one was on the other was off and have script that describes what is happening in the serial monitor. The Python code needs to be written and run on the Raspberry Pi.

### Evidence 

https://user-images.githubusercontent.com/56924009/143916987-87879754-65ae-4328-b800-0fc1e6a88700.MOV

### Wiring

![unnamed](https://user-images.githubusercontent.com/56924009/143917198-831a493f-eb58-4a0d-be98-b88bae1ac794.jpg)

### Reflection

I was not aware of any of these naming conventions, so I learned a lot about what the different things mean. I learned the most about the BCM because it is the one I used for the coding. I learned multiple commands that manually effect the pin slots letting me change their function and if they are on or off if it is an output. When writing script on the raspberry pi you first can choose your prefered naming covention e.x. GPIO.setmode(GPIO.BCM) sets it to BCM. Then you can setup individual pins with GPIO.setup(21, GPIO.OUT)
and only then can you really write your code.

## RPi Safe Shutdown Button

### Assignment discription

This assignment has you create a button on your breadboard that restarts your pi when pressed once or shuts down when held down. The majority of the steps and code are on an externel site that has all the code you need and tells you what to change in order to make it work without some devices like the Qwiic pHAT. This is all useful because it lets you safely shut down and reboot your pi while it is not connected to a computer.

### Evidence 

https://user-images.githubusercontent.com/56924009/144470154-7738501c-a1b8-4a06-8849-ea6d0067e12f.MOV

### wiring

![wiring_shut_down](https://user-images.githubusercontent.com/56924009/144470974-68bc17cd-fe62-4f7c-8016-8d3d47e95bf3.jpg)

### Reflection

In this assignment i learned more about different parts and how code can affect them. Something that i had not previously known was that there is an internal resistor like function in the pi that you can access and activate with code allowing you to no need a resistor in the wiring. Another thing that you can do is go into base files in your pi  and change or add to it's base code, which we used in this project to get our code to be constantly running in the background.

## GPIO Pins - I2C

### Assignment discription

In this assignment we
