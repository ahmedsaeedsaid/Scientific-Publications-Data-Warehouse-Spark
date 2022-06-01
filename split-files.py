import os
import argparse
import re


def main():

    stack = []
    countOfObjects = 0
    countFiles = 0
    output =open("dblpv13_" + str(countFiles) + ".json", "w", encoding="utf8")
    with open("dblpv13.json", "r", encoding="utf8") as input:
            while countFiles != 1000:
                    line = input.readline()
                    if not line:
                        break

                    getNumberIntRegex = re.compile(r'NumberInt\(\d+\)')
                    getIntRegex = re.compile(r'\d+')
                    numberInt = getNumberIntRegex.search(line)

                    if numberInt:
                        number = getIntRegex.search(numberInt.group(0))
                        line = re.sub(r"NumberInt\(\d+\)", number.group(0), line)

                    checkOpenBracketRegex = re.compile(r'".*{.*"')
                    checkCloseBracketRegex = re.compile(r'".*}.*"')
                    try:

                        if  '{' in line and not checkOpenBracketRegex.search(line):
                            stack.append('{')

                        if '}' in line and not checkCloseBracketRegex.search(line):
                            stack.pop()
                            if not stack:
                                countOfObjects += 1
                                print('object:',countOfObjects,', file: ',countFiles)

                    except:
                        print(line)
                        break

                    if countOfObjects == 25000:
                        output.write("}]")
                        countFiles += 1
                        output = open("dblpv13_" + str(countFiles) + ".json", "w", encoding="utf8")
                        countOfObjects = 0
                        output.write("[")
                    else:
                        output.write(line)

if __name__ == "__main__":

    main()
