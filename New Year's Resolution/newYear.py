#Alex's New Year's resolution for 2015 is to eat healthier foods. He's done some research and has found out that calories come from three main sources, called macronutrients: protein, carbohydrates, and fat. Alex wants to get the right balance of protein, carbohydrates, and fat to have a balanced diet. For each available food, Alex can only choose to eat it or not eat it. He can't eat a certain food more than once, and he can't eat a fractional amount of a food.

# Input
# Input begins with an integer T, the number of test cases. For each test case, the first line consists of three space-separated integers: GP, GC, and GF, which represent the amount of protein, carbohydrates, and fat that Alex wants to eat. The next line has the number of foods for that test case, an integer N. The next N lines each consist of three space-separated integers: P, C, and F, which represent the amount of protein, carbohydrates, and fat in that food, respectively.

# Output
# For each test case i, print a line containing "Case #i: " followed by either "yes" if it is possible for Alex to eat the exact amount of each macronutrient, or "no" if it is not possible.

def subset_sum( numbers, target, partial=[] ) :
    s = [0, 0, 0]
    for i in range( len( partial ) ) :
        s[0] += partial[i][0]
        s[1] += partial[i][1]
        s[2] += partial[i][2]

    if s == target: return True
    if s > target: return False

    # we didn't reach the target  yet
    for i in range( len( numbers ) ) :
        remaining = numbers[i+1:]
        result = subset_sum( remaining, target, partial + [ numbers[i] ] )

        if result : return result

if __name__ == "__main__" :
    content = [row.split(' ') for row in open( 'new_years_resolution.txt', 'r' ).readlines()]
    content = [[int(x) for x in row] for row in content]

    number_tests = content[0][0]
    del content[0]

    for i in range( number_tests ) :
        desire = content[0]
        choices = content[1][0]
        dishes = content[2:2+choices]

        result = subset_sum( dishes, desire, [] )

        if result == None : print 'Case #%s: no' % (i+1)
        else : print 'Case #%s: yes' % (i+1)

        content = content[2+choices:] # the test cases remaining