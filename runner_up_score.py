# Challenge: Find the Runner-Up Score!
"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given N scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains N. The second line contains an array A[] of N integers each separated by a space.

Constraints
2 <= N <= 10
-100 <= A[i] <= 100

Output Format
Print the runner-up score.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5

Sample Input 1
4
57 57 -57 57

Sample Output 1
-57

"""


def runner_up():
    n = int(input())
    arr = map(int, input().split(" "))

    winner = arr.__next__()
    runner = arr.__next__()

    if winner < runner:
        winner, runner = runner, winner

    for value in arr:
        if runner == winner > value:
            # in my view, there is no tie
            runner = value

        if runner < winner < value:
            runner = winner
            winner = value

        if runner < value < winner:
            runner = value

    print(runner)
    # print(winner)


if __name__ == '__main__':
    runner_up()
