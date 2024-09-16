import random

false_answer = "Nein, das war leider nicht die richtige Bedeutung des Wortes. Versuche es beim nächsten Mal."

def lineAusfüllen(solution, german):
    print("Du liegst richtig! '" + solution + "' war die Bedeutung des Wortes und bedeutet auf Deutsch '" + german + "'.");

print("");
print("Willkommen zum Bayerischen Wörter Quiz!");
print("In diesem Quiz musst du entscheiden, welches bayerische Wort zum Deutschen passt.");
print("Falls du Hilfe mit der Aussprache der Wörter brauchst, gebe die Wörter hier auf dieser Website ein:");
print("https://de.forvo.com/languages/bar/");

print("");

resume = input("Drücke Enter zum Fortfahren... ");

print("");

print("Wähle deine Kategorie: (1) Was man so macht | (2) Zu Hause in Bayern | (3) In der Küche");
print("---------------------");
choose = input("Deine Auswahl: ");

print("");

if choose == '1':
    wordlist1 = ['Jodeln: (1) schwimmen | (2) singen | (3) lachen',
                'Obandln: (1) flirten | (2) weinen | (3) beten',
                'Babba: (1) husten | (2) betteln | (3) kleben',
                'Griang: (1) schlafen | (2) bekommen | (3) zusammenarbeiten'
                ];
    quiz_word = random.choice(wordlist1);
    print(quiz_word);

    selection = input("Gebe deine Auswahl ein: ");

    if quiz_word == 'Jodeln: (1) schwimmen | (2) singen | (3) lachen':
        print("");
        if selection == '2':
            lineAusfüllen("Jodeln", "singen");
        else:
            print(false_answer);
    
    if quiz_word == 'Obandln: (1) flirten | (2) weinen | (3) beten':
        print("");
        if selection == '1':
            lineAusfüllen("Obandln", "flirten");
        else:
            print(false_answer);
    
    if quiz_word == 'Babba: (1) husten | (2) betteln | (3) kleben':
        print("");
        if selection == '3':
            lineAusfüllen("Babba", "kleben");
        else:
            print(false_answer);

    if quiz_word == 'Griang: (1) schlafen | (2) bekommen | (3) zusammenarbeiten':
        print("");
        if selection == '2':
            lineAusfüllen("Griang", "bekommen");
        else:
            print(false_answer);

if choose == '2':
    wordlist2 = ['Glump: (1) Schöne Sache | (2) minderwertige Ware | (3) Vorschlag',
                'Diddn: (1) Tasche | (2) Hose | (3) Shirt',
                'Drebbm: (1) Toilette | (2) Topf | (3) Treppe',
                'Buidl: (1) Reserve | (2) Bild | (3) Desert'            
                ];
    quiz_word = random.choice(wordlist2);
    print(quiz_word);

    selection = input("Gebe deine Auswahl ein: ");

    if quiz_word == 'Glump: (1) Schöne Sache | (2) minderwertige Ware | (3) Vorschlag':
        print("");
        if selection == '2':
            lineAusfüllen("Glump", "minderwertige Ware");
        else:
            print(false_answer);

    if quiz_word == 'Diddn: (1) Tasche | (2) Hose | (3) Shirt':
        print("");
        if selection == '1':
            lineAusfüllen("Diddn", "Tasche");
        else:
            print(false_answer);

    if quiz_word == 'Drebbm: (1) Toilette | (2) Topf | (3) Treppe':
        print("");
        if selection == '3':
            lineAusfüllen("Drebbm", "Treppe");
        else:
            print(false_answer);

    if quiz_word == 'Buidl: (1) Reserve | (2) Bild | (3) Desert':
        print("");
        if selection == '2':
            lineAusfüllen("Buidl", "Bild");
        else:
            print(false_answer);

if choose == '3':
    wordlist3 = ['Kich: (1) Küche | (2) Zimmer | (3) Wohnzimmer',
                'Gmias: (1) Bier | (2) Frucht | (3) Gemüse',
                'Budda: (1) Schere | (2) Brot | (3) Butter ',
                'Pfandl: (1) Pfanne | (2) Apfel | (3) Teig'
                ];
    quiz_word = random.choice(wordlist3);
    print(quiz_word);

    selection = input("Gebe deine Auswahl ein: ");

    if quiz_word == 'Kich: (1) Küche | (2) Zimmer | (3) Wohnzimmer':
        print("");
        if selection == '1':
            lineAusfüllen("Kich", "Küche");
        else:
            print(false_answer);

    if quiz_word == 'Gmias: (1) Bier | (2) Frucht | (3) Gemüse':
        print("");
        if selection == '3':
            lineAusfüllen("Gmias", "Gemüse");
        else:
            print(false_answer);

    if quiz_word == 'Budda: (1) Schere | (2) Brot | (3) Butter ':
        print("");
        if selection == '3':
            lineAusfüllen("Budda", "Butter");
        else:
            print(false_answer);

    if quiz_word == 'Pfandl: (1) Pfanne | (2) Apfel | (3) Teig':
        print("");
        if selection == '1':
            lineAusfüllen("Pfandl", "Pfanne");
        else:
            print(false_answer);
