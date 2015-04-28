init 10 python:
    locations = []
    class Location:
        def __init__(self,id,name,base_prob, position):
            self.id = id
            self.name = name
            self.base_prob = base_prob
            self.events = []
            self.position = position
            self.people = []
            
        def getprob(self):
            if lt() > 0 or lt() == -4: return -1 #Если ночь, то на улице никого нет
            elif self.position in ['classroom', 'school'] and lt() == -1: return self.base_prob/4 #Если внеурочное время, то в школе шансов встретить меньше
            else : return self.base_prob #Иначе настоящая вероятность.
    
    class Event:
        def __init__(self,id,corr):
            self.id = id
            self.corr = corr
    
    def getLoc(id):
        for x in locations:
            if x.id == id:
                return x
        return False
    
#Функция добавления эвентов в локации
    def getEvents():
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'event_': #находим тот, что с евентом
                for location in locations: #начинаем перебирать локации
                    if eventLabel.find(location.id) > 0: #Если имя локации содержится в имени эвента
                        index = eventLabel.rfind(location.id) #находим правый индекс имени локации
                        corr = eventLabel[index:] #режем по нему
                        temp = corr.split("_") #разбиваем строку по_
                        corr = int(temp[2]) #находим развратность
                        event = Event(id = eventLabel, corr = corr) # создаём эвент
                        location.events.append(event) #добавляем его в массив эвентов локации
        return 0
    
#Создание массива всех локаций
    _locs = renpy.get_all_labels()
    
    for x in _locs:
        if x[:4] == 'loc_':
            if x == 'loc_home': loc = Location(id = x, name = 'дом', base_prob = 100, position = 'home')
            elif x == 'loc_bedroom': loc = Location(id = x, name = 'спальня', base_prob = 0, position = 'home')
            elif x == 'loc_bathroom': loc = Location(id = x, name = 'ванная', base_prob = 0, position = 'home')
            elif x == 'loc_kitchen': loc = Location(id = x, name = 'кухня', base_prob = 0, position = 'home')
            
            elif x == 'loc_street': loc = Location(id = x, name = 'улица', base_prob = 15, position = 'other')
            elif x == 'loc_beach': loc = Location(id = x, name = 'пляж', base_prob = 35, position = 'other')
            elif x == 'loc_beachChange': loc = Location(id = x, name = 'раздевалка', base_prob = 0, position = 'other')
            elif x == 'loc_shopStreet': loc = Location(id = x, name = 'торговая улица', base_prob = 25, position = 'other')
            elif x == 'loc_shop': loc = Location(id = x, name = 'магазин', base_prob = 10, position = 'other')
            elif x == 'loc_shopBeauty': loc = Location(id = x, name = 'салон красоты', base_prob = 5, position = 'other')
            elif x == 'loc_sexShop': loc = Location(id = x, name = 'сексшоп', base_prob = 5, position = 'other')
            
            elif x == 'loc_hall': loc = Location(id = x, name = 'холл', base_prob = 15, position = 'school')
            elif x == 'loc_entrance': loc = Location(id = x, name = 'вход', base_prob = 15, position = 'school')
            elif x == 'loc_library': loc = Location(id = x, name = 'библиотека', base_prob = 10, position = 'school')
            elif x == 'loc_changeRoom': loc = Location(id = x, name = 'школьная раздевалка', base_prob = 5, position = 'school')
            elif x == 'loc_gym': loc = Location(id = x, name = 'спортивный зал', base_prob = 25, position = 'classroom')
            elif x == 'loc_pool': loc = Location(id = x, name = 'бассейн', base_prob = 15, position = 'classroom')
            elif x == 'loc_firstFloor': loc = Location(id = x, name = 'первый этаж', base_prob = 20, position = 'school')
            elif x == 'loc_secondFloor': loc = Location(id = x, name = 'второй этаж', base_prob = 20, position = 'school')
            elif x == 'loc_class1': loc = Location(id = x, name = 'Класс 1', base_prob = 10, position = 'classroom')
            elif x == 'loc_class2': loc = Location(id = x, name = 'Класс 2', base_prob = 10, position = 'classroom')
            elif x == 'loc_class3': loc = Location(id = x, name = 'Класс 3', base_prob = 10, position = 'classroom')
            elif x == 'loc_class4': loc = Location(id = x, name = 'Класс 4', base_prob = 10, position = 'classroom')
            elif x == 'loc_class5': loc = Location(id = x, name = 'Класс 5', base_prob = 10, position = 'classroom')
            elif x == 'loc_teacherRoom': loc = Location(id = x, name = 'учительская', base_prob = 0, position = 'school')
            elif x == 'loc_wcm': loc = Location(id = x, name = 'Туалет для мальчиков', base_prob = 5, position = 'school')
            elif x == 'loc_wcf': loc = Location(id = x, name = 'Туалет для девочек', base_prob = 5, position = 'school')
            elif x == 'loc_storage': loc = Location(id = x, name = 'кладовка', base_prob = 5, position = 'school')
            elif x == 'loc_office': loc = Location(id = x, name = 'офис', base_prob = 0, position = 'school')
            
            elif x == 'loc_dreams': loc = Location(id = x, name = 'Сны', base_prob = 0, position = 'self')
            elif x == 'loc_class1Learn': loc = Location(id = x, name = 'Учёба', base_prob = 0, position = 'tech')
            elif x == 'loc_class2Learn': loc = Location(id = x, name = 'Учёба', base_prob = 0, position = 'tech')
            elif x == 'loc_class3Learn': loc = Location(id = x, name = 'Учёба', base_prob = 0, position = 'tech')
            elif x == 'loc_class4Learn': loc = Location(id = x, name = 'Учёба', base_prob = 0, position = 'tech')
            elif x == 'loc_class5Learn': loc = Location(id = x, name = 'Учёба', base_prob = 0, position = 'tech')
            elif x == 'loc_gymLearn': loc = Location(id = x, name = 'Учёба', base_prob = 0, position = 'tech')
            elif x == 'loc_poolLearn': loc = Location(id = x, name = 'Учёба', base_prob = 0, position = 'tech')
            
            else: loc = Location(id = x, name = 'UNKNOWN', base_prob = 0, position = 'other')
            locations.append(loc)
            
    getEvents() #добавляю всем эвенты
    
