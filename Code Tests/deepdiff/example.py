from deepdiff import DeepDiff

t1 = [1, 3, 1, 4]
t2 = [4, 4, 1]

ddiff = DeepDiff(t1, t2, ignore_order=True, report_repetition=True)
print(ddiff)
