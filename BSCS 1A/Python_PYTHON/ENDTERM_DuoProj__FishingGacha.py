import random

print("--- FishGO: Reel 'em All! ---")

## i call these "flags." these flags are simply keeping track if a thing has happened or not
ben_firstmeet = True
ben_excellent = True ## highest tier rod u did it
default_rod = True

######

## i do these so i can call them in a function below

options = ("LET'S CATCH!", "FISHDEX", "SHOP", "GUIDE", "Exit.")
tutorial = ["Catching", "Fishdex", "Shop", "You", "...Nevermind!"] ## seen later under the INFO menu, case 4

##NOTE: these def functions are NOT important, they're simply showing
def show_options():
    for i in range(len(options)):
        print((i+1), "-", options[i])
def show_tutorial():
    for i in range(len(tutorial)):
        print((i+1), "-", tutorial[i])

######
# let's get into dict territory. why seperate? organization

fishes = {
    "betta" : {
        "name" : "Betta Fish",
        "def" : "Betta (/ˈbɛtə/, BET-tə) is a large genus of small, active, often colorful, freshwater ray-finned fishes, in the gourami family (Osphronemidae).",
        "star1" : "The betta fish can breathe air thanks to a special organ called the labyrinth organ. That’s why they can survive in low-oxygen water—and even gulp air from the surface like tiny aquatic lung-users.",
        "star2" : "Male bettas are famous for their dramatic aggression. Put two together, and they’ll flare their fins, spread their gills, and fight—hence the nickname “Siamese fighting fish.”",
        "star3" : "They build bubble nests. The male blows bubbles at the surface and carefully places eggs inside after mating, then guards them like a very intense single parent.",
        "star4" : "Bettas can actually recognize their owners and learn simple routines, like swimming up when it’s feeding time. Not bad for a fish most people underestimate.",
        "star5" : "they’re a mix of beauty and survival engineering. Flowing, colorful fins that look delicate—but paired with air-breathing ability, territorial instincts, and parental care. It’s like a living contradiction: elegant on the outside, surprisingly tough and strategic underneath.",
    },
    "clown" : {
        "name" : "Clownfish",
        "def" : "Clownfish or anemonefishes (genus Amphiprion) are saltwater fish found in the warm and tropical waters of the Indo-Pacific.",
        "star1" : "Clownfish are basically born male—and some of them switch to female later. In a group, the biggest fish becomes the dominant female, and if she dies, the next biggest male “levels up” and changes sex. Nature really said they can just do that.",
        "star2" : "They live in sea anemones… without getting stung. The trick? A special mucus coating on their skin that makes the anemone think, “yeah, you’re one of me.” It’s like having a biological invisibility cloak.",
        "star3" : "Clownfish are super territorial for their size. Despite being small, they will aggressively defend their anemone from much larger fish—and even divers. Tiny fish, huge attitude.",
        "star4" : "They have a surprisingly organized social hierarchy. It’s basically a strict ranking system: one female at the top, one breeding male, and a bunch of smaller non-breeding males underneath. Step out of line, and you’ll get chased off.",
        "star5" : "Clownfish and sea anemones have a mutual partnership that feels almost strategic. The fish gets protection from predators, while the anemone gets cleaned, fed scraps, and even better water circulation from the clownfish’s movement. It’s not just survival—it’s teamwork so effective it looks like they planned it.",
    },
    "moray" : {
        "name" : "Moray Eel",
        "def" : "Moray eels, or Muraenidae (/ˈmɒreɪ, məˈreɪ/), are a family of eels whose members are found worldwide.",
        "star1" : "The moray eel always looks angry—but that open-and-close mouth motion isn’t aggression. It’s how they breathe, pumping water over their gills while hiding in crevices.",
        "star2" : "They have a second set of jaws called pharyngeal jaws. When they catch prey, those inner jaws shoot forward, grab it, and pull it down their throat—basically an alien-style double bite.",
        "star3" : "Moray eels have poor eyesight but a strong sense of smell, so they rely more on scent than vision when hunting. That’s why they often snap at anything that smells like food—even if they can’t clearly see it.",
        "star4" : "Some species cooperate with other fish while hunting. For example, a moray eel might team up with a grouper—one flushes prey out of rocks, the other catches it. It’s like underwater tag-team strategy.",
        "star5" : "They’re perfectly engineered ambush predators. Long, flexible bodies to snake through coral, mucus-covered skin instead of scales for tight spaces, and that nightmare-level jaw system—all optimized for striking from the shadows with terrifying efficiency."
    },
    "whale" : {
        "name" : "Whale Shark",
        "def" : "The whale shark (Rhincodon typus) is a slow-moving, filter-feeding carpet shark and the largest known extant fish species.",
        "star1" : "The whale shark is the largest fish on Earth, reaching lengths of 12+ meters—about the size of a bus—but it’s completely harmless to humans.",
        "star2" : "Despite its size, it’s a filter feeder. It eats tiny plankton, fish eggs, and small organisms by swimming with its mouth wide open—basically a gentle giant vacuuming the ocean.",
        "star3" : "Each whale shark has a unique pattern of white spots, kind of like a fingerprint. Scientists even use photo databases to identify and track individual sharks over time.",
        "star4" : "They’re incredible travelers. A single whale shark can migrate thousands of kilometers across oceans, following food blooms like plankton and spawning events.",
        "star5" : "Everything about them is built around peaceful dominance. They’re the biggest fish alive, yet they don’t hunt, don’t attack, and don’t need to. They just glide through the ocean, feeding on the tiniest life forms—proving you can be the most powerful presence in the room without being aggressive at all."
    },
    "sun" : {
        "name" : "Sunfish",
        "def" : "The ocean sunfish (Mola mola), also known as the common mola, is one of the largest bony fish in the world. It is the type species of the genus Mola, and one of five extant species in the family Molidae.",
        "star1" : "The heaviest bony fish on Earth—it can weigh over 2,000 kg (that’s heavier than a small car), yet it mostly just drifts around eating soft jellyfish.",
        "star2" : "It looks like a fish that got “cut in half,” and that’s not far off. Instead of a normal tail, it has a weird rounded structure called a clavus, which it wiggles to steer—basically swimming like a giant, living pancake.",
        "star3" : "Sunfish are famous for sunbathing. They’ll float sideways at the surface, which made people think they were sick or dying—but they’re actually warming up after deep, cold dives and sometimes letting birds pick parasites off them. Free spa day.",
        "star4" : "Despite their massive size, they’re pretty defenseless. No real scales, not great swimmers, and lots of predators when they’re young. Their main survival strategy is grow ridiculously big, ridiculously fast.",
        "star5" : "The wildest part is a single female ocean sunfish can produce up to 300 million eggs at once—more than any known vertebrate. It’s like they compensate for being a floating, awkward giant by just overwhelming the ocean with sheer numbers. Quantity over quality."
    }
}
# functions same as the other show_
def show_fish():
    for i, fish in enumerate(fishes.values(), start=1):
        print(i, "-", fish["name"])