######################################################
#Объявление всех картинок
init:
    image home = im.FactorScale('pic/locations/home/1.jpg', 1.5)
    image bedroom = im.FactorScale('pic/locations/home/2.jpg', 1.5)
    image bathroom = im.FactorScale('pic/locations/home/3.jpg', 1.5)
    image kitchen = im.FactorScale('pic/locations/home/4.jpg', 1.5)
    image street = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/street/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/street/2.jpg",1.5),
        )
    image beach = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/beach/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/beach/2.jpg",1.5),
        )
    image beachChange = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/beach/changeRoom/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/beach/changeRoom/2.jpg",1.5),
        )
    image shopStreet = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/shopStreet/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/shopStreet/2.jpg",1.5),
        )
    image shop = im.FactorScale('pic/locations/shop/1.jpg', 1.5)
    image shopBeauty = im.FactorScale('pic/locations/shopBeauty/1.jpg', 1.5)
    image sexShop = im.FactorScale('pic/locations/sexShop/1.jpg', 1.3)
    image hall = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/hall/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/hall/2.jpg",1.5),
        )
    image entrance = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/entrance/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/entrance/2.jpg",1.5),
        )
    image library = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/library/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/library/2.jpg",1.5),
        )
    image pool = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/pool/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/pool/2.jpg",1.5),
        )
    image gym = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/gym/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/gym/2.jpg",1.5),
        )
    image changeRoom = im.FactorScale('pic/locations/school/changeRoom/1.png', 1.5)
    image storage = im.FactorScale('pic/locations/school/storage/1.jpg', 1.5)
    image firstFloor = ConditionSwitch(
        "hour >= 5 and hour < 9", im.FactorScale("pic/locations/school/firstFloor/1.jpg",1.5),
        "hour >= 9 and hour <= 20", im.FactorScale("pic/locations/school/firstFloor/2.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/firstFloor/3.jpg",1.5),
        )
    image office = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/office/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/office/2.jpg",1.5),
        )
    image class1 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/class1/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/class1/2.jpg",1.5),
        )
    image class2 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/class2/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/class2/2.jpg",1.5),
        )
    image class3 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/class3/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/class3/2.jpg",1.5),
        )
    image class4 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/class4/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/class4/2.jpg",1.5),
        )
    image class5 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/class5/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/class5/2.jpg",1.5),
        )
    image secondFloor = ConditionSwitch(
        "hour >= 5 and hour < 9", im.FactorScale("pic/locations/school/secondFloor/1.jpg",1.5),
        "hour >= 9 and hour <= 20", im.FactorScale("pic/locations/school/secondFloor/2.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/secondFloor/3.jpg",1.5),
        )
    image teacherRoom = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.FactorScale("pic/locations/school/teacherRoom/1.jpg",1.5),
        "hour > 20 or hour < 5", im.FactorScale("pic/locations/school/teacherRoom/2.jpg",1.5),
        )
    image wcm =  im.FactorScale('pic/locations/school/secondFloor/wcm.jpg', 1.5)
    image wcf =  im.FactorScale('pic/locations/school/secondFloor/wcf.jpg', 1.5)
    
#Для теста
label test:
    python:
        player.dirty += 1
        player.coverSperm('ноги','лицо','рот','грудь','руки', 'вагина', 'анус')
        player.addItems('Салфетка','Салфетка','Салфетка')
    show daytime
    hide screen stats_screen
    player.say 'тест'
    screen empty:
        fixed:
            vbox:
                for x in range (0,10):
                    $ temp = getChar('male')
                    text temp.name
                    $ temp = getChar('female')
                    text temp.name
                textbutton _('Назад') action Function(move, 'loc_home')
    call screen empty
    

##############################################################
# Home
##############################################################
label loc_home:
    show expression im.FactorScale('pic/locations/home/1.jpg', 1.5) at left as home
    screen home:
        fixed:
            text _('Ваша маленькая квартира в этом миленьком городке. В центре комнаты стоит небольшой стеклянный столик, у стены вольготно расположилась полка с любимыми игрушками, которые Вы коллекционировали всю жизнь. Отсюда можно пойти в спальню или, если есть необходимость, в ванную. Слева выход в небольшую кухню.') xalign 0.0 yalign 1.0 style style.description
            textbutton _('Кухня') xalign 0.05 yalign 0.4 action Function(move, 'loc_kitchen') style "navigation_button" text_style "navigation_button_text"
            textbutton _('Спальня') xalign 0.05 yalign 0.5 action Function(move, 'loc_bedroom') style "navigation_button" text_style "navigation_button_text"
            textbutton _('Ванная') xalign 0.45 yalign 0.3 action Function(move, 'loc_bathroom') style "navigation_button" text_style "navigation_button_text"
            textbutton _('Улица') xalign 0.7 yalign 0.85 action Function(move, 'loc_street') style "navigation_button" text_style "navigation_button_text"
            textbutton _('Test') xalign 0.0 yalign 0.2 action Function(move,'test') style "navigation_button" text_style "navigation_button_text"
    call screen home

    label loc_bedroom:
        show bedroom at left
        screen bedroom:
            fixed:
                text _('Уютненькая маленькая спальня. Слева находится небольшой шкаф, в котором висит ваша повседневная одежда. Справа кровать, довольно удобная. Тут ещё есть телевизор, но он не работает, так что совсем не будет мешать Вам отходить ко сну.') xalign 0.0 yalign 1.0 style style.description
                textbutton _('Гостинная') xalign 0.5 yalign 0.8 action Function(move, 'loc_home') style "navigation_button" text_style "navigation_button_text"
                if (ptime - last_sleeped >= 4) or (player.energy < player.health/4):
                    textbutton _('Спать') xalign 0.85 yalign 0.7 action Jump('sleep') style "navigation_button" text_style "navigation_button_text"
        call screen bedroom
        
        
    label loc_kitchen:
        show kitchen at left
        screen kitchen:
            fixed:
                text _('Микроволновка, плита, раковина, шкафчики. Кухня одним словом. \nОценив количество оставшейся еды, Вы прикидываете, что её хватит ещё на несколько раз.') xalign 0.0 yalign 1.0 style style.description
                textbutton _('Гостинная') xalign 0.5 yalign 0.8 action Function(move, 'loc_home') style "navigation_button" text_style "navigation_button_text"
                
        call screen kitchen
        

    label loc_bathroom:
        show bathroom at left
        screen bathroom:
            fixed:
                text _('Ванная комната. Совмещённая. В лучших традициях далёкой страны. Тут можно искупаться, чтобы смыть с себя грязь и прочие человеческие нечистоты. А можно просто постоять под душем и отдохнуть.') xalign 0.0 yalign 1.0 style style.description
                textbutton _('Гостинная') xalign 0.5 yalign 0.8 action Function(move, 'loc_home') style "navigation_button" text_style "navigation_button_text"
                textbutton _('Душ') xalign 0.4 yalign 0.2 action Jump('shower') style "navigation_button" text_style "navigation_button_text"
                
        call screen bathroom
        
    

##############################################################
# SCHOOL
##############################################################
label loc_entrance:
    show entrance at left
    screen entrance:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text _('Вход в Вашу новую школу. Ворота, крыльцо, всё как у всех, ничего необычного. Разве что кусты не особо пострижены, и дети там периодически играют, ну да ладно.') style style.description
                if is_library == 0:
                    text _('Слева от школы полно места. Вроде как там раньше стоял сарай, но он давным давно рухнул, и теперь земля пустует. Библиотеку чтоли там построить? ') style style.description
                else:
                    text _('Справа от школы виден вход в школьную библиотеку. В самом деле, замечательное приобретение! ') style style.description
                if is_wall == 0:
                    text _('Окидывая взглядом свои владения, вы видите прекрасный вид на окна школы. Выглядит конечно красиво, но как то всё напоказ. ') style style.description
                else:
                    text _('Довольно высокая стена окружает школу. С улицы вообще непонятно, толи это школа, толи режимный объект. ') style style.description
            textbutton _('Холл') xalign 0.456 yalign 0.7 action [Function(move, 'loc_hall')] style "navigation_button" text_style "navigation_button_text"
            textbutton _('Первый этаж') xalign 0.456 yalign 0.5 action [Function(move, 'loc_firstFloor')] style "navigation_button" text_style "navigation_button_text"
            textbutton _('Второй этаж') xalign 0.456 yalign 0.35 action [Function(move, 'loc_secondFloor')] style "navigation_button" text_style "navigation_button_text"
            textbutton _('Ваш офис') xalign 0.6 yalign 0.5 action [Function(move, 'loc_office')] style "navigation_button" text_style "navigation_button_text"
            textbutton _('Домой') xalign 0.1 yalign 0.7 action [Function(changetime, 30),Function(move, 'loc_street')] style "navigation_button" text_style "navigation_button_text"
            if is_library == 1: 
                textbutton _('Библиотека') xalign 0.8 yalign 0.7 action [Function(move, 'loc_library')] style "navigation_button" text_style "navigation_button_text"
    call screen entrance
    
    label loc_library:
        show library at left
        screen library:
            fixed:
                vbox xalign 0.0 yalign 1.0:
                    text _('Недавно построенная школьная библиотека. Всё  сделано на удивление быстро и качественно. Городская библиотека выделила много книг на её заполнение, которые всё равно готовились списать.') style style.description
                    text _('В любом случае тут - прекрасное место для самообразования и не только!') style style.description
                textbutton _('Выход') xalign 0.5 yalign 0.8 action [Function(move, 'loc_entrance')] style "navigation_button" text_style "navigation_button_text"
        call screen library
        
        
    label loc_hall:
        show hall at left
        screen hall:
            fixed:
                vbox xalign 0.0 yalign 1.0:
                    text _('По всему холлу расставлены шкафчики для личных вещей. И еще лавочки, сидя на которых удобно переобуваться. В образующих шкафчиками коридорах легко потеряться с непривычки. По школе ходят ужасные истории, что из первого выпуска школы, ещё никто не вернулся домой. Так и бродят они до сих пор по коридорам, и воруют у новых учеников обувь, чтобы починить свои стоптанные за года блужданий ботинки. Глупая история, считаете Вы.') style style.description
                textbutton _('Первый этаж') xalign 0.1 yalign 0.7 action [Function(move, 'loc_firstFloor')] style "navigation_button" text_style "navigation_button_text"
                textbutton _('Бассейн') xalign 0.8 yalign 0.7 action [Function(move, 'loc_pool')] style "navigation_button" text_style "navigation_button_text"
                textbutton _('Спортзал') xalign 0.8 yalign 0.6 action [Function(move, 'loc_gym')] style "navigation_button" text_style "navigation_button_text"
                textbutton _('Выход') xalign 0.5 yalign 0.5 action [Function(move, 'loc_entrance')] style "navigation_button" text_style "navigation_button_text"
        call screen hall

        label loc_pool:
            show pool at left
            screen pool:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Бассейн. Здесь проходят занятия по вторникам и четвергам. Хотя так же в перемены, и после уроков ученики могут придти сюда, чтобы поплавать или просто постоять глядя на воду. Вы так же можете немного потренировать своё здоровье, попытавшись проплыть стометровку пару раз.') style style.description
                        text _('Неподалеку от бассейна находится душ, где Вы в любой момент можете освежиться.') style style.description
                    textbutton 'Раздевалка' xalign 0.2 yalign 0.1 action [Function(move, 'loc_changeRoom')] style "navigation_button" text_style "navigation_button_text"
                    textbutton _('В душ') xalign 0.05 yalign 0.7 action Jump('shower') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Холл') xalign 0.5 yalign 0.8 action [Function(move, 'loc_hall')] style "navigation_button" text_style "navigation_button_text"
            call screen pool
            
            
        label loc_changeRoom:
            show changeRoom at left
            screen changeRoom:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Раздевалка. Она разделена на 2 отделения для мальчиков и девочек. Как ни странно, Вы тоже можете тут переодеваться. В отделении для девочек разумеется. Хотя кто знает, что там в соседнем отделении? Вы точно не знаете.') style style.description
                    textbutton _('Бассейн') xalign 0.2 yalign 0.8 action [Function(move, 'loc_pool')] style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Спортзал') xalign 0.8 yalign 0.8 action [Function(move, 'loc_gym')] style "navigation_button" text_style "navigation_button_text"
            call screen changeRoom
                
            
        label loc_gym:
            show gym at left
            screen gym:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Раздевалка. Она разделена на 2 отделения для мальчиков и девочек. Как ни странно, Вы тоже можете тут переодеваться. В отделении для девочек разумеется. Хотя кто знает, что там в соседнем отделении? Вы точно не знаете.') style style.description
                    textbutton _('Кладовка') xalign 0.35 yalign 0.3 action [Function(move, 'loc_storage')] style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Раздевалка') xalign 0.8 yalign 0.8 action [Function(move, 'loc_changeRoom')] style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Холл') xalign 0.5 yalign 0.8 action [Function(move, 'loc_hall')] style "navigation_button" text_style "navigation_button_text"
            call screen gym
            
            label loc_storage:
                show storage at left
                screen storage:
                    fixed:
                        vbox xalign 0.0 yalign 1.0:
                            text _('Кладовка спорт инвентаря. В ней находятся мячи, маты, козлы и прочий спортинвентарь. Многие ученики  ходят сюда, чтобы немного отдохнуть и уединиться ото всех.') style style.description
                        textbutton _('Спортзал') xalign 0.5 yalign 0.8 action Function(move, 'loc_gym') style "navigation_button" text_style "navigation_button_text"
                call screen storage

        label loc_firstFloor:
            show firstFloor at left
            screen firstFloor:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Коридор первого этажа. Тут находится Ваш офис, а так же первые три классных кабинета: Кабинет химии, кабинет биологии и класс уроков Секспросвета. Вы видите лестницу на второй этаж и в холл.') style style.description
                    textbutton _('Ваш офис') xalign 0.2 yalign 0.8 action Function(move, 'loc_office') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Класс 1') xalign 0.25 yalign 0.7 action Function(move, 'loc_class1') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Класс 2') xalign 0.3 yalign 0.6 action Function(move, 'loc_class2') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Класс 3') xalign 0.35 yalign 0.5 action Function(move, 'loc_class3') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Второй\nэтаж') xalign 0.37 yalign 0.35 action Function(move, 'loc_secondFloor') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Холл') xalign 0.6 yalign 0.8 action Function(move, 'loc_hall') style "navigation_button" text_style "navigation_button_text"
            call screen firstFloor
            
        label loc_office:
            show office at left
            screen office:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Ваш офис. Большой дубовый стол, компьютер, сразу видно что Вы здесь уважаемы.') style style.description
                    textbutton _('Первый этаж') xalign 0.8 yalign 0.8 action Function(move, 'loc_firstFloor') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Воспользоваться\nокном') xalign 0.2 yalign 0.3 action Function(move, 'loc_entrance') style "navigation_button" text_style "navigation_button_text"
            call screen office

        label loc_class1:
            show class1 at left
            screen class1:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Кабинет Химии. Тут обычно преподаёт Валентина Купрувна. Весь учительский стол завален всякими колбами и ретортами. В стороне даже приютилась пара баночек для анализов.') style style.description
                    textbutton 'Первый этаж' xalign 0.8 yalign 0.8 action Function(move, 'loc_firstFloor') style "navigation_button" text_style "navigation_button_text"
            call screen class1
            
        label loc_class2:
            show class2 at left
            screen class2:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Кабинет Биологии. Тут обычно преподаёт Полина Данокова.') style style.description
                    textbutton _('Первый этаж') xalign 0.8 yalign 0.8 action Function(move, 'loc_firstFloor') style "navigation_button" text_style "navigation_button_text"
            call screen class2
            
        label loc_class3:
            show class3 at left
            screen class3:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Кабинет Секспросвета. Тут обычно преподаёт Ангелина Фригидовна. Студентов заставляют заниматься в этом классе в случае провинности.') style style.description
                    textbutton _('Первый этаж') xalign 0.8 yalign 0.8 action Function(move, 'loc_firstFloor') style "navigation_button" text_style "navigation_button_text"
            call screen class3
            
        label loc_class4:
            show class4 at left
            screen class4:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Кабинет Математики. Тут обычно преподаёт Валентина Биссектрисовна. У доски стоит здоровенная учительская тумба, в которой хранятся разные мелки, тряпки и прочая дребедень. Прикинув, Вы понимаете, что такая тумба вместит даже небольшого человека. Только зачем бы там кому то прятаться?') style style.description
                    textbutton _('Второй этаж') xalign 0.2 yalign 0.8 action Function(move, 'loc_secondFloor') style "navigation_button" text_style "navigation_button_text"
            call screen class4
            
        label loc_class5:
            show class5 at left
            screen class5:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Кабинет Английского языка. Тут обычно преподаёт Анжела Диковна.') style style.description
                    textbutton _('Второй этаж') xalign 0.2 yalign 0.8 action Function(move, 'loc_secondFloor') style "navigation_button" text_style "navigation_button_text"
            call screen class5
            
        label loc_secondFloor:
            show secondFloor at left
            screen secondFloor:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Из этого коридора Вы видите оставшиеся два класса, класс математики и класс английского языка. А так же учительскую и лестницу на первый этаж.') style style.description
                        text _('В конце коридора расположены туалеты для мальчиков и девочек.') style style.description
                    textbutton 'Класс 4' xalign 0.7 yalign 0.6 action Function(move, 'loc_class4') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Класс 5') xalign 0.3 yalign 0.3 action Function(move, 'loc_class5') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Учительская') xalign 0.05 yalign 0.4 action Function(move, 'loc_teacherRoom') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Дверь с М') xalign 0.2 yalign 0.2 action Function(move, 'loc_wcm') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Дверь с Ж') xalign 0.2 yalign 0.25 action Function(move, 'loc_wcf') style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Первый этаж') xalign 0.6 yalign 0.8 action Function(move, 'loc_firstFloor') style "navigation_button" text_style "navigation_button_text"
            call screen secondFloor
            
        label loc_teacherRoom:
            show teacherRoom at left
            screen teacherRoom:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Тут обычно проходят кофе-брейки учителей, а так же различные совещания. А ещё, у Вас тут частенько будут вымогать деньги на нужды школы.') style style.description
                    textbutton _('Второй этаж') xalign 0.8 yalign 0.8 action Function(move, 'loc_secondFloor') style "navigation_button" text_style "navigation_button_text"
            call screen teacherRoom
            
        label loc_wcm:
            show wcm at left
            screen wcm:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Мужской туалет. Писсуары явно говорят об этом. Вам здесь нечего делать. Будет неприятно, если Вас здесь застукают.') style style.description
                    textbutton _('Второй этаж') xalign 0.2 yalign 0.8 action Function(move, 'loc_secondFloor') style "navigation_button" text_style "navigation_button_text"
            call screen wcm
            
        label loc_wcf:
            show wcf at left
            screen wcf:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Женский туалет. Очень миленький. Справа есть умывальник. С зеркалом.') style style.description
                    textbutton _('Первый этаж') xalign 0.2 yalign 0.8 action Function(move, 'loc_secondFloor') style "navigation_button" text_style "navigation_button_text"
            call screen wcf

##############################################################
# OTHER
##############################################################
label loc_street:
    show street
    screen street:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text _('Простая улица на которой стоит Ваш дом. Вдоль улицы стоят другие дома ваших соседей. Кто знает, может быть где то по соседству живёт кто то из вашей школы?".') style style.description
                text _('Улица пересекает почти весь небольшой городок, и в конце упирается в улицу "Торговая".') style style.description
                if hour >= 5 and hour <= 20: 
                     text _('Посмотрев вдоль, Вы видите пару бегущих людей. Действительно, улица чрезвычайно удобна для пробежек.') style style.description
                else:
                     text _('Посмотрев вдоль, Вы больше не видите бегущих людей. Наверное убежали. Или же просто ночь наступила?') style style.description
            textbutton _('Домой') xalign 0.2 yalign 0.3 action Function(move, 'loc_home') style "navigation_button" text_style "navigation_button_text"
            textbutton _('Пляж') xalign 0.7 yalign 0.8 action [Function(changetime, 30),Function(move, 'loc_beach')] style "navigation_button" text_style "navigation_button_text"
            textbutton _('Торговая улица') xalign 0.35 yalign 0.3 action [Function(changetime, 15),Function(move, 'loc_shopStreet')] style "navigation_button" text_style "navigation_button_text"
            textbutton _('Школа') xalign 0.5 yalign 0.8 action [Function(changetime, 30),Function(move, 'loc_entrance')] style "navigation_button" text_style "navigation_button_text"
    call screen street
    
    label loc_beach:
        show beach at left
        screen beach:
            fixed:
                vbox xalign 0.0 yalign 1.0:
                    text _('Пляж, просто пляж. На нём можно неплохо загореть, если уделить этому недельку времени, или же просто искупаться.') style style.description
                textbutton _('К дому') xalign 0.5 yalign 0.8 action [Function(changetime, 30),Function(move, 'loc_street')] style "navigation_button" text_style "navigation_button_text"
                textbutton _('Раздевалка') xalign 0.7 yalign 0.45 action Function(move, 'loc_beachChange') style "navigation_button" text_style "navigation_button_text"
        call screen beach
        
        label loc_beachChange:
            show beachChange at left
            screen beachChange:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Специально обустроенные комнатки для переодеваний. Внутри небольшая полочка для вещей, умывальник и полотенце. Очень удобно, хотя и необычно.') style style.description
                    textbutton _('Пляж') xalign 0.5 yalign 0.8 action Function(move, 'loc_beach') style "navigation_button" text_style "navigation_button_text"
            call screen beachChange
            
    
        
    label loc_shopStreet:
        show shopStreet at left
        screen shopStreet:
            fixed:
                vbox xalign 0.0 yalign 1.0:
                    text _('Торговая улица! На ней много всяких маленьких магазинчиков, в которых закупается весь город. Говорят, что в некоторых странах Есть ОГРОМНЫЕ магазины, в которых есть ВСЁ. Но это как то бездушно. Зачем тебе это всё, когда души то нет?') style style.description
                    text _('Мини маркет работает круглосуточно.') style style.description
                    text _('Салон красоты работает с 8 до 19 ежедневно.') style style.description
                textbutton _('К дому') xalign 0.5 yalign 0.8 action [Function(changetime, 15),Function(move, 'loc_street')] style "navigation_button" text_style "navigation_button_text"
                textbutton _('Магазин') xalign 0.4 yalign 0.5 action [Function(move, 'loc_shop')] style "navigation_button" text_style "navigation_button_text"
                if hour >=8 and hour <= 19: 
                    textbutton _('Салон\nКрасоты') xalign 0.2 yalign 0.55 action [Function(move, 'loc_shopBeauty')] style "navigation_button" text_style "navigation_button_text"
                    textbutton _('Сексшоп') xalign 0.65 yalign 0.45 action [Function(move, 'loc_sexShop')] style "navigation_button" text_style "navigation_button_text"
        call screen shopStreet
        

        label loc_shop:
            show shop at left
            screen shop:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Круглосуточный магазин, единственный в Вашем районе. После прогулки в нем Вы сможете без промедления набрать еды на кухню, выбрать себе напитки напитки и некоторые иные вещи.') style style.description
                    textbutton _('Назад') xalign 0.5 yalign 0.8 action [Function(move, 'loc_shopStreet')] style "navigation_button" text_style "navigation_button_text"
            call screen shop
            
            
        label loc_shopBeauty:
            show shopBeauty at left
            screen shopBeauty:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text _('Салон красоты приветствует Вас чистым полом и ярким рецепшеном. Наверняка тут предлагают великолепные по качеству услуги для улучшения внешности, если природа Вас обделила. Хотя и прирождённым красавицам они безусловно тоже помогут стать ещё красивее. Вот только цена, не отпугнёт ли она случайного клиента?') style style.description
                    textbutton _('Назад') xalign 0.5 yalign 0.8 action [Function(move, 'loc_shopStreet')] style "navigation_button" text_style "navigation_button_text"
            call screen shopBeauty
            
            
        label loc_sexShop:
                show sexShop at left
                screen sexShop:
                    fixed:
                        vbox xalign 0.0 yalign 1.0:
                            text _('Вы видите перед собой магазин для взрослых. Полки уставлены различными игрушками для взрослых. Дилдо, вибраторы, резиновые дырки для мальчиков, пони с уникальным седлом для девочек. Отдельная полка для афродизиаков и прочей медицины. Глаза прямо разбегаются от обилия выбора!') style style.description
                        textbutton _('Назад') xalign 0.5 yalign 0.8 action [Function(move, 'loc_shopStreet')] style "navigation_button" text_style "navigation_button_text"
                call screen sexShop
