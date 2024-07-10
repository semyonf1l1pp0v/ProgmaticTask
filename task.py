def find_combinations(digits, target_sum, partial=None, partial_sum=0):
    if partial is None:
        partial = []
    if partial_sum == target_sum:
        print(''.join(partial))
    if digits == '':
        return
    for i in range(1, len(digits) + 1):
        find_combinations(digits=digits[i:], target_sum=target_sum, partial=partial + ['+' + digits[:i]], partial_sum=partial_sum + int(digits[:i]))
        find_combinations(digits=digits[i:], target_sum=target_sum, partial=partial + ['-' + digits[:i]], partial_sum=partial_sum - int(digits[:i]))


find_combinations('9876543210', 200)
