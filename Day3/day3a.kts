fun readFile(name: String) = object {}::class.java.classLoader.getResource(name)!!.readText().trimEnd()

fun readFileAsLines(name: String) = readFile(name).lines()

data class Point2D(val x: Int, val y: Int)

class Grid<T>(private val points: Map<Point2D, T>) : Map<Point2D, T> by points {
    private val highestX = points.keys.maxOf { it.x }
    private val highestY = points.keys.maxOf { it.y }

    override fun toString() = buildString {
        for (y in 0..highestY) {
            for (x in 0..highestX) {
                append(points[Point2D(x, y)])
            }
            if (y < highestY) appendLine()
        }
    }
}

infix fun IntRange.overlapsWith(other: IntRange) =
    this.intersect(other).isNotEmpty()

fun List<Int>.product() = reduce(Int::times)

val grid: Map<Point2D, String> = buildMap {
    val lines = readFileAsLines("day3.txt")
    for (y in lines.indices) {
        val sb = StringBuilder()
        for (x in lines[0].indices) {
            val c = lines[y][x]
            if (!c.isDigit() && sb.isNotEmpty()) {
                put(Point2D(x - sb.length, y), sb.toString())
                sb.clear()
            }
            if (c.isDigit()) {
                sb.append(c)
            } else if (c != '.') {
                put(Point2D(x, y), c.toString())
            }
            if (x == lines.indices.last && sb.isNotEmpty()) {
                put(Point2D(x - sb.length + 1, y), sb.toString())
                sb.clear()
            }
        }
    }
}

val part1Result = grid
    .filterValues { it.isNumeric() }
    .filterKeys { key -> grid.getSurroundingCoordinates(key).values.any { !it.isNumeric() } }
    .values
    .sumOf { it.toInt() }



println("$part1Result")


private fun String.isNumeric() = toIntOrNull() != null

private fun Map<Point2D, String>.getSurroundingCoordinates(point2D: Point2D): Map<Point2D, String> {
    val xRange = (point2D.x - 1)..(point2D.x + this[point2D]!!.length)
    val yRange = (point2D.y - 1)..(point2D.y + 1)
    return filter { it.getXRange() overlapsWith xRange && it.key.y in yRange }
}

private fun Map.Entry<Point2D, String>.getXRange() =
    if (!value.isNumeric()) key.x..key.x
    else key.x until (key.x + value.length)
