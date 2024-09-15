def compress_string(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    # Adding the last character's count
    compressed.append(s[-1] + str(count))

    compressed_str = ''.join(compressed)

    return compressed_str if len(compressed_str) < len(s) else s


# Test the function
input_string = input("Enter a string to compress: ")
compressed_result = compress_string(input_string)
print("Compressed string:", compressed_result)