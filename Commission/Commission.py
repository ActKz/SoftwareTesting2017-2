def commission( locks, stocks, barrels):
    if not 1 <= locks <= 70:
        return "Out of range value"
    if not 1 <= stocks <= 80:
        return "Out of range value"
    if not 1 <= barrels <= 90:
        return "Out of range value"
    sales = locks * 45 + stocks * 30 + barrels * 25
    if sales > 1800:
        return 1000 * 0.1 + 800 * 0.15 + (sales - 1800) * 0.2
    elif sales > 1000:
        return 1000 * 0.1 + (sales - 1000) * 0.15
    else:
        return sales * 0.1
