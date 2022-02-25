import csv
with open('C:\\Users\\Dell\\Desktop\\name_age.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open('C:\\Users\\Dell\\Desktop\\name_age.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'fide_rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})