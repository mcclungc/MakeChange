#!/usr/bin/env python3 
#Connie McClung 
#CS325 Spring 2018
#Homework 3 - Question 5: Making Change implementation


# implement making change algorithm
def makeChange(V, A): #V is array of denominations, A is amount
	S=[0]*(A+1) 	#create a helper array to hold last coin used to make minimum change for each amount 1 to A
	# idea for a helper array came from http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
	m = -1 			#initialize m for minimum coins used
	n = len(V) 		# n is upper boundary when looping through V
	#print("Length of array V is: " + str(n))
	#print("Array V contents: ",V)
	C = [] 			#initialize an array to hold minimum coins to make change for each amount 1 to A
	C.append(0); 	# base case - if you have 0 cent, you need 0 coins to make change
	for i in range(1, A+1): 	# initalize remaining values in C to infinity to ensure min is properly calculated
		C.append(float("inf"))
	for i in range(A+1): 		# for every amount from 1 to A
		denomination = 1 
		for j in range( n): 	# loop through V
			if V[j] <= i: 		# if denomination at j is less than amount i
				if C[i] > C[i-V[j]]+ 1: # get the new minimum
					C[i] = C[i-V[j]]+ 1
					denomination = V[j] 
		S[i]=denomination 		# this is the final coin used to make minimum change for amount i
		#print("S[i] is ", S[i])
	m = C[A] 					# this is the minimum coins needed to make change for A
	sequence = [] 				# create an array to hold change results for A
	for k in range(1,len(V)+1):
		sequence.append(0) 		# initialize all values in change result array to 0
	while A > 0:
		currentCoin = S[A] 		# start with last coin used to make minimum change
		for k in range(0,len(V)): 
			if V[k] == currentCoin:
				sequence[k] += 1
		A = A - currentCoin
	#print(S)
	#print(C)
	return m,sequence


def main():
	with open("change.txt", "w+") as outputFile: 		#open output file for write
		with open("amount.txt", "r") as inputFile: 		#open input file for read
			# read each line into a list, sort, and write list to output file
			for line in inputFile:
				# read 2 lines into list
				Vlist = [int(i) for i in line.split()] 	# first line is array V
				nextline = next(inputFile)
				A = int(nextline) 		# second line is A
				# call makeChange function
				m,sequence = makeChange(Vlist,A)
				# write output file with newlines as neneded
				for v in Vlist: 			# first write denomination array
					outputFile.write(str(v))
					outputFile.write(" ")	#space between numbers
				outputFile.write("\n")
				outputFile.write(str(A)) 	# then write amount
				outputFile.write("\n")
				for s in sequence:			# then write change result array
					outputFile.write(str(s))
					outputFile.write(" ")	#space between numbers
				outputFile.write("\n")
				outputFile.write(str(m))	# then write minimum coins needed
				outputFile.write("\n")

# call the main() function to begin the program
if __name__ == '__main__':
    main()

