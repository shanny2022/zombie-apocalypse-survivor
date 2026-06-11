def zombie_apocalypse_survivor(total_food, survivors):
    n = len(survivors)

    # dp[i][f] = max skill using first i survivors with f food
    dp = [[0] * (total_food + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        skill, food = survivors[i - 1]

        for f in range(total_food + 1):
            # Don't keep survivor
            dp[i][f] = dp[i - 1][f]

            # Keep survivor if enough food
            if food <= f:
                dp[i][f] = max(
                    dp[i][f],
                    dp[i - 1][f - food] + skill
                )

    # Reconstruct chosen survivors
    result = []
    f = total_food

    for i in range(n, 0, -1):
        if dp[i][f] != dp[i - 1][f]:
            skill, food = survivors[i - 1]
            result.append([skill, food])
            f -= food

    result.reverse()
    return result
