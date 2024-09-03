my_shop_list=["bread","milk","butter"]
print(my_shop_list[0])
print(len(my_shop_list))


def bring_more_food(my_shop_list):
    my_shop_list.append("cheese")
    return my_shop_list

l=bring_more_food(my_shop_list)

print(l)