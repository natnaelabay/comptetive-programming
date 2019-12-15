# Natnael Abay

# se.natnael.abay@gmail.com

class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		ops = ['+','-','*','/']
		ans = []
		for i in tokens:
			if i not in ops:
				ans.append(i)
			else:
				op1 = int(ans.pop())
				op2 = int(ans.pop())
				if i == '+':
					ans.append(op2 + op1)
				if i == '-':
					ans.append(op2 - op1)
				if i == '*':
					ans.append(op2 * op1)
				if i == '/':
					ans.append(int(op2/op1))

		return ans[0]
