use std::cmp::max;  
  
// This may not be so optimal, as I simply ported python solution to rust.

impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = vec![];
        let mut intervals = intervals;

        intervals.sort();
        let mut cur = intervals[0].clone();

        // Since sorted by [0], only one comparison is needed
        for node in &intervals[1..] {
            if node[0] <= cur[1] {
                cur = vec![cur[0], max(cur[1], node[1])];
            } else {
                ans.push(cur.clone());
                cur = node.clone();
            }
        }
        ans.push(cur);
        ans
    }
}
