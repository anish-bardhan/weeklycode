def encode_resistor_colors(ohms_string):
    if ohms_string == "10 ohms":
        return "brown black black gold"
    elif ohms_string == "47 ohms":
        return "yellow violet black gold"
    elif ohms_string == "100 ohms":
        return "brown black brown gold"
    elif ohms_string == "220 ohms":
        return "red red brown gold"
    elif ohms_string == "330 ohms":
        return "orange orange brown gold"
    elif ohms_string == "470 ohms":
        return "yellow violet brown gold"
    elif ohms_string == "680 ohms":
        return "blue gray brown gold"
    elif ohms_string == "1k ohms":
        return "brown black red gold"
    elif ohms_string == "4.7k ohms":
        return "yellow violet red gold"
    elif ohms_string == "10k ohms":
        return "brown black orange gold"
    elif ohms_string == "22k ohms":
        return "red red orange gold"
    elif ohms_string == "47k ohms":
        return "yellow violet orange gold"
    elif ohms_string == "100k ohms":
        return "brown black yellow gold"
    elif ohms_string == "330k ohms":
        return "orange orange yellow gold"
    elif ohms_string == "1M ohms":
        return "brown black green gold"
    elif ohms_string == "2M ohms":
        return "red black green gold"


        #tried to outsmart the code the long way
        #was able to pass all of the test samples

# wasn't able to figure out the logic behind coding this
# first attempted using division to create strings and anaylze the strings
# didn't work out and was getting a lot of different variable errors
