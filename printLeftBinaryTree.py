from collections import deque


# A class to store a binary tree node
class Node:
	def __init__(self, key=None, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right


# Iterative function to print the left view of a given binary tree
def leftView(root):

	# return if the tree is empty
	if root is None:
		return

	# create an empty queue and enqueue the root node
	queue = deque()
	queue.append(root)

	# loop till queue is empty
	while queue:

		# calculate the total number of nodes at the current level
		size = len(queue) #0
		i = 0

		# process every node of the current level and enqueue their
		# non-empty left and right child
		while i < size:
			# pointer to store the current node
			curr = queue.popleft()
			i = i + 1

			# if this is the first node of the current level, print it
			if i == 1:
				print(curr.key, end=' ')

			if curr.left:
				queue.append(curr.left)

			if curr.right:
				queue.append(curr.right)


if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.right = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(6)
	root.right.left.left = Node(7)
	root.right.left.right = Node(8)
                #        1
                #   2          3 
                #      4    5    6
                #         7   8
	leftView(root)
