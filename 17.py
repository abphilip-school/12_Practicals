c = 0
with open('STORY.TXT', 'r') as file1:
    for line in file1:
        if line[0].lower() != 'a':
            c += 1

print 'Number of lines not starting with A:', c
