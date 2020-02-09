# Toy Robot Simulator

## Procedure for Execution

To perform the unittests and execute toy robot simulator.
Navigate to the extracted folder in your terminal and run the following commands.

```bash
python toy_robot_unittest.py
python app.py
```

#### Sketches of important points of simulator

##### Directions:

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; North\
West <--|-->East\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; South

##### Table Structure:
<table>
  <tr>
    <td>0,4</td>
    <td>1,4</td>
    <td>2,4</td>
    <td>3,4</td>
    <td>4,4</td>
  </tr>
  <tr>
    <td>0,3</td>
    <td>1,3</td>
    <td>2,3</td>
    <td>3,3</td>
    <td>4,3</td>
  </tr>
  <tr>
    <td>0,2</td>
    <td>1,2</td>
    <td>2,2</td>
    <td>3,2</td>
    <td>4,2</td>
  </tr>
   <tr>
    <td>0,1</td>
    <td>1,1</td>
    <td>2,1</td>
    <td>3,1</td>
    <td>4,1</td>
  </tr>
   <tr>
    <td>0,0</td>
    <td>1,0</td>
    <td>2,0</td>
    <td>3,0</td>
    <td>4,0</td>
  </tr>
</table>

##### Available commands: PLACE, MOVE, LEFT, RIGHT, REPORT, EXIT
where PLACE command has three parameters x_position, y_position and Direction (NORTH, SOUTH, EAST, WEST)

Available commands are stored as macros in seperate file for ease of accessibility.

#### Proposed Solution:
1) To create a class for ToyRobot for its placement, movements and position changes on the table.
2) Main function performs the functionality of getting input from the user and its validation using other sub functions.

#### Testcases:
1) Unit test to be carried out using unittest package in python.
2) Ad-hoc testcases for integration testing are also included in Testcases folder.

#### Solution Description:
REA Toy Robot Coding Challenge involves movements of toy robot across a table of 5x5 units without any obstructions. Here the challenge is solved using Python 3.6, involving a Class for the Toy Robot (toy_robot.py) with desired features as class variables and Toy Robot's functions as Class methods. The main function (app.py) is used to execute the simulator.

> #### Included files and their corresponding description
>
> - *app.py* - Includes main function to start/execute simulator
> - *toy_robot.py* - Toy Robot class file containing features and methods for its movement on table
> - *toy_robot_unittest.py* - Toy Robot unittest execution file in python
> - *macros.py* - Global constants (Available commands) and corresponding values
> - *README.md* - Higlights the important points and describes the solution
> - *PROBLEM.md* - Description of the given problem
> - *Testcases* - Contains Sample Testcases from PROBLEM.md file
> - *toy-robot_TESTCASES.py* - Documentation of all testcases verified with the simulator 
>

This challenge involves toy robot simulation of movements on a table in 5x5 size (as shown in above table). It's simple and powerful to implement using python programming. Therefore, this solution is developed based on OOP principles (Object-Oriented Programming). Here the class concept is implemented for the toy robot with its features as class variables and functions as class methods. Each major line of code is commented with its description. The sequence of program flow starts from main function, accessing the class contents using class object and renders the result using REPORT command.

> #### Important add-ons and special cases considered
>
> - *EXIT* - To quit the simulator, an extra command is recognized as `EXIT`
> - *Case Insensitive* - Enables the user to type the commands in Upper/Lower case and recognized properly
> - *Headers & Commands List* - Simulator lists out the headers and commands along with descriptions at start of the program
> - *Responsive Prompts* - Provides the warnings for the user if the command is not recognized or incorrect
> - *Eliminates majority of escape sequences* - Simulator removes the escape sequence characters, if users enters any. (For example: Up/Down/Left/Right Arrows, empty spaces)
> - *Ignores and warns user* - If the user enters MOVE/RIGHT/LEFT/REPORT command when the toy robot is not placed on the table, simulator warns the user by asking him/her to place the toy robot on the table
> - *Prevents Robot fall off* - When user tries to move robot off the table (>5x5), simulator shows the message that MOVE action is prevented and ignored
> - *Recognizes float valued position indices (PLACE)* - Simulator recognizes float valued position indices for PLACE command. For Example: PLACE 2.0,3.5,SOUTH => 2,3,SOUTH (Floor values are taken into consideration)
> - *Unit Testcases and Integration Testcases* - All the unit testcases and integration testcases are considered and documented along with expected & actual results
>

![Sample Execution](sample_screenshot.png?raw=true "Sample Testcase Screenshot")
