//2677. Chunk Array
//https://leetcode.com/problems/chunk-array/description/
//Beats: 60.62%
var chunk = function (arr, size) {
    var output = []
    for (let i = 0; i < arr.length; i += size) {
        output.push(arr.slice(i, i + size))
    }
    return output;
};

arr = [1,2,3,4,5]
size = 1
console.log(chunk(arr, size))
