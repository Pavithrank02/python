let text = "i need to reverse this text";
let words = text.split(" ")
// console.log(words)
for(i = 0; i < words.length; i++){
    let rev_word = ""
    console.log(words[i])
    for(j= words[i].length - 1; j>=0; j--){
        rev_word += words[i][j] 
    }
    console.log(rev_word)
}