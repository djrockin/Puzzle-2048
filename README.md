# Puzzle-2048
2048 is a well known game developed in 2014 designed by Italian web developer Gabriele Cirulli. In this game, there is a (4,4) grid and each cell has a value in power of 2. Four actions are possible - left, right, up, down. Our aim is to get maximum tile in game 2048 and maximize the score.

We implement the game and wrote a function to get the best next move to take.We have implemented the following strategies till now.

A. Greedy Approach
In this our approach was to take the move with the highest number of merges.But this approach did not give satisfactory results.We were never able to make 2048. Also the average score was around 3000.

B. Greedy Approach with a depth level
In this approach we consider the score gained from each move. But for each move we maintain the highest score that can be obtained by exploring all possible moves till a particular depth. The move with the highest score is selected. Here the average score is around 2125.

C. Heuristic Based Approach with different heuristics weights
It is mainly minimax along with heuristics and domain knowledge. It can be observed that keeping the bigger no near one corner can be helpful in making more merges and score.

The final heuristic of the action is computed by multiplying weight matrix to grid after taking an action and this quantity is subtracted by another heuristic (say h’) in which for each cell difference from neighbours is calculated and total sum is the final value.

Using Heuristic We were able to get to a max score of 133000 and average score of 71000 
