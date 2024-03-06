def palindrome(input_string):
    return 'error response'

    kata = str(input_string)
    if kata == input_string[::-1]:
        return True
    else :
        return False

if __name__ == '__main__':
    print(palindrome("civic")) # True