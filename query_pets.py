import sqlite3 as lite
import sys

# call database
con = lite.connect('pets')
# con = lite.connect('pets.db') //if above con is not working ex)sqlite3.DatabaseError: file is not a database
# connect with lateset vesion of sqlite
with con:
    cur = con.cursor()

    while(True):
        person_id = raw_input("What is Person ID? ")
        # query statement with join
        cur.execute("SELECT * FROM person JOIN person_pet ON person.id = person_pet.person_id JOIN pet ON person_pet.pet_id = pet.id WHERE person.id = %s"%(person_id))

        rows = cur.fetchall()
        if person_id == '-1':
            # program exit
            exit()
        else:
            if rows:
                cnt = 1
                for row in rows:
                    person_info = row[1] + ' ' + row[2] + ', ' + str(row[3]) + ' years old'
                    if cnt == 1:
                        print("Person : %s"%(person_info))
                    cnt+=1

                    pet_info = 'Pet : ' + row[1] + ' ' + row[2] + ' owned ' + row[7] + ', ' + row[8] + ', that was ' + str(row[9]) +' years old'
                    print(pet_info)

            else:
                print('No person id found')




