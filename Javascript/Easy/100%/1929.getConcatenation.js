//1929. Concatenation of Array
//https://leetcode.com/problems/concatenation-of-array/description/
//Beats: 100.00%
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    return nums.concat(nums)
};

var nums = [1,2,1]
console.log(getConcatenation(nums))
