package main

func merge(nums1 []int, n int, nums2 []int, n int){
   i := m-1
   j := n-1
   for(var k=m+n-1;k>=0;k--){
       if j<0 || i>=0 && (nums1[k] > nums2[k]{
           nums1[k] = nums1[i]
           i --
       }else{
           nums1[k] = nums2[j]
           j --
       }
   }

}