# dict for rod portion
rod = {
    "medium":{
        "name" : "Medium Rare Rod",
        "price":50,
        "mod":3,
        "break_until": 10
    },
    "well":{
        "name" : "Well Done Rod",
        "price":100,
        "mod":5,
        "break_until": 15
    },
    "excel":{
        "name" : "Excellent Rod",
        "price":200,
        "mod":10,
        "break_until": 20
    }
}
def show_rod():
    for i, r in enumerate(rod.values(), start=1):
        print(i, "-", r["name"], f"(₱{r['price']})")

def show_star_unlocks(count, fish_name):
    if 1 <= count <= 4:
        print(f"\n{fish_name}: Unlocked {count} STAR! (Check Fishdex!)")
    elif count == 5:
        print(f"\n{fish_name}: Unlocked FINAL STAR! (Check Fishdex!)")
# gotta keep track for star unlocks 
betta_caught = 0
clown_caught = 0
moray_caught = 0
whale_caught = 0
sun_caught = 0

mod = 0

coins = 0

break_count = 0 # rod break mechanic

# this function catches the randomized die and checks what was rolled
## will also be used for checking stars
def check_catch():
    global coins, betta_caught, clown_caught, moray_caught, whale_caught, sun_caught

    if roll_die <= 4:
        # garbage_caught += 1
        print("Caught GARBAGE!")
    elif roll_die >= 5 and roll_die <= 10:
        coin = random.randint(5, 20) # how much coin did we fish out?
        coins += coin # needed so randomized value doesn't clear the current count of coins
        print(f"Caught COINS! (+{coin})")
    elif roll_die >= 11 and roll_die <= 14:
        betta_caught += 1
        print("Caught a BETTA FISH!")

        if betta_caught == 1:
            print("Betta believe it!")

        show_star_unlocks(betta_caught, "BETTA")

    elif roll_die >= 15 and roll_die <= 19:
        clown_caught += 1
        print("Caught a CLOWNFISH!")
        if clown_caught == 1:
            print("No clowning around!")

        show_star_unlocks(clown_caught, "CLOWN")

    elif roll_die >= 20 and roll_die <= 25:
        moray_caught += 1
        print("Caught a MORAY EEL!")
        if moray_caught == 1:
            print("Moray the merrier!")

        show_star_unlocks(moray_caught, "MORAY")

    elif roll_die >= 26 and roll_die <= 29:
        whale_caught += 1
        print("Caught a WHALE SHARK!")
        if whale_caught == 1:
            print("Stop whaling around!")

        show_star_unlocks(whale_caught, "WHALE")

    elif roll_die >= 30:
        sun_caught += 1
        print("Caught a SUNFISH!")
        if sun_caught == 1:
            print("This is off the scales!")

        show_star_unlocks(sun_caught, "SUN")
    else:
        print(":P")

