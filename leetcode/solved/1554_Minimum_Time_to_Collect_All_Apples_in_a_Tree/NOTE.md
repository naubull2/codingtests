# Notes on Success
+  observation:
  - In the shortest route, we only traverse an edge twice.
  - If there exists a child node/it-self has apple, then all the nodes in the path needs to be traversed.
    - If there aren't any child node with an apple, we don't go down that path. 

	build adjacency list,
	recursion on node 0,

	pseudo code be like,
	def recursion(node, parent):
			count = 0
			for n in node.neighbor:
					count += recursion(n)
			if count > 0 or node.hasApple:
					count += 2 # visit this node
			return count

> Time : O(E) , Space : O(E)
