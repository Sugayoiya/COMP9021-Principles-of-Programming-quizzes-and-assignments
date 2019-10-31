Solving a **sudoku puzzle** is a very common assignment; it is not difficult and moderately interesting as a “solution” (the completed grid) tells nothing about how the solution was reached. More interesting solvers are logical in the sense that they (possibly partially only) solve the puzzle in steps and at every step, explain how they made some progress; they do so by using some of the well known techniques that most people who solve sudoku puzzles apply. Two remarks are in order.


* Methods that only discover digits in empty cells are fairly limited; most methods need to keep track of the list of possible digits that can go into a given cell, and making progress might mean reducing that list. To apply techniques of the second kind, it is necessary to first mark the grid.

* Often, it is not possible to completely solve a puzzle using exclusively the chosen methods; at some point no progress can be made and then a random guess has to be made to either put a digit into a given empty cell, or to remove a digit from the list of possible digits that can go into a given cell. It might subsequently be necessary to backtrack and make alternative guesses if the earlier guesses turn out to be inconsistent with a solution.

You will design and implement a program that will read a sudoku grid whose representation is stored in a file filename.txt and create a Sudoku object, with a number of methods:

* a method preassess() that prints out to standard output whether the representation is correct and has no digit that occurs twice on the same row, on the same column or in the same box;

* a method bare_tex_output() that outputs some Latex code to a file, filename_bare.tex, that can be compiled by pdflatex to produce a pictorial representation of the grid;

* a method forced_tex_output() that outputs some Latex code to a file, filename_forced.tex, that can be compiled by pdflatex to produce a pictorial representation of the grid to which the forced digits technique has been applied;

* a method marked_tex_output() that outputs some Latex code to a file, filename_marked.tex, that can be compiled by pdflatex to produce a pictorial representation of the grid to which the forced digits technique has been applied and that has been marked;

* a method worked_tex_output() that outputs some Latex code to a file, filename_worked.tex, that can be compiled by pdflatex to produce a pictorial representation of the grid to which the forced digits technique has been applied, that has been marked, and to which the preemptive set technique has been applied.

##### file structure:
>sudoku.py
>>  main program
>sudoku_\*.txt
>>  sudoku file
>sudoku_\*_bare.tex
>>  sudoku_\*_bare.tex that can be given as argument to pdflatex to produce a file named sudoku_3_bare.pdf that views as follows.
![alt ass1_1](https://github.com/mokomokoo/COMP9021-Principles-of-Programming-quizzes-and-assignments/blob/master/assignments/Assignment_1/1.png)
>sudoku_\*_marked.tex
>>   sudoku_\*_marked.tex that can be given as argument to pdflatex to produce a file named sudoku_3_marked.pdf that views as follows.
![alt ass1_1](https://github.com/mokomokoo/COMP9021-Principles-of-Programming-quizzes-and-assignments/blob/master/assignments/Assignment_1/1.png)
>sudoku_\*_forced.tex
>>  sudoku_\*_forced.tex that can be given as argument to pdflatex to produce a file named sudoku_3_forced.pdf that views as follows.
![alt ass1_1](https://github.com/mokomokoo/COMP9021-Principles-of-Programming-quizzes-and-assignments/blob/master/assignments/Assignment_1/1.png)
>sudoku_\*_worked.tex
>>   sudoku_\*_worked.tex that can be given as argument to pdflatex to produce a file named sudoku_3_worked.pdf that views as follows.
![alt ass1_1](https://github.com/mokomokoo/COMP9021-Principles-of-Programming-quizzes-and-assignments/blob/master/assignments/Assignment_1/1.png)