def show_fish_details(fish_key, caught_count): ## this is for fishdex
    fish = fishes[fish_key]

    print("\nNAME:", fish["name"])
    print(fish["def"])

    # loop stars instead of if-chain
    for i in range(1, 6):
        if caught_count >= i:
            print("\n" + fish[f"star{i}"])

while (True):

    print("----> ON THE DOCKS...")
    print("COINS:", coins)
    print("ROD BREAKS:", break_count)
    print()

    show_options()
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            print("\n-- CATCHING... --")
            if not default_rod and break_count <= 0:
                print("OH NO, your rod broke! Go to the shop again?")
                default_rod = True
                continue

            if break_count > 0:
                break_count -= 1

            basic_die = random.randint(1, 20 + mod)
            roll_die = basic_die

            print(f"ROLL: {roll_die}")
            check_catch()
        case 2:
            print("\n-- FISHDEX --")
            print("-> AT THE FISH TANK...")
            while True:
                show_fish()
                print("6 - Return...")
                
                pick_fish = int(input("Choose fish to inspect: "))
                match pick_fish:
                    case 1:
                        show_fish_details("betta", betta_caught)
                    case 2:
                        show_fish_details("clown", clown_caught)
                    case 3:
                        show_fish_details("moray", moray_caught)
                    case 4:
                        show_fish_details("whale", whale_caught)
                    case 5:
                        show_fish_details("sun", sun_caught)
                    case 6:
                        print("\nThanks for checkin'! Gotta reel 'em all!")
                        break
                    case _:
                        print("INPUT CRASHED. Wave again!")
                        continue
        case 3:
            print("\n-- SHOP --")
            while (True):
                # simple ben dialogue. wanted to make it a little alive 
                if ben_firstmeet:
                    print("BEN: Stranger 'round these parts. Nice to meetcha.")
                    print("BEN: 'Fore you move on, remember these rods break. And that's okay. Just come back for more, yeah?")
                    ben_firstmeet = False
                else:
                    print("BEN: Ah, hello. Nice to see ya, buddy.")
                    print("BEN: Break 'em, get more of 'em. That's life.")
                
                # showing all rods available
                show_rod()
                print("4 - Next time...")

                # yay shopkeeping
                shop_choice = int(input("What'll it be?: "))
                ##NOTE all if-else in the cases from now on check if player can afford or not
                match shop_choice:
                    case 1:
                        # medium rare rod
                        if coins >= 50:
                            default_rod = False
                            break_count = rod["medium"]["break_until"]
                            coins -= 50
                            mod = rod["medium"]["mod"]
                            print("BEN:", rod["medium"]["name"],"! Solid choice, buddy. Try it on for size.")
                        else:
                            print("BEN: Oof. Sorry, buddy, can't afford that just yet.")
                        break

                    case 2:
                        # well done rod
                        if coins >= 100:
                            default_rod = False
                            break_count = rod["well"]["break_until"]
                            coins -= 100
                            mod = rod["well"]["mod"]
                            print("BEN:", rod["well"]["name"],"! Ya growin', ain't ya, rookie? Right on.")
                        else:
                            print("BEN: Sorry, buddy. Come back, will ya?")
                        break
                    case 3:
                        # excellent rod
                        ## dialogue check for if player unlocks it for the 1st time, then keeps on buying later
                        if ben_excellent and coins >= 200:
                            default_rod = False
                            break_count = rod["excel"]["break_until"]
                            coins -= 200
                            mod = rod["excel"]["mod"]
                            print("BEN:", rod["excel"]["name"],"... Ya really did it, buddy. Keep on.")
                            ben_excellent = False
                        elif coins >= 200: 
                            default_rod = False
                            break_count = rod["excel"]["break_until"]
                            coins -= 200
                            mod = rod["excel"]["mod"]
                            print(rod["excel"]["name"],"BOUGHT!")
                            print("BEN: Back for more, eh? Reel 'em all.")
                        else:
                            print("BEN: Ah, sorry, buddy. Not that one... Not just yet.")
                        break
                    case 4:
                        # exit option chosen
                        print("\nBEN: Nuthin'? Alright, see ya 'round.")
                        break
                    case _:
                        print("BEN: Eh? 'Fraid I didn't catch that, bud. Say that 'gain?")
        case 4:
            print("\n-- GUIDE --")
            print("-> AT THE HELP DESK...")

            print("\nJOE: Heya! It's Joe. Welcome to the isle of reef.")
            while True:
                print()
                show_tutorial()
                ask_joe = int(input("What would you like to know about?: "))

                match ask_joe:
                    case 1:
                        print("\nJOE: Reel 'em all in FishGO!\nThere are 5 species available for catching: Clownfish, sunfish, moray eel, betta fish. and whale shark.\nSTARS are earned the more of the same species you're catching! For each STAR, you earn a FUN FACT!")
                    case 2:
                        print("\nJOE: Access FUN FACTS and STAR status of the fishies via the FISHDEX menu.\nThere's always fish in the sea, but... You can get them even more SHINY...?")
                    case 3:
                        print("\nJOE: Running low? Head on over to Ben's SHOP for the best rods!\nRemember: RODS BREAK! And that's okay! You can always come back for more.")
                    case 4: 
                        print("\nJOE: Me? Oh, I'm sorry, I'm no one special... Please enjoy the isle!")
                    case 5:
                        print("\nJOE: Thank you for your time. Enjoy the isle!")
                        break
                    case _:
                        print("\nJOE: Ah, sorry. Please repeat that.")
        case 5:
            print("\n-- EXIT --")

            print("PROGRAM ENDED. Catch you on the waves later!")
            break
        case _:
            print("\nINVALID INPUT! Swim another day!")
    print()

