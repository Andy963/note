# 主体思路，两个索引，对应的数哪个小放哪个
# 细节：注意边界问题
# 注意python range 左开右闭不管是倒序还是正序都是左开右闭

def merge(nums1:list, m:int, nums2:list,n:int):
    i,j = m-1,n-1
    for k in range(m+n-1,-1,-1):
        # j 到头了就放i
        # i 未到头
        if j <0 or (i >= 0 and nums1[i] >= nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
