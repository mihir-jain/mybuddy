import hillcipher

hillcipher.user = "none"
K = [[0, 72, 47], [57, 33, 88], [6, 73, 68]]
m = input('What is your username? ')
n = input('What is your password? ')
with open('user.txt', 'r') as f:
    gh = f.readlines()
my = False
for i in gh:
    i = i.strip()
    i = i.split()
    if m == i[0]:
        my = True
        i.remove(m)
        password = [[],[],[]]
        i[0] = i[0].replace("[", '', 1)
        i[-1] = i[-1].replace("]", '', 1)
        counter = 0
        for word in i:
          updatedWord = word.replace("[", '').replace("]", '')
          addCounter = "]" in word
          password[counter].append(int(updatedWord))
          if addCounter:
            counter += 1
        decrypted = hillcipher.matrix_to_string(hillcipher.decrypt_plaintext(K, password))
        decrypted = decrypted.strip()
        if n == decrypted:
            with open(m + '.txt', 'r') as f:
                nam = f.readline()
                hillcipher.user = m
            print('Welcome back', nam)
        else:
            print('Invalid password')
if not my:
    hillcipher.user = m
    open(m + '.txt', 'w')
    print('Creating account!')
    with open('user.txt', 'a') as f:
        encripted = hillcipher.generate_ciphertext(K, hillcipher.string_to_matrix(hillcipher.add_filler_text(n)))
        f.write(m + ' ' + str(encripted).replace('\n', ' ') + '\n')

    with open(m + '.txt', 'w') as f:
        print('Time for an introduction questionaire!!!')
        name = input('What would you like to me called? (This does not have to be your name) ')
        name = name.lower()
        name = name[0].upper() + name[1:]
        f.write(name + '\n')
        gender = input("What is your gender? ")
        f.write(gender + '\n')
        grade = input("What grade are you in? ")
        f.write(grade + '\n')
        lgbt = input('Are you part of the LGBT+ community or an ally? ')
        f.write(lgbt + '\n')
        color = input('Which color is your favorite? ')
        f.write(color + '\n')
        mood = input('How do you feel on a daily basis? ')
        f.write(mood + '\n')
        sport = input('Do you like sports? ')
        f.write(sport + '\n')
        music = input('What is your favorite genre of music? ')
        f.write(music + '\n')
        stress = input('On a scale of 1-5, how stressed are you? ')
        f.write(stress + '\n')
        subjectNumber = input('How many subjects are you struggling in? ')
        f.write(subjectNumber + '\n')
        for i in range(int(subjectNumber)):
          subject = input('What is one subject that you are struggling in? ')
          f.write(subject + '\n')
print()