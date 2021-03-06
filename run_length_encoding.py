#QUESTION:
# This is an interview question asked by Amazon.
# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
# repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" 
# would be encoded as "4A3B2C1D2A". Implement run-length encoding and decoding. You can assume the 
# string to be encoded have no digits and consists solely of alphabetic characters. You can assume the
# string to be decoded is valid.

def encode(s):
    chars = [s[0]]
    numbers = [0]
    for item in s:
        if item != chars[-1]:
            chars.append(item)
            numbers.append(1)
        else:
            numbers[-1] += 1
    return "".join([str(i)+j for i,j in zip(numbers,chars)])
def decode(s):
    result = ""
    count = 0
    for i in s:
        if i.isdigit():
            count = count*10 + int(i)
        else:
            result += count * i
            count = 0
    return result