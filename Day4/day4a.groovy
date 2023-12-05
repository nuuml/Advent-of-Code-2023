import java.io.BufferedReader;
import java.io.FileReader;

def br = new BufferedReader(new FileReader("day4.txt"));

def parseLine(line) {
    println(line)
    left = line.split('\\|')[0]
    right = line.split('\\|')[1].split(' ').findAll { it != "" }
    winners = left.split(":")[1].split(" ").findAll { it != "" }
    if ("" in right){
        println("Null in winners")
    }
    score = 0
    println(winners)
    println(right)
    print("Matches : ")
    for (winner in winners){
        if (winner in right){
            print(winner.trim())
            print(" ")
            if (score == 0){
                score = 1
            } else {
                score *= 2
            }
        }
    }
    println()
    print("Score   : ")
    println(score)
    return score
}
line = br.readLine()
sum = 0
while (line != null) {
    sum += parseLine(line)
    line = br.readLine()
}
println(sum)