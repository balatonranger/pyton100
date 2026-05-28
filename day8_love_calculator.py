def calculate_love_score(name1, name2):
    # Combine names and convert to lowercase
    combined = (name1 + name2).lower()
    
    # Count TRUE letters
    t = combined.count("t")
    r = combined.count("r")
    u = combined.count("u")
    e = combined.count("e")
    true_total = t + r + u + e
    
    # Count LOVE letters
    l = combined.count("l")
    o = combined.count("o")
    v = combined.count("v")
    e2 = combined.count("e")  # count E again for LOVE
    love_total = l + o + v + e2
    
    # Create love score
    love_score = int(str(true_total) + str(love_total))
    
    print(love_score)
    return love_score

# Test the function
calculate_love_score("Kanye West", "Kim Kardashian")
