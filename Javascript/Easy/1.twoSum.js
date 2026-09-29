//1. Two Sum
//https://leetcode.com/problems/two-sum/description/
//Beats: 5.02%
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (i=0; i< nums.length; i++) {
        for (j=0; j<nums.length; j++) {
            if ((i != j) && ((nums[i] + nums[j]) == target)) {
                return [i, j]
            }
        }
    }
}

var nums = [2,7,11,15]
var target = 9
console.log(twoSum(nums, target))
