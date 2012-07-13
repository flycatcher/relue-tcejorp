/**
 * Copyright (C) 2012, Jun Mei
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package nevralia;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;

public class PrizeNode {
    private LinkedList<Attendance> records_;
    private int tardiness_;

    public PrizeNode() {
    }

    public PrizeNode(Attendance a) {
        records_ = new LinkedList<>();
        records_.push(a);
        tardiness_ = (a == Attendance.Late) ? 1 : 0;
    }

    public LinkedList<Attendance> getRecords() {
        return records_;
    }

    public void setRecords(LinkedList<Attendance> r) {
        this.records_ = r;
    }

    public int getTardiness() {
        return tardiness_;
    }

    public void setTardiness(int x) {
        this.tardiness_ = x;
    }

    public Collection<PrizeNode> getSuccessors() {
        Collection<PrizeNode> result = new ArrayList<>();
        if (this.getTardiness() == 0) {
            PrizeNode c = new PrizeNode();
            @SuppressWarnings("unchecked")
            LinkedList<Attendance> a = (LinkedList<Attendance>) this.records_
                .clone();
            if (a.size() >= 2) {
                a.poll();
            }
            a.offer(Attendance.Late);
            c.setRecords(a);
            c.setTardiness(1);
            result.add(c);
        }

        {
            PrizeNode c = new PrizeNode();
            @SuppressWarnings("unchecked")
            LinkedList<Attendance> a = (LinkedList<Attendance>) this.records_
                .clone();
            if (a.size() >= 2) {
                a.poll();
            }
            a.offer(Attendance.OnTime);
            c.setRecords(a);
            c.setTardiness(this.tardiness_);
            result.add(c);
        }

        boolean isAbsentOk = (this.records_.size() < 2);
        isAbsentOk = isAbsentOk
            || (this.records_.peekFirst() != Attendance.Absent);
        isAbsentOk = isAbsentOk
            || (this.records_.peekLast() != Attendance.Absent);
        if (isAbsentOk) {
            PrizeNode c = new PrizeNode();
            @SuppressWarnings("unchecked")
            LinkedList<Attendance> a = (LinkedList<Attendance>) this.records_
                .clone();
            if (a.size() >= 2) {
                a.poll();
            }
            a.offer(Attendance.Absent);
            c.setRecords(a);
            c.setTardiness(this.tardiness_);
            result.add(c);
        }

        return result;
    }

    @Override
    public int hashCode() {
        int result = 3699417;
        result = result ^ this.getTardiness();
        for (Attendance x : this.getRecords()) {
            result = result ^ x.hashCode();
        }
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (this.hashCode() != obj.hashCode())
            return false;

        if (obj instanceof PrizeNode) {
            PrizeNode other = (PrizeNode) obj;
            if (this.getTardiness() != other.getTardiness())
                return false;
            else if (this.getRecords().equals(other.getRecords()))
                return true;
        }

        return false;
    }
}
