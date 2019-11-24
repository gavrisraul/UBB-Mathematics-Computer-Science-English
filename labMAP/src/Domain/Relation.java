package Domain;

import java.io.Serializable;

public class Relation extends BaseObject implements Serializable {

    public String first;
    public String second;

    public Relation(String csvLine) {
        super(csvLine);
        String[] csvLineData = csvLine.split(",");
        this.first = csvLineData[0];
        this.second = csvLineData[1];
    }

    public Relation(String first, String second) {
        super("Make relation constructor");
        this.first = first;
        this.second = second;
    }

    public String getFirst() {
        return this.first;
    }

    public String getSecond() {
        return this.second;
    }

    public boolean setFirst(String first) {
        this.first = first;
        return true;
    }

    public boolean setSecond(String second) {
        this.second = second;
        return true;
    }

    @Override
    public String toString() {
        return this.first + ", " + this.second;
    }

}
