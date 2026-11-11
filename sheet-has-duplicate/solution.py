def has_duplicate(nums):
    """Return True if any value appears at least twice."""
    # This is correct but too slow: it compares every pair of values.
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
