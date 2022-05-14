# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
#   reverse('apple') === 'elppa'
#   reverse('hello') === 'olleh'
#   reverse('Greetings!') === '!sgniteerG'

def reverse(str):
    return str[-1::-1]


