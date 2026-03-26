import re  # module for regular expressions

#1 Match 'a' followed by zero or more 'b'

text1 = "abbb a ab abb"

pattern1 = r"ab*"  # 'a' followed by zero or more 'b'
matches1 = re.findall(pattern1, text1)

print("#1:", matches1)


#2 Match 'a' followed by two to three 'b'

text2 = "ab abb abbb abbbb"

pattern2 = r"ab{2,3}"  # 'a' followed by 2 or 3 'b'
matches2 = re.findall(pattern2, text2)

print("#2:", matches2)


#3 Find lowercase words joined with underscore

text3 = "hello_world test_string Hello_World"

pattern3 = r"[a-z]+_[a-z]+"  # lowercase letters separated by underscore
matches3 = re.findall(pattern3, text3)

print("#3:", matches3)


#4 Find uppercase letter followed by lowercase letters

text4 = "Hello World test Python Code"

pattern4 = r"[A-Z][a-z]+"  # one capital letter + lowercase letters
matches4 = re.findall(pattern4, text4)

print("#4:", matches4)


#5 Match 'a' followed by anything ending with 'b'

text5 = "acb a123b ac axxxb"

pattern5 = r"a.*b"  # starts with 'a' and ends with 'b'
matches5 = re.findall(pattern5, text5)

print("#5:", matches5)


#6 Replace space, comma, or dot with colon

text6 = "Hello, world. Python is great"

result6 = re.sub(r"[ ,\.]", ":", text6)  # replace space, comma, dot

print("#6:", result6)


#7 Convert snake_case to camelCase

text7 = "hello_world_example"

def snake_to_camel(match):
    return match.group(1).upper()  # convert letter to uppercase

result7 = re.sub(r"_([a-z])", snake_to_camel, text7)

print("#7:", result7)


#8 Split string at uppercase letters

text8 = "HelloWorldPython"

result8 = re.split(r"(?=[A-Z])", text8)  # split before capital letters

print("#8:", result8)


#9 Insert spaces before capital letters

text9 = "HelloWorldPython"

result9 = re.sub(r"([A-Z])", r" \1", text9).strip()  # add space before capitals

print("#9:", result9)


#10 Convert camelCase to snake_case

text10 = "helloWorldExample"

result10 = re.sub(r"([A-Z])", r"_\1", text10).lower()  # add underscore and lower case

print("#10:", result10)