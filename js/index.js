// let text = "i need to reverse this text";
// let words = text.split(" "); // Split the text into words

// for (let i = 0; i < words.length; i++) {
//    // Initialize an empty array to store the reversed characters
//     let rev_word = ""; 
//     let final = [] // Initialize an empty string to store the reversed word
    
//     // Loop through each character of the word in reverse order
//     for (let j = words[i].length - 1; j >= 0; j--) {
//         rev_word += words[i][j];  // Add each character to the reversed word string
        
        
//     }
//     final.push(rev_word)
//     // Add the reversed word to the array
//     console.log(final.join(" "))
  
// }


function findPrime(num) {

    if(num < 1 ){
        return false
    }else{
        for(let i = 2; i<  Math.sqrt(num); i++){
            num % i === 0
            console.log("not prime")
            return false
        }
        console.log("prime")
        return true;
    }
    
}

findPrime(3)
findPrime(6)

let button =  document.getElementById("")
button.addEventListeners('click', ()=>{
    console.log("clicked")
})

element.createElement = "create element";
document.createElement 



