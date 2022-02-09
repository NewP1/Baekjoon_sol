m_list = list(map(int, input().split()))

sort_m = sorted(m_list)
rsort_m = sorted(m_list, reverse=True)

if m_list == sort_m:
    print("ascending")
elif m_list == rsort_m:
    print("descending")
else:
    print("mixed")