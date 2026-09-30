//2942. Find Words Containing Character
//https://leetcode.com/problems/find-words-containing-character/
//Beats: 83.77%
var findWordsContaining = function(words, x) {
  const output = []
  for (i=0; i< words.length; i++) {
    if (words[i].includes(x)){
      output.push(i)
    }
  }
return output
};


words = ["leet","code"]
x = "e"
console.log(findWordsContaining(words, x));
