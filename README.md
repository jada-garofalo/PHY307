## PHY307 Projects
A collection of projects from my undergraduate computational physics course at Syracuse University (PHY307), taught by Prof. Walter Freeman.
This work was completed independently, apart from some help debugging my programs from Prof. Freeman.

---
### 1. Project 1 - Defining Functions

The first project of the course started on the bare basics of defining and running functions, namely a Celsius and Fahrenheit converter.

---
### 2. Project 2 - Using Loops

For this project, we had to learn and utilize loops in a few scenarios.

First we had to create a loop to calculate and print the summation of integers over a set range. This involved keeping a running sum as the loop iterated over the specified range.
Next we had to create a loop to calculate the Gaussian integral through numeric integration, summing bits of area with a designated step-size and range.
Then we had to create a loop to count the number of prime numbers that occur before a given integer. This involved a running sum as the program scanned each relevant integer, specified by our given integer.

---
### 3. Project 3 - Generalized Numeric Integration

Using what we learned in the first two projects, we were tasked with creating a numeric integration program, which would sum over a set range and use input functions for Right Riemann, Left Riemann, midpoint, and trapezoidal sums.

---
### 4. Project 4 - Differential Equations

This project consisted of two parts.

For the first part, we were asked to write code to compute Newton's temperature cooling differential equation. Using this function, we then ran it using two different numerical differential equation methods: Euler's method and the second-order Runge-Kutta (RK2) method. We then set up these programs to give us error analysis so that we could graphically represent the difference in accuracy between first-order and second-order algorithms.
For the second part, we edited our RK2 code to cut off after a specific amount of cooling had been achieved. We had to make sure to incorporate an additional bit at the end to maintain second-order accuracy, by predicting what the next segment of time would approximately be.

---
### 5. Project 5 - Animating and Analyzing Pendulums

For this project, we first had to write code to portray a pendulum swinging on a massless string. This code then had its outputs read into Prof. Walter Freeman's custom animation code "anim" through the terminal outputs.
Next, we adjusted our code to compute the period of our pendulum. This allowed us to then display the difference between the theoretical and computational values for the period so that we could analyze our model's accuracy.

---
### 6. Projects 6 and 7 - Simulating Orbits

For this project, we spent a lot of time building up the principle of orbits.

To start, we developed code that would keep track of a planetary body orbiting one stationary star. This would then feed into the anim program to give us an output we could analyze. Included in this output was a running display of the kinetic and potential energies in the system.
We then expanded this code to analyze a binary star system, where both bodies were moving. In order to do this, we used the concept of arrays to store information in three dimensions in a more convenient and concise way.
This was then extrapolated to a ternary star system to show the power of arrays and display how unstable these systems are.

---
### Project 8 - Simulating a Vibrating String

In the final project for this course, we were asked to simulate a vibrating string in two dimensions as a series of masses connected by springs.

To do this, first we generated arrays to contain the position and velocity vectors for all of our masses. From this, we could easily make them move and display their locations in anim using similar principles to the stellar orbits. From this, we then played around with various start conditions (one displaced mass, a sinusoidal wave, and a Gaussian distribution) to see how the model behaved. We also incorporated code to track the period of oscillation of the sinusoidal start condition.
