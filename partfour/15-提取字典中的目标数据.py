counts = {"test1": 90, "test2": 80, "test3": 85, "test4": 60, "test5": 40}
count1 = {key: value for key, value in counts.items() if value >= 80}
print(count1)


