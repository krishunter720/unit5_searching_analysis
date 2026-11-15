
# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search by testing both algorithms with small and large sorted datasets. I also tested different edge cases to see how each algorithm handled them.

## Learning Objectives

- Implemented linear search
- Implemented binary search
- Compared search results using different dataset sizes
- Analyzed algorithm efficiency
- Tested edge cases

## Implementation

I implemented two search functions.

- **Linear Search:** Checked each item from the beginning of the list until the target was found. It returned the index or -1 if the value was not found.
- **Binary Search:** Used the middle of a sorted list to eliminate half of the remaining search area during each step. It returned the index or -1 if the value was not found.

## Testing

I tested both algorithms using a small dataset containing 10 values and a large dataset containing 100,000 values.

Both algorithms returned the correct indexes for values that existed and returned -1 for values that were missing.

I also tested these edge cases:

- Empty list
- Single-element list
- Searching for the first value
- Searching for the last value
- Searching for a value that was not present

Both algorithms handled all of these tests correctly.

## Performance Analysis

Linear search had O(n) time complexity because it could need to check every item in the list.

Binary search had O(log n) time complexity because it removed half of the remaining search area during each iteration.

Binary search was more efficient for large sorted datasets. However, linear search was still useful for smaller or unsorted collections because it did not require the data to be sorted first.

## Real-World Application

A real-world example of linear search would be looking through an unsorted list of files to find a specific document. Binary search would be more useful when searching through an organized list, such as an alphabetized contact list.

## Discussion Board Reflection

After completing this assignment, I learned how linear search and binary search work and why they have different speeds. Linear search checks items one at a time, while binary search cuts the search area in half each time. One challenge was making sure both searches worked with empty lists and values that were not in the list. I fixed this by testing different situations and comparing the results. I also learned that binary search is much faster when working with large lists, but the list has to be sorted first. Linear search is slower, but it can be used on unsorted data and is easier to use when there are only a few items. A real-world example would be looking through an unsorted folder for a file, where linear search would work fine. If the files were organized alphabetically, binary search could make finding one much faster. Overall, I learned that the best search method depends on how the data is organized and how much data needs to be searched.