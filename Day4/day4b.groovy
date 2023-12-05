import java.io.BufferedReader
import java.io.FileReader

def br = new BufferedReader(new FileReader("day4.txt"))

def parseLine(line) {
    println(line)
    left = line.split('\\|')[0]
    right = line.split('\\|')[1].split(' ').findAll { it != "" }
    winners = left.split(":")[1].split(" ").findAll { it != "" }
    score = 0
    for (winner in winners) {
        if (winner in right) {
            print(winner.trim())
            print(" ")
            score ++
        }
    }
    return score
}

def sum = 0
def currentLine = 1
def cardCount = (1..202).collectEntries { key -> [key, 1] }
println(cardCount)
def line = br.readLine()
while (line != null) {
    def innerCount = 0
        def numToAdd = parseLine(line)
        println("Card ${currentLine} scored ${numToAdd}")
        if (numToAdd > 0){
        for (x in (currentLine + 1)..(currentLine + numToAdd)) {
            cardCount[x] += cardCount[currentLine]
        }
        }
    
    currentLine++
    line = br.readLine()
}

br.close()

def totalSum = cardCount.values().sum()
println(totalSum)
