import sqlite3
import unittest

class TestSQLiteInsertFunctions(unittest.TestCase):
  def testConn(self):
    sqlite_file = 'quotes_test_db.sqlite'
    quotes_table = 'quotes'
    saying_field = 'saying'
    saying_field_type = 'TEXT'
    who_field = 'who'
    who_field_type = 'TEXT'
    index_name = 'id'

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # Creating a new SQLite table with 2 columns
    c.execute('CREATE TABLE {tn} (id integer primary key, {sf} {sft}, {wf} {wft})'\
            .format(tn=quotes_table, sf=saying_field, sft=saying_field_type, wf=who_field, wft=who_field_type))

    # Committing changes
    conn.commit()
    quotes = [
      {
        'saying': "Waar ik inmiddels behoorlijk zenuwachtig van wordt is het lot van Jip en Janneke.",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Since there is absolutely no logical reason to assume there is an afterlife, I decided to make the life I have now as much fun as possible.",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Ik heb besloten om me terug te trekken uit het voetbal en ga me volledig inzetten voor het supporterschap van de wielerploeg Francaise des Jeux!",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Blijkbaar leidt in de politiek een zoen tot meer ophef dan fraude! Zo komt het natuurlijk nooit goed met Nederland!",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Een vrolijke vrind is U goed gezind!",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Je oude rommel verkopen op Koningsdag! Dat kan niet anders dan een Republikein zijn die dat heeft verzonnen!",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Op papier is Messi de beste speler ter wereld. Vanavond spelen we op gras.",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Als je je pink in je oor doet, en dan op en neer gaat, klinkt het als Pacman. Toch??",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Everyone you meet is fighting a battle you know nothing about. That's why u must be kind always!",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "RIVM waarschuwt geen rauw vlees te eten uit Ebola-landen. Nou had ik toch al niet zo'n trek in rauwe Liberiaanse geit.",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Eindelijk weer eens tijd om iets op Facebook te plaatsen! ....... Dat was het dan weer!! Tot de volgende keer!",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Het voordeel van in een vrouwengezin leven is dat je als een echte prinses behandeld wordt!!! ",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Tuurlijk heb ik mening! :) Niet vies van Erik van Wunnik marketing! ;)",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "A library makes me smart on a photo!",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "Iedereen veel drank, liefde en goeie muziek de komende feestdagen! Ik zeker......",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "I will not follow where the path may lead, but I will go where there is no path, and I will leave a trail.",
        'who': "Erik van Wunnik"
      },
      {
        'saying': "The more future to come, the more customers to satisfy",
        'who': "Erik van Wunnik"
      }
    ]

    for x in quotes:
      try:
        c.execute("INSERT INTO {tn} ({sf}, {wf}) VALUES (\"{sv}\", \"{wv}\")".\
          format(tn=quotes_table, sf=saying_field, wf=who_field, sv=x['saying'], wv=x['who']))
      except sqlite3.IntegrityError:
        print('ERROR')
      print ('inserted: ', x['saying'], ': ', x['who'])
      conn.commit()

    # close the connection to the database file
    conn.close()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSQLiteInsertFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
