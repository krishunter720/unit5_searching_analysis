
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student): COMPLETED

    Implement a linear search algorithm.
    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Check each item in the list, starting at index 0.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # If the loop finishes, the target was not found.
    # Linear search has O(n) time complexity because
    # it may need to examine every item in the list.
    return -1


def binary_search(lst, target):
    """
    TODO (Student): COMPLETED

    Implement a binary search algorithm.
    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:
        # Find the middle position of the current search area.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        elif lst[middle] < target:
            # The target must be in the right half.
            # Moving left past the middle eliminates
            # the entire left half from consideration.
            left = middle + 1

        else:
            # The target must be in the left half.
            # Moving right before the middle eliminates
            # the entire right half from consideration.
            right = middle - 1

    # The search area is empty, so the target is not present.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # COMPLETED
    # ===============================
    #
    # Create a small sorted dataset.
    # Test both searches with an existing
    # value and a value that does not exist.
    #
    # Both algorithms return the index when
    # a value is found and -1 when it is missing.

    print("\n=== SMALL DATASET TEST ===")

    small_data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    existing_value = 30
    missing_value = 99

    print("Small dataset:", small_data)

    print("\nSearching for an existing value:", existing_value)
    print("Linear search result:", linear_search(small_data, existing_value))
    print("Binary search result:", binary_search(small_data, existing_value))

    print("\nSearching for a missing value:", missing_value)
    print("Linear search result:", linear_search(small_data, missing_value))
    print("Binary search result:", binary_search(small_data, missing_value))

    # ===============================
    # TODO (Student): LARGE DATASET
    # COMPLETED
    # ===============================
    #
    # Create a much larger sorted dataset.
    # Both algorithms search for the same values.
    #
    # Binary search becomes more efficient as the
    # dataset grows because it removes half of the
    # remaining search area during every iteration.
    # Linear search may still need to check every item.

    print("\n=== LARGE DATASET TEST ===")

    large_data = list(range(1, 100001))

    large_existing_value = 87654
    large_missing_value = 120000

    print("Large dataset contains", len(large_data), "items.")

    print("\nSearching for an existing value:", large_existing_value)
    print("Linear search result:", linear_search(large_data, large_existing_value))
    print("Binary search result:", binary_search(large_data, large_existing_value))

    print("\nSearching for a missing value:", large_missing_value)
    print("Linear search result:", linear_search(large_data, large_missing_value))
    print("Binary search result:", binary_search(large_data, large_missing_value))

    # Linear search has O(n) time complexity.
    # Binary search has O(log n) time complexity.
    # Binary search is faster on large sorted datasets
    # because it eliminates half the remaining values
    # with each comparison.

    # ===============================
    # TODO (Student): EDGE CASES
    # COMPLETED
    # ===============================
    #
    # Demonstrate multiple edge cases:
    # - Empty list
    # - Single-element list
    # - First and last positions
    # - Value not present

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_data = []
    print("\nEdge Case 1: Empty list")
    print("Linear search:", linear_search(empty_data, 10))
    print("Binary search:", binary_search(empty_data, 10))
    # Both return -1 because the list has no elements.

    # Edge Case 2: Single-element list
    single_data = [25]
    print("\nEdge Case 2: Single-element list")
    print("Linear search:", linear_search(single_data, 25))
    print("Binary search:", binary_search(single_data, 25))
    # Both return index 0 because the target is the only item.

    # Edge Case 3: First and last positions
    boundary_data = [10, 20, 30, 40, 50]
    print("\nEdge Case 3: First and last positions")
    print("First value (10):")
    print("Linear search:", linear_search(boundary_data, 10))
    print("Binary search:", binary_search(boundary_data, 10))

    print("Last value (50):")
    print("Linear search:", linear_search(boundary_data, 50))
    print("Binary search:", binary_search(boundary_data, 50))

    # Edge Case 4: Missing value
    print("\nEdge Case 4: Missing value")
    print("Linear search:", linear_search(boundary_data, 99))
    print("Binary search:", binary_search(boundary_data, 99))
    # Both return -1 when the target is not found.

    print("\n=== ALL SEARCH TESTS COMPLETED ===")


if __name__ == "__main__":
    main()