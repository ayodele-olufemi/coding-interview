// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'elppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {
    let result = "";
    for (let i=1; i <= str.length; i++) {
        result += str.charAt(str.length - i);
    }
    return result;
}

module.exports = reverse;
