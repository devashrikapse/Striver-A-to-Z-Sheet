def string_palindrome(s, l, r):

    if l >= r:
        return True

    if s[l] != s[r]:
        return False

    return string_palindrome(s, l + 1, r - 1)

s = "wowwow"
print(string_palindrome(s, 0, len(s)-1))