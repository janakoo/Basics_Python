m_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 555]
m_list2=[m_list[i] for i in range (1,len(m_list)) if m_list[i] > m_list[i-1]]
print(m_list2)