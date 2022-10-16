import random


first_name = ( 'Ludo','Bathilda','Helga','Rubeus','  Godric','  Hermione','  Aberforth','Bill',' Lord Voldemort',
                'Cedric',"Fleur",'Alastor','Barty ','Dolores ','Bellatrix','Sirius','Gellert','Sybill','Ron',
                'Myrtle','Tom','Severus','Merope','Rowena','Helena','Quirinus ','James','Harry ','Alastor',
                'Nymphadora', 'Horace',"Remus",' Xenophilius',' Newt ','Luna','Neville','Viktor','Helga','Rubeus',)


last_names = (' Bagman',' Bagshot',' Grindelwald' ,'Black','Lestrange','Umbridge','Crouch Sr ',' Moody',' Delacour',' Diggory',
              ' Weasley','Dumbledore','Granger',' Gryffindor',' Hagrid',' Hufflepuff',' Krum ',' Longbottom',' Chang ',' Lovegood',
              ' Scamander','Lupin',' McGonagall',' Slughorn','Tonks ','(Mad-Eye) Moody','Potter ','Quirrell',' Ravenclaw ','Voldemort',
              'snape','Marvolo Riddle',' Warren',' Weasley','Trelawney')

middle_names= ( 'Motormouth','Crazy Eyes','Doofus','Nearly Headless','Dumb Bull Doors',
                'Malfoy\’s Manners','Hogwarts Dropouts','Bloody Morons','Hungry Hufflepuffs',
                'Soul Eaters.','Muggle-borns.','Wild Weasleys','The Chosen One','Obliviators.')

def main():
 while (True):
    f= random.choice(first_name)
    m = random.choice(middle_names)
    l =random.choice(last_names)
    print(f"{f}    '{m} ' {l} ")
    inp = input('Enter yes to continue no to exit  ')
    inp.lower
    if inp == 'no':
        break
    elif inp == "yes" : 
        continue

main()


  


  
