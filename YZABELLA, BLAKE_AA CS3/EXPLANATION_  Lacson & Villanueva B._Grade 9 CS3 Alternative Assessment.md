# **Mini Plants vs Zombies Game**

Grade 9 Computer Science 3  |  First Quarter  |  Pair Activity  | Alternative Assessment  |  100 points

**Create a short Python game that runs in the terminal. One Plant protects a lane from one Zombie. Use classes and objects to make them interact. You will plan, draw a UML class diagram, code, test, and explain your work with your partner.**

Partners: Blake Villanueva  Yzabella Lacson

Section: Neon  Date: 09/30/2026

# 

DECOMPOSITION:

There are two classes; namely, the Plant class and the Zombie class. The Plant class defines the attributes and methods of what a plant should do in our game, while the Zombie class defines the attributes and methods of what a zombie should do in our game. A plant should have the attributes: name, health, and damage and methods: attack and take\_damage. On the other hand, a zombie should have the attributes: name, health, damage, and distance and methods: move, attack, and take\_damage.

PATTERN RECOGNITION:

In every turn of the match, several repetitive actions and structural checks are being performed. The game must constantly show the status overview showing current health points and spatial distance at the start of each cycle of each variable. It also evaluates the custom health fields before allowing any object to attack, ensuring that defeated plants cannot strike and a defeated zombie cannot move anymore. In addition,  the game repeatedly evaluates the zombie’s proximity metric— if greater than zero, it moves, but when it is lesser than zero, it turns into attack mode

Abstraction:

We only maintain the information needed for combat and remove unnecessary things. For plants, this means tracking name, health, and damage. For the zombie, we only track name, health, damage, and distance.

Algorithm Design: 

First, it initiates all characters with their starting stats and characteristics. Second, it starts a loop that runs while the zombie and at least one plant is alive. Third, Plant 1 attacks if still alive, stopping the game if the zombie dies. Fourth, Plant 2 attacks if alive, also checking if the zombie dies. Fifth, the zombie moves closer if distance is above zero; otherwise, it bites the first living plant and will eventually kill it unless it dies due to the damage being taken. Finally, the loop ends when the plants or the zombie wins, and the game prints the final result. 

