print('Welkom op de mini pop quiz!')
answer=input('Let op de spelling en hoofdletters! Ben je klaar om te spelen ? (ja/nee) :')
score=0
total_questions=5
 

if answer.lower()=='ja':
    # ------1
    answer=input('Vraag 1: Welke band bracht in 1975 het nummer Bohemiam Rhapsody uit? ')
    if answer == 'Queen':
        score += 1
        print('Goed!')
    else:
        print('Fout Antwoord :(')

    # ------2
    answer=input('Vraag 2: Welke artiest werd ook wel "the king of pop" genoemd? ')
    if answer == 'Michael Jackson':
        score += 1
        print('Goed!')
    else:
        print('Fout Antwoord! :(')

    # ------3
    answer=input('Vraag 3: Welke act won het Eurovisiesongfestival in 2006 ')
    if answer == 'Lordi':
        score += 1
        print('Goed!')
    else:
        print('Fout Antwoord :(')

    # ------4
    anwser=input('Vraag 4: Met welk liedje brak Justin Bieber door bij het grote publiek? ')
    if anwser == 'Baby':
        score += 1
        print('Goed!')
    else:
        print('Fout Antwoord :(')

    # ------5
    anwser=input('Vraag 5: In welke andere taal zong Celine Dion in de jaren 90 regelmatig? ')
    if anwser == 'Frans':
        score += 1
        print('Goed!')
    else:
        print('Fout Antwoord :(')

print('Bedankt voor het meespelen met deze mini pop quiz, je hebt',score,"vragen goed!")
mark=(score/total_questions)*100
print('Score:',mark)
print('Doei!')
