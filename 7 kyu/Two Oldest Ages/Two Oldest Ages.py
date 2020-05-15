def two_oldest_ages(ages):
    m = max(ages)
    ages.remove(m)
    smax = max(ages)
    return [smax, m]