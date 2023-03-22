# sistema-de-coordenadas
## Cartesian Coordinates Translator

### Project main goal
The purpose of this project is to develop a program that can translate the origin of Cartesian coordinates and the quadrants.
The program reads the translated origin (X, Y) of the Cartesian coordinate system and a determined number of points.
For each point, the program informs which quadrant the point belongs to and how many points are in each quadrant.
The program also prints the following information at the end of processing individual points:
  * The point closest to the translated origin and its Euclidean distance.
  * The point farthest from the translated origin and its Euclidean distance.
  * The number of points in each quadrant (the points on the translated abscissa or translated ordinate are not counted).
After printing the information above, the program asks the user to input the origin coordinate (point A) and how long the robot will move for.
With this data, the program prints the final coordinate of the robot on the Cartesian plane.
The Cartesian plane has the origin (0, 0).

After this, the program requests a pair of coordinates (x, y) and a time (expressed in seconds) during which the 'robot will walk' through the Cartesian plane.
The answer will be the final point that the robot reaches, considering that it moves 1 unit up and 2 units to the right (each movement requires 1 second).

### Demo
Inputs and outputs:

![image](https://user-images.githubusercontent.com/87617614/227059376-ed4857ac-a17f-4cd1-93d6-6ef1942a0298.png)

Graphical representation for the previous inputs/outputs(the program does not display these images):

![image](https://user-images.githubusercontent.com/87617614/227059183-f350285f-0935-4071-a8c2-1ee0e9acb482.png)


![image](https://user-images.githubusercontent.com/87617614/227058013-013ffd5f-79f1-4258-b517-44a21ddf12b0.png)

### Installation
To install the program, follow these steps:
  1. Clone the repository to your local machine.
  2. Open the command prompt or terminal and navigate to the project directory.
  3. Run the program with the command python cartesian_coordinates.py.
  4. Follow the prompts to input the necessary data.
 
### Contributors
  * ImGabreuw: programmer.
  * AntonioFC82: README.md file writer.

