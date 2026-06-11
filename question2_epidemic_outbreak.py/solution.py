def epidemic_outbreak(infected):
    for i in range(1, len(infected)):
        if infected[i] < infected[i - 1]:
            return i + 1  # 1-based day number
    return 0


# Example tests
print(epidemic_outbreak([1, 2, 3, 2, 1]))      # 4
print(epidemic_outbreak([99999, 99999]))       # 0
