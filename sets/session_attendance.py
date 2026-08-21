# Students present in the morning session
morning_session = {"Alice", "Bob", "Charlie", "David"}

# Students present in the afternoon session
afternoon_session = {"Charlie", "David", "Emma", "Fred"}

# Find students present in both sessions
both_sessions = morning_session.intersection(afternoon_session)

# Find students present only in the morning
only_morning = morning_session.difference(afternoon_session)

# Find students present only in the afternoon
only_afternoon = afternoon_session.difference(morning_session)

# Find students present in at least one session (union)
at_least_one = morning_session.union(afternoon_session)

# Display results
print("Morning session:", morning_session)
print("Afternoon session:", afternoon_session)
print("Students present in both sessions:", both_sessions)
print("Students present only in the morning:", only_morning)
print("Students present only in the afternoon:", only_afternoon)
print("Students present in at least one session:", at_least_one)
