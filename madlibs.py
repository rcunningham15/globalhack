while(1==1):
    print("""
    Welcome to Madlibs!""")
    adj1 = raw_input("Adjective: ")
    adj2 = raw_input("Adjective: ")
    n1 = raw_input("Noun: ")
    n2 = raw_input("Noun: ")
    pn1 = raw_input("Plural noun: ")
    game1 = raw_input("Game: ")
    pn2 = raw_input("Plural noun: ")
    ing1 = raw_input("Verb ending in 'ing': ")
    ing2 = raw_input("Verb ending in 'ing': ")
    pn3 = raw_input("Plural noun: ")
    ing3 = raw_input("Verb ending in 'ing': ")
    n3 = raw_input("Noun: ")
    plant1 = raw_input("Plant: ")
    bpart1 = raw_input("Body part: ")
    place1 = raw_input("Place: ")
    ing4 = raw_input("Verb ending in 'ing': ")
    adj3 = raw_input("Adjective: ")
    num1 = raw_input("Number: ")
    pn4 = raw_input("Plural noun: ")
    
    madlibs = ("""A vacation is when you take a trip to some %s place
    with your %s family. Usually you go to some place
    that is near a/an %s or up on a/an %s.
    A good vacation place is one where you can ride %s
    or play %s or go hunting for %s. I like
    to spend my time %s or %s.
    When parents go on a vacation, they spend their time eating
    three %s a day, and fathers play golf, and mothers
    sit around %s. Last summer, my little brother
    fell in a/an %s and got poison %s all
    over his %s. My family is going to go to (the)
    %s, and I will practice %s. Parents
    need vacations more than kids because parents are always very
    %s and because they have to work %s
    hours every day all year making enough %s to pay
    for the vacation.""")
    
    print(madlibs %(adj1,adj2,n1,n2,pn1,game1,pn2,ing1,ing2,pn3,ing3,n3,plant1,bpart1,place1,ing4,adj3,num1,pn4))
    