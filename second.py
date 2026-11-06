statement = "chocolate moulds come in various materials and shapes"

#upper_case
st_in_uppercase = statement.upper();

#lower_case
st_in_lowercase = statement.lower();

#title_case
st_in_titlecase = statement.title();

#split
st_split = statement.split();

st_join = ",".join(st_split);

find_st = statement.find("come");

print(st_in_uppercase);
print(st_in_lowercase);
print(st_in_titlecase);
print(st_split);
print(st_join);
print(find_st);