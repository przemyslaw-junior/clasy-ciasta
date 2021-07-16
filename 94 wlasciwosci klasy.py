# stworzenie klasy torty z atrybutami
# - name(nazwa), - kind(rodzaj), -taste(smak), - addictions(dodatki), - filling(nadzienie)

class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        # jezeli nazwa jest w liście nazw podaj ją, jeżeli nie to wyświetl "Other"
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = "Other"
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        # dodanie ciasta do listy
        self.bakery_offer.append(self)
        # dodanie ukrytej informacji
        self.__gluten_free = gluten_free
        # dodenie ukrytego atrybutu
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

       
    # dodanie informacji o produkcie
    def show_info(self):
        print ('Nazwa - {}, Rodzaj - {}'.format(self.name, self.kind).upper())
        print ('smak -      {}'.format( self.taste))
        print ('wolne od glutenu -  {}'.format( self.__gluten_free))
        # wypunktowanie dodatku
        if len(self.additives) > 0:
            print ('Aditives')
            for a in self.additives:
                print ('\t{}'.format(a))
        # wypunktowanie nadzienia
        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-'*30)   

    # dodanie inf o ciastach
    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives = additives

    def __get_text(self):
        return  self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
             print('>>>>>Text can be set only for cake ({})'.format(self.name))
    Text = property(__get_text, __set_text, None, 'Text on the cake')
 


# stworzenie kilku instancji
cake_01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade','nuts'],'cream', False,  'Happy Birthday Margaret!')
cake_02 = Cake('Chokolade Muffin','muffin', 'chokolade', ['chokolade'],'',False, '')
cake_03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [],'',True, '')
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa',False, '')


'''
# utworzenie listy bakery_offer i dodanie do niej utworzonych obiektów klasy
bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)
bakery_offer.append(cake_04)
'''

# dodenie kolejnych informacji o ciastach
cake_02.set_filling('vanilla cream')
cake_03.add_additives(['coca powder', 'coconuts'])

# iterując przez liste wyświetl inf o ciastach
print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

cake_01.Text = 'Happy Birthday Margaret!'
cake_02.Text = '18'
'''
# Wyświetl informacje o "instancji" cake01 i o klasie Cake korzystając z funkcji "vars" i "dir"
print('Is cake_01 of type Cake? (isinstance)', isinstance(cake_01, Cake))
print()
print('Is cake_01 of type Cake? (type)', type(cake_01) is Cake)
print()
print('vars cake_01', vars(cake_01))
print()
print('vars Cake?', vars(Cake))
print()
print('dir cake_01', dir(cake_01))
print()
print('dir Cake?', dir(Cake))
'''

# wyświetlenie informacji ukrytych 
cake_03.__gluten_free = False
print(dir(cake_03))
cake_03._Cake__gluten_free = False
cake_03.show_info()