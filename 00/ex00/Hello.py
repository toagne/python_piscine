ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Finland!")
ft_set.remove("tutu!")
ft_set.add("Helsinki!")
ft_dict["Hello"] = "Hive!"

print(ft_list)
print(ft_tuple)
print(sorted(ft_set))
print(ft_dict)