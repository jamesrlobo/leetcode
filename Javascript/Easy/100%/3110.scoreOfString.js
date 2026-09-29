//3110. Score of a String
//https://leetcode.com/problems/score-of-a-string/description/
//Beats: 100.00%
/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    n = s.length
    var output = 0
    // console.log(n)
    for(var i=0; i<n-1; i++){
        output = output + (Math.abs(s[i].charCodeAt()-s[i+1].charCodeAt()))
        // console.log("****")
    }
    return output
    };


var s = "hello"
console.log(scoreOfString(s))
