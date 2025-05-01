max_hit = 10
club = max_hit + 10
sword = max_hit + 30

#print("\033[91mThis is red text\033[0m")
#print("\033[92mThis is green text\033[0m")
#print("\033[93mThis is yellow text\033[0m")
#print("\033[94mThis is blue text\033[0m")
#print("\033[1m\033[95mThis is bold magenta text\033[0m")
def get_name():
    with open('savefile.txt', 'r') as f:
        load_list = f.readlines()
        name = load_list[0]
        return name
    