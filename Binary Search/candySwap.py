class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        al_tot = sum(aliceSizes)
        bob_tot = sum(bobSizes)

        toSwap = (al_tot + bob_tot) // 2
        for 





sol = Solution()
result = sol.fairCandySwap([2], [1,3])
print(result)