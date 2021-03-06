# import unittest
# from pymongo import MongoClient

# class TestMongoInsertFunctions(unittest.TestCase):

#   def setUp(self):
#     # Get a reference to the MongoDB
#     self.client = MongoClient('mongodb://localhost:27017/')
#     self.db = self.client['quotes']
#     self.collection = self.db['simple']

#   def testConn(self):
#     quotes = [
#       {
#         'text': "Waar ik inmiddels behoorlijk zenuwachtig van wordt is het lot van Jip en Janneke.",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Since there is absolutely no logical reason to assume there is an afterlife, I decided to make the life I have now as much fun as possible.",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Ik heb besloten om me terug te trekken uit het voetbal en ga me volledig inzetten voor het supporterschap van de wielerploeg Francaise des Jeux!",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Blijkbaar leidt in de politiek een zoen tot meer ophef dan fraude! Zo komt het natuurlijk nooit goed met Nederland!",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Een vrolijke vrind is U goed gezind!",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Je oude rommel verkopen op Koningsdag! Dat kan niet anders dan een Republikein zijn die dat heeft verzonnen!",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Op papier is Messi de beste speler ter wereld. Vanavond spelen we op gras.",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Als je je pink in je oor doet, en dan op en neer gaat, klinkt het als Pacman. Toch??",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Everyone you meet is fighting a battle you know nothing about. That's why u must be kind always!",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "RIVM waarschuwt geen rauw vlees te eten uit Ebola-landen. Nou had ik toch al niet zo'n trek in rauwe Liberiaanse geit.",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Eindelijk weer eens tijd om iets op Facebook te plaatsen! ....... Dat was het dan weer!! Tot de volgende keer!",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Het voordeel van in een vrouwengezin leven is dat je als een echte prinses behandeld wordt!!! ",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Tuurlijk heb ik mening! :) Niet vies van Erik van Wunnik marketing! ;)",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "A library makes me smart on a photo!",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "Iedereen veel drank, liefde en goeie muziek de komende feestdagen! Ik zeker......",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "I will not follow where the path may lead, but I will go where there is no path, and I will leave a trail.",
#         'who': "Erik van Wunnik"
#       },
#       {
#         'text': "The more future to come, the more customers to satisfy",
#         'who': "Erik van Wunnik"
#       }
#     ]
#     for quote in quotes:
#       ## print values
#       # for kk, vv in quote.iteritems():
#       #   print kk, ': ', vv
#       quote_id = self.collection.insert(quote)
#       print 'inserted: ', quote_id

# suite = unittest.TestLoader().loadTestsFromTestCase(TestMongoInsertFunctions)
# unittest.TextTestRunner(verbosity=2).run(suite)
