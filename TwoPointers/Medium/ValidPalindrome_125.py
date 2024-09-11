def isPalindrome(s):
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char
        else:
            continue

    cleaned = cleaned.lower()
    cleaned = cleaned.strip()

    start = 0
    end = len(cleaned) - 1

    while start <= end:
        if cleaned[start] != cleaned[end]:
            return False
        else:
            start += 1
            end -= 1

    else:
        return True