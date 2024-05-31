def most_frequent(string):
        string = string.lower()
    freq_dict = {}
    for char in string:
        if char.isalpha():  # Consider only alphabetic characters
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    for char, freq in sorted_freq:
        print(f"{char} = {freq:02}")
input_string = "Mississippi"
print("Input :", input_string)
print("Output :")
most_frequent(input_string)
