# Day 2: Advent of Code 2023

Today's task to save Christmas required extracting data from rows of text to count the quantities of different colored cubes.

Task 1 required testing to see if the quantity respected set limits for each color. The challenge in this task was how to extract the information from the string efficiently. I found my solution by splitting the example string and examining the different sticking points. As each string had the same format for the beginning, it was easy enough to identify where the first colors/quantities could be found in the list. I then had to adjust the loop to account for the varying list lengths.
I feel like a regex findall will be a better option, but I'm sick today and exhausted from the week so I will come back and try that out another time. Done is better than good for today.

Task 2 required finding the minimum number of each color needed for a game to be possible. With the kinks worked out in task one, this was quite simple. I made empty lists for each color. Then, where my code previously checked whether the quantity of cubes was over the limit, I simply replaced this with an append to add the quantity to the list. All that was left to do was to use max() to get the highest number in the lists and multiply them together as prompted.

Lingering cold aside, it was nice to start my Saturday morning saving Christmas with a fun brainteaser. Thanks, AoC!
