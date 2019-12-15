# Natnael Abay

# se.natnael.abay@gmail.com

class Solution:
	def hIndex(self, citations: List[int]) -> int:
		ans =0
		citations=sorted(citations,reverse=True)
		for i in range(len(citations)):
			if citations[i]>=i+1:
				ans =i+1
		return ans
