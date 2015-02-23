# Every business can make use of a good accountant and, if they're not big on following the law, sometimes a bad one. Bad accountants try to make more money for their employers by fudging numbers without getting caught.

# Sometimes a bad accountant wants to make a number larger, and sometimes smaller. It is widely known that tax auditors will fail to notice two digits being swapped in any given number, but any discrepancy more egregious will certainly be caught. It's also painfully obvious when a number has fewer digits than it ought to, so a bad accountant will never swap the first digit of a number with a 0.

# Given a number, how small or large can it be made without being found out?

# Input
# Input begins with an integer T, the number of numbers that need tweaking. Each of the next T lines contains a integer N.

# Output
# For the ith number, print a line containing "Case #i: " followed by the smallest and largest numbers that can be made from the original number N, using at most a single swap and following the rules above.

def find_smallest(numbers):
	smallest_index = 0
	for i in range( len(numbers) ) :
		if numbers[smallest_index] > numbers[i] and	numbers[i] != 0 :
			smallest_index = i
	return smallest_index

def find_greatest(numbers):
	greatest_index = 0
	for i in range( len(numbers) ) :
		if numbers[greatest_index] < numbers[i] :
			greatest_index = i
	return	greatest_index

def swap_digit( numbers_o, index ):
	numbers = list(numbers_o)
	temp = numbers[0]
	numbers[0] = numbers[index]
	numbers[index] = temp
	numbers = [ str(x) for x in numbers ]
	return ''.join(numbers)

if __name__ == "__main__":
	content = open( 'cooking_the_books.txt', 'r' ).readlines()
	n_tests = int(content[0])
	content = [[int(x) for x in row if x.isdigit()] for row in content]

	del content[0]

	for i in range( n_tests ) :
		smallest_index = find_smallest( content[i] )
		greatest_index = find_greatest( content[i] )

		smallest_number = swap_digit( content[i], smallest_index )
		greatest_number = swap_digit( content[i], greatest_index )

		print 'Case #%d: %s %s' % ( i+1, smallest_number, greatest_number )