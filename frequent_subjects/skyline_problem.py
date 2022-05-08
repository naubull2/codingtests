import heapq
# NOTE: min-heap we invert values to negatives to achieve max-heap
# we can implement the above data structure as array, where left, right childs are accessed by 2k+1, 2k+2 (0 indexed arrays)

def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
	"""Easy to understand but O(N**2)"""
	heap = [0] # initially max height is 0
	
	coords = []
	
	for l, r, h in buildings:
		coords.append((l, -h)) # -h represents start of building
		coords.append((r, h)) # +h represents end of building
	
	coords.sort() # sort by x coord followed by y coord (height)
	result = []

	for coord, h in coords:
		prev_max = heap[0] # keep track of prev max to see whether there is any change due to new building's ending or starting
		if h > 0: # if a building ends at this point 
			heap.remove(-h) # we should remove it from heap  O(N)
			heapify(heap)  # O(klogk)
		else:
			heappush(heap, h) # O(logk)

		if prev_max != heap[0]: # if max has changed in heap
			result.append((coord, -heap[0])) # we should add this to result

	return result
	

## The point here is to make sure the heap operation stays O(logN)
def getSkyline(buildings):
	"""Quite complex, but runs fast O(NlogN)"""
	N, hs = len(buildings), []
	for i, (l, r, h) in enumerate(buildings):
		# track i as building number
		hs.append((l, 0, -h, i))
		hs.append((r, 1, h, i))
	hs.sort() 
	alive = [False] * N # check if building is still there
	
	res, heap, current_height = [], [], 0
	for x, tp, h, i in hs: 
		if tp == 0:  # start of i-th building
			heapq.heappush(heap, (h, i))
			alive[i] = True
			if current_height < -h:
				res.append([x, -h])
				current_height = -h
		else:  # end of i-th building
			alive[i] = False
			# remove any buildings that is already done : including current building
			while heap and not alive[heap[0][1]]:
				heapq.heappop(heap)  
			if heap and -heap[0][0] < current_height:
				current_height = -heap[0][0]
				res.append([x, current_height])
			elif not heap:
				current_height = 0 
				res.append([x, current_height])
	return res
			
	
	
		
			
		
