# Day 1: Advent of Code 2023

Today's task involved extracting coordinates from a data source.
In challenge one, we had to extract the first and last digit from each line of text, concatenate them as strings ( ex: 1 + 2 = 12) and then calculate the sum of all the lines.
In challenge two, we had to do the same task only this time some numbers were written out as words. For example, in '41pqdmfvptwo' the first digit is 4 and the last digit is 2 so the value to add to the total is 42.

I enjoyed this task as a good review of some basic Python. The second task was of course more challenging and my first attempt was an impressively long lock of spaghetti code. I was able to refactor it by adding variables to store the values of the first and last number as the loops progressed and only changing the words to digits at the end, if necessary.
