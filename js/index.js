let text = "malayalam";
let isPalindrome = true;  // Assume it's a palindrome initially

// Loop to check if the string is a palindrome
for (let i = 0; i < text.length / 2; i++) {
    console.log(i)
    if (text[i] !== text[text.length - 1 - i]) {
        isPalindrome = false;  // If any characters don't match, it's not a palindrome
        break;  // Exit the loop early since we've already determined it's not a palindrome
    }
}

// Output the result
if (isPalindrome) {
    console.log("palindrome");
} else {
    console.log("not palindrome");
}
