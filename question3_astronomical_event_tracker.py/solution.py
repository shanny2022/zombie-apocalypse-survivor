def astronomical_event_tracker(showers):
    events = []

    for start, end in showers:
        events.append((start, 1))   # shower starts
        events.append((end, -1))    # shower ends

    events.sort()

    current = 0
    max_concurrent = 0

    for time, change in events:
        current += change
        max_concurrent = max(max_concurrent, current)

    return max_concurrent


# Example tests
print(astronomical_event_tracker([
    ["2025-11-17 21:00:00", "2025-11-17 23:00:00"],
    ["2025-11-17 22:00:00", "2025-11-18 01:00:00"],
    ["2025-11-18 00:00:00", "2025-11-18 02:00:00"]
]))  # 2

print(astronomical_event_tracker([
    ["2099-12-31 23:59:59", "2100-01-01 00:00:01"]
]))  # 1
