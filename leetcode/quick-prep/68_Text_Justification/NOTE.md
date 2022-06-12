# Notes on Success

line buffer
for each w in words
	-> try to assign words in the the buffer, check char <count + number of words - 1>
	
	1. Greedily assign words to the line
	
	for each line:
	2. justify remaining chars in the intervals, evenly distributed
		-> remainder / (#words-1)
			21-14 chars  4words divmod => 4, 2 add [:2]
			ws ['     ', '     ', '    ']
			"w      w      w     w"
		-> INTERTWINE words and spaces
		
	3. for the last line,
		 -> left justify + simply add remaining whitespaces

> Time : O(N) , Space : O(N)
