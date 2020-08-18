while True:
    print '1. Create a text file \n2. Count vowels, digits and words \n3. Create new file'
    print "OR Enter 0 to exit"
    c = raw_input('Enter choice: ')
    if not c.isdigit() and int(c) not in range(0,4):
        print 'Invalid choice'
        continue
    if c == '0':
        break
    if c == '1':
        print 'Type file contents. After the last line, press enter twice.'
        with open(raw_input('Enter new file name: '), 'w') as file1:
            while True:
                l = raw_input()
                if l:
                    file1.write(l + '\n')
                else:
                    break
        print 'Written to file.'
        continue
    
    elif c == '2':
        w = d = l = 0
        with open(raw_input('Enter file name to read: '), 'r') as file:
            for line in file:
                for word in line.split():
                    w += 1
                    for char in word:
                        if char.isdigit():
                            d += 1
                        elif char.isalpha() and char.lower() in 'aeiou':
                            l += 1
        print 'The file contians', w, 'words,', d, 'digits and', l, 'vowels.'
        continue
    
    elif c == '3':
        file2 = open(raw_input('Enter new file name: '), 'w')
        with open(raw_input('Enter file name to read: '), 'r') as file1:
            for line in file1:
                file2.write(line.replace(' ', '#'))
        file2.close()
        print 'New file written with # in place of spaces'
        continue
