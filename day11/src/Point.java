public class Point {
    public long x;
    public long y;

    public Point(long x, long y) {
        this.x = x;
        this.y = y;
    }    
    public Point add(Point delta) {
        return new Point(x + delta.x, y + delta.y);
    }

    public long manhattan(Point p) {
        return Point.manhattan(this, p);
    }

    public static long manhattan(Point a, Point b) {
        return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    }

    @Override
    public String toString()
    {
        return "[" + this.x + ", " + this.y + "]";
    }
}
