text = "    hello welcome to python training"

new_text = text.upper();

print(text)    
print(new_text)

#title_case
st_in_titlecase = text.title();

#split
st_split = text.split();

print(st_split);

#reversing the string
st_reversed = text[::-1];
print(st_reversed);

#remove spaces from left
text_left = text.lstrip();


# join with "_"

text_joined = "_".join(st_split);
print("text_joined =",text_joined);

# concatination
text_concat = text + " " + new_text;
print("text_concat =",text_concat);

# joining two dynamic values in a string
text_dynamic_values = f"Normal text {text} and joined with _ text {text_joined}"
print("text_dynamic_values =",text_dynamic_values);
