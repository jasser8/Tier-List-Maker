S_TIER = []
A_TIER = []
B_TIER = []
C_TIER = []
D_TIER = []


def write_to_tier_list():
    
    tier_list = open("tierlist.txt", "w")

    tier_list.writelines("\nS TIER: ")
    tier_list.writelines(S_TIER)
    tier_list.writelines("\n")

    tier_list.writelines("\nA TIER: ")
    tier_list.writelines(A_TIER)
    tier_list.writelines("\n")

    tier_list.writelines("\nB TIER: ")
    tier_list.writelines(B_TIER)
    tier_list.writelines("\n")

    tier_list.writelines("\nC TIER: ")
    tier_list.writelines(C_TIER)
    tier_list.writelines("\n")

    tier_list.writelines("\nD TIER: ")
    tier_list.writelines(D_TIER)
    tier_list.writelines("\n")

    tier_list.close()


def make_tier_list():
    
    while True:
        choice = str(input("Would you like to add to the tier list? ")).lower()

        if "yes" in choice:
            item = str(input("Type what you would like to tier: "))
            choice_tier = str(input(f"What tier would you like to add {item} to? ")).lower()

            if "s" in choice_tier:
                S_TIER.append(item)
                print(f"Adding {item} to S tier...\n")

            elif "a" in choice_tier:
                A_TIER.append(item)
                print(f"Adding {item} to A tier...\n")

            elif "b" in choice_tier:
                B_TIER.append(item)
                print(f"Adding {item} to B tier...\n")

            elif "c" in choice_tier:
                C_TIER.append(item)
                print(f"Adding {item} to C tier...\n")

            elif "d" in choice_tier:
                D_TIER.append(item)
                print(f"Adding {item} to D tier...\n")

            else:
                print("Not a valid tier, the tiers are: S, A, B, C, and D.\n")        
        
        else:
            print("Creating tier list...")
            write_to_tier_list()
            print("Tier list created!")
            break


make_tier_list()
