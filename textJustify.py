def fullJustify(words, maxWidth):
    result = []
    numChar, curLine = 0, []
    for w in words:
        if len(w) + numChar + len(curLine) > maxWidth:
            for i in range(maxWidth-numChar):
                curLine[i % (len(curLine)-1 or 1)] += ' '
            result.append(''.join(curLine))
            numChar, curLine = 0, []
        numChar += len(w)
        curLine.append(w)
    result.append(''.join(curLine).ljust(maxWidth))
