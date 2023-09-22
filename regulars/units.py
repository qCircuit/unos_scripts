import re

# Your input text
text = "This is a sample text with 1,250 мл of something and also 1.250 гр of something else."

# Define a regular expression pattern to match numbers with optional comma or dot as the decimal separator, followed by мл or гр
pattern = r'(\d+(?:[\.,]\d+)?)\s*(мл|гр)'

# Use re.findall to find all matches in the text
matches = re.findall(pattern, text)

# Check if any matches were found
if matches:
    for match in matches:
        number, unit = match
        print(f"Number: {number}, Unit: {unit}")
else:
    print("Pattern not found in the text.")