import os

for filename in os.listdir("."):
    words = filename.split('.')

    # Make sure it does not rename itself
    if words[0] == "remo":
        continue

    # Make sure it hasn't already been renamed
    if len(words) == 2:
        continue

    # Make sure it's a movie
    if words[len(words) - 1] != "mp4" and words[len(words) - 1] != "mkv":
        continue
    else:
        extension = words[len(words) - 1]

    
    year = ""
    yearIndex = 1   # Default = 1

    # Get index of the year in word list
    for word in words:
        if word.isdigit() and int(word) > 1950:
            year = word
            yearIndex = words.index(word)

    
    movie = ""

    # Put together movie name
    for i in range(0,yearIndex):
        movie += words[i] + " "

    newFilename = movie + "(" + year + ")" + "." + extension
    
    os.rename(filename, newFilename)