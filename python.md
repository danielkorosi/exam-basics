# EXAM: Programming Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Create a `.gitignore` file so generated files won't be committed
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.
- **Don't push your work** to GitHub until your mentor announces that the time is up


# Tasks
## 1-3. Complete the following tasks: (~90 mins)
- [Odd Average](oddavg/odd_avg.py)
- [Copy](copy/copy.py)
- [BlackJack](blackjack/black_jack.py)

### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://google.github.io/styleguide/pyguide.html) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 4. Question time! (~10 mins) [4p]

### Name each building block of a method! [2p]

![anatomy](anatomy/anatomy_py.png)

#### Your answer:
[add your answer here]   
1: signature of the function
2: function name
3: parameter variable (from another point of view: argument)
4: body of the function
5: local variable
6: return statement
7: return value

### What is the constructor? When it is used? [2p]
#### Your answer:
[add your answer here]
In object-oriented programming, the constructor is responsible for initializing a class. In Python this is done by the __init__ method, which is called right after creating the class. The init method is different from 'regular' methods of the given class since it is called automatically every time a new instance of a class is created.
In the contructor, the argument 'self' has to be added in any case. The word 'self' is not a keyword but a convention to use it always as the first argument of the init method. 'Self' refers to the object of the class and so to every instances of the class. This is in contrast with the first arguments of "regular" methods, which are specific to a given instance. So the constructor is favoured to be applied when certain variables or procedures need to be shared among all instances of class. 
