# バックトラック法でエイトクイーンを解く。

# チェス盤を初期化する。
board = [[False]*8]*8

# クイーンの動きを表す。(x: 行を表す変数。 y: 列を表す変数。)
def check(x, y):

	# 右にクイーンがあるかチェックする。
	for i in range(0, 8):
		if board[i][y] == True:
			return False

	i = x
	j = y

	# 左下にクイーンがあるかチェックする。
	for n in range(i, 0, -1):
		for m in range(j, 0, -1):
			if board[n][m] == True:
				return False

	i = x
	j = y

	# 左上にクイーンがあるかチェックする。
	for n in range(i, 0, -1):
		for m in range(j, 8, 1):
			if board[n][m] == True:
				return False

	return True

# チェス盤を表示する
def showBoard():
	for i in range(0, 8):
		for j in range(0, 8):
			# (i, j)上にクイーンが存在すれば'Q'を表示し、存在しなければ'.'を表示する。
			if board[i][j] == True:
				print 'Q',
			else:
				print '.',
		print ""

# 実際に解く関数 (x: 行を表す変数)
def solve(x):
	# 再帰を用いるため、xが8に達した場合、Trueを返して関数から抜け出す。
	if x == 8:
		return True
	
	# i: 列を表す変数
	for i in range(0, 8):
		# (x, i)が置いてあるクイーンの範囲外である場合
		if check(x, i):
			# (x, i)にクイーンを置く。
			board[x][i] = True
			# 次の行も置くことができれば、Trueを返す。できなければ、(x, i)からクイーンを取り除く。
			if solve(x+1):
				return True
			else:
				board[x][i] = False

	return False

def main():
	# 0行目より開始。
	if solve(0):
		showBoard()

if __name__ == "__main__":
	main()
