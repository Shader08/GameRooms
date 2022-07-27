my_dict={'7-8': 0, '8-9': 0, '9-10': 7, '10-11': 0, '11-12': 0, '12-13': 3, '13-14': 0, '14-15': 0, '15-16': 11, '16-17': 4, '17-18': 3, '18-19': 5, '19-20': 
0, '20-21': 0}
print(sorted(my_dict.items(), key=lambda x: (x[1], int(x[0].split('-')[0]))))

new_dict={'Assasins Creed': 15, 'Fifa 23': 5, 'Age of Empires IV': 8, 'Total War': 3, "NFS":22}
marklist = sorted(new_dict.items(), key=lambda x:x[1], reverse=True)
print(marklist[:3])