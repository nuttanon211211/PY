n = int(input())
b = [int(e) for e in raw_input().split()]

board = [0] * len(b)
board[:2] = b[:2]

for i in range(2,len(b)):
	board[i] = max(board[i-1],max(board[:i-1])+ b[i])
print(board[-1])
