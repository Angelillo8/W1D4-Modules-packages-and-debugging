
def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, snack):
    if snack in person["favourites"]["snacks"]:
        return True
    else:
        return False
    
def add_friend(person, new_friend):
    person["friends"].append(new_friend)
    return len(person["friends"])

def remove_friend(person, no_longer_a_friend):
    person["friends"].remove(no_longer_a_friend)
    return len(person["friends"])

def total_money(people_list):
    total_money = 0
    for person in people_list:
        total_money += person["monies"]
    return total_money

def lend_money(lender, receiver, money_lent):
    lender["monies"] -= money_lent
    receiver["monies"] += money_lent
    return lender, receiver

def all_favourite_foods(people_list):
    all_favourite_snacks = []
    for person in people_list:
          for snack in person["favourites"]["snacks"]:
              all_favourite_snacks.append(snack)
    return all_favourite_snacks

def find_no_friends(people_list):
    people_with_no_friends = []
    for person in people_list:
        if len(person["friends"]) == 0:
            people_with_no_friends.append(person)
    return people_with_no_friends

def unique_favourite_tv_shows(people_list):
    unique_tv_shows = []
    for person in people_list:
        if person["favourites"]["tv_show"] not in unique_tv_shows:
            unique_tv_shows.append(person["favourites"]["tv_show"])
    return unique_tv_shows

def unique_favourite_tv_shows_by_set(people_list):
    unique_tv_shows = []
    for person in people_list:
        unique_tv_shows.append(person["favourites"]["tv_show"])
    unique_tv_shows = sorted(list(set(unique_tv_shows)))
    return unique_tv_shows