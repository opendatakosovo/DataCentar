#coding=utf-8
import unittest
from importing_rashodi_manager import mongo

class RashodiImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass
    # Json container for each novi beograd parent category
    novi_beograd_counts_of_parents = {
        "Расходи за запослене": 7,
        "Коришћење услуга и роба": 6,
        "Донације дотације и трансфери": 2,
        "Социјално осигурање и социјална заштита": 1,
        "Остали расходи": 3,
        "Средства резерве": 2,
        "Основна средства": 3
    }

    #Json container for each vranje parent category
    vranje_counts_of_parents = {
        "РАСХОДИ ЗА ЗАПОСЛЕНЕ": 7,
        "КОРИШЋЕЊЕ РОБА И УСЛУГА": 6,
        "НЕГ. КУРС.РАЗЛИКЕ": 1,
        "СУБВЕНЦИЈЕ": 2,
        "ДОТАЦИЈЕ ИЗ БУЏЕТА": 2,
        "СОЦИЈАЛНЕ ПОМОЋИ": 1,
        "ОСТАЛИ РАСХОДИ": 5,
        "РЕЗЕРВЕ": 1,
        "ОСНОВНА СРЕДСТВА У ИЗГРАДЊИ": 6
    }
    vranje_programs = {
            "ПРОГРАМ 15: ЛОКАЛНА САМОУПРАВА": [
                ("Програмска активност: Функционисање локалне самоуправе и градских општина", 9+27),
                ("Пројекат: Прослава Дана особођења Града и државних празника", 2),
                ("Програмска активност: Управљање јавним дугом", 2),
                ("Програмска активност: Информисање", 2),
                ("Програмска активност: Програми националних мањина", 2),
                ("Програмска активност: Заштитник грађана", 7)
            ],
            "ПРОГРАМ 1: ЛОКАЛНИ РАЗВОЈ И ПРОСТОРНО ПЛАНИРАЊЕ": [
                ("Пројекат: Експропријација земљишта за потребе Фабрике за прераду отпадних вода и заобилазнице до индустријске зоне Бунушевац", 1),
                ("Програмска активност: Стратешко, просторно и урбанистичко планирање", 3),
                ("Партерно уређење платоа у Врањској Бањи", 1),
                ("Програмска активност: Уређивање грађевинског земљишта", 4+21),
                ("Пројекат : Реконструкција шеталишта у улици Краља Стефана Првовенчаног од Робне куће до зграде ЈП Дирекције", 1)
            ],
            "ПРОГРАМ 3: ЛОКАЛНИ ЕКОНОМСКИ РАЗВОЈ": [
                ("Програмска активност: Унапређење привредног амбијента", 2),
                ("Програмска активност: Подстицаји за развој предузетништва", 2),
                ("Програмска активност: Одржавање економске инфраструктуре", 1),
                ("Програмска активност: Финансијска подршка локалном економском развоју", 1),
                ("Пројекат: Стручна пракса 2015", 1)
            ],
            "ПРОГРАМ 7 - ПУТНА ИНФРАСТРУКТУРА": [
                ("Пројекат: Увођење видео надзора у центру Града", 1),
                ("Програмска активност: Управљање саобраћајном инфраструктуром", 2),
                ("Програмска активност: Одржавање путева", 2),
                ("Пројекат: Периодично одржавање путева  Златокоп -Ћуковац-Врањска Бања и Бунушевац-Содерце, Миланово-Буштрање", 1)
            ],
            "ПРОГРАМ 11: СОЦИЈАЛНА И ДЕЧЈА ЗАШТИТА": [
                ("Програмска активност: Социјалне помоћи", 3+12),
                ("Програмска активност: Подршка социо-хуманитарним организацијама", 1),
                ("Програмска активност: Активности Црвеног крста", 1),
                ("Пројектат: Смањење сиромаштва и унапређење могућности запошљавања маргинализованих и угрожених група становништва са фокусом на ресоцијализацију осуђеника", 1),
                ("Пројекат: Смањење сиромаштва и унапређење могућности запошљавања маргинализованих и угрожених група становништва са фокусом на Ромкиње у Србији", 1),
                ("Пројекат: Изградња монтажних објеката за трајно решавање смештаја избелих и расељених лица", 1),
                ("Програмска активност: Прихватилишта, прихватне станице и друге врсте смештаја", 2+15)
            ],
            "ПРОГРАМ 12: ПРИМАРНА ЗДРАВСТВЕНА ЗАШТИТА": [
                ("Програмска активност: Функционисање установа примарне здравствене заштите", 1),
                ("Пројекат: Суфинансирање вантелесне оплодње", 1)
            ],
            "ПРОГРАМ 14 - РАЗВОЈ СПОРТА И ОМЛАДИНЕ": [
                ("Програмска активност: Подршка локалним спортским организацијама, удружењима и савезима", 1),
                ("Програмска активност: Подршка предшколском, школском и рекреативном спорту и масовној физичкој култури", 1),
                ("Програмска активност: Одржавање спортске инфраструктуре", 1)
            ],

            "ПРОГРАМ 15 - ЛОКАЛНА САМОУПРАВА": [
                ("Функционисање локалне самоуправе и градских општина", 7),
                ("Пројекат: Градска слава - Света Тројица", 2),
                ("Програмска активност: Општинско јавно правобранилаштво", 12),
                ("Програмска активност: Функционисање локалне самоуправе и градских општина", 0),
                ("СКУПШТИНА ОПШТИНЕ", 6),
                ("ПРЕДСЕДНИК ОПШТИНЕ И ОПШТИНСКО ВЕЋЕ", 5),
                ("ОПШТИНСКА УПРАВНА ЈЕДИНИЦА", 17),
                ("УПРАВА БАЊЕ", 18),
                ("Друмски саобраћај", 4),
                ("Изградња Балон сале - завршетак I и II фаза", 1),
                ("Уређивање и одржавање зеленила", 2),
                ("Уређење водотокова", 4),
                ("Екпропријација и припремање грађевинског земљишта", 2),
                ("Изградња канализационе мреже", 1),
                ("Улична расвета", 7),
                ("Програмска активност: Месне заједнице", 4),
                ("Програмска активност: Канцеларија за младе", 2)
            ],
            "ПРОГРАМ 2: КОМУНАЛНЕ ДЕЛАТНОСТИ": [
                ("Програмска активност: Јавна расвета", 4),
                ("Програмска активност: Водоснабдевање", 2),
                ("Програмска активност: Управљање отпадним водама", 2),
                ('Пројекат: "ESCO" пројекат побољшања енергетског учинка јавне расвете', 1)
            ],
            "ПРОГРАМ 7: ПУТНА ИНФРАСТРУКТУРА": [
                ("Програмска активност: Одржавање путева", 3),
                ("Пројекат: Асфалтирање путева у сеоским МЗ", 1),
                ("Програмска активност: Управљање саобраћајном инфраструктуром", 3)
            ],
            "ПРОГРАМ 5: РАЗВОЈ ПОЉОПРИВРЕДЕ": [
                ("Програмска активност: Унапређење  услова за пољопривредну делатност", 5)
            ],
            "ПРОГРАМ 6: ЗАШТИТА ЖИВОТНЕ СРЕДИНЕ": [
                ("Програмска активност: Управљање заштитом животне средине и природних вредности", 5),
                ("Програмска активност: Праћење квалитета елемената животне средине", 1),
                ("Пројекат: Набавка контејнера за изношење смећа", 1),
                ('Пројекат: Изградња санитарног контејнера и биолошког пречишћивача отпадних вода у насељу "Цигански рид" у Врању', 1),
                ("Пројекат: Набавка уличних канти за отпатке и бетонских мобилијера", 1),
                ("Пројекат: Озелењавање јавних површина", 1),
                ("Пројекат: Набавка камиона аутосмећара", 1),
                ("Пројекат: Очување животне средине уређењем отпадних вода", 1),
                ("Пројекат: Компостно поље", 1)
            ],
            "ПРОГРАМ 4 - РАЗВОЈ ТУРИЗМА":[
                ("Програмска активност: Управљањем развојем туризма", 10+14),
                ("Дани Врања и Дани Врања у Београду", 2),
                ("Прослава Дана Града", 1),
                ("Програмска активност: Туристичка промоција", 4+3),
                ("Пројекат: Доградња планинарског дома", 1),
                ("Пројекат: Уградња соларних панела", 1),
                ("Пројекат: Изградња платоа испред планинарског дома", 1),
                ("Пројекат: Постављање жичаре Дубока 2", 1)
            ],
            "ПРОГРАМ 2 - КОМУНАЛНА ДЕЛАТНОСТ": [
                ("Програмска активност: Водоснабдевање", 2),
                ("Програмска активност: Управљање отпадним водама", 2),
                ("Програмска активност: Паркинг сервис", 4),
                ("Програмска активност: Уређење, одржавање и коришћење пијаца", 1),
                ("Програмска активност: Уређење и одржавање зеленила", 1),
                ("Програмска активност: Јавна расвета", 4),
                ("Програмска активност: Одржавање гробаља, и погребне услуге", 1)
            ],
            "ПРОГРАМ 13 - РАЗВОЈ КУЛТУРЕ": [
                ("Програмска активност: Подстицаји културном и уметничком стваралаштву", 2+2+5+1),
                ("Програмска активност: Функционисање локалних установа културе", 12+14+17+15+16+7),
                ('Пројекат: "35. Борини позоришни дани"', 1),
                ("Пројекат: Изградња и опремање зграде Позоришта", 2),
                ("Пројекат: Светосавска недеља 2016", 5),
                ("Програм социјалне укључености лица са инвалидитетом,  посебним потребама  и  радно способних лица", 1),
                ("Пројекат: Еколошки кутак и еколошка едукација", 2),
                ("Пројекат: Набавка архивских кутија", 1),
                ('Манифестација "Златни пуж 2015."', 4)
            ],
            "ПРОГРАМ 8 - ПРЕДШКОЛСКО ОБРАЗОВАЊЕ": [
                ("Програмска активност: Функционисање предшколских установа", 13),
                ('Пројекат: Санација отворене терасе на вртићу "Чаролија"', 1)
            ],
            "ПРОГРАМ 9 - ОСНОВНО ОБРАЗОВАЊЕ": [
                ("Програмска активност: Функционисање основних школа", 11),
                ("Пројекат: Поправка инсталације грејања, котла и димњака у ОШ 20. октобар Власе", 1),
                ("Пројекат: Санирање и опремање школске кухиње ЈЈ Змај", 5),
                ("Пројекат: Реконструкција санитарног чвора у ОШ 20. октобар Власе и ОШ Предраг Девеџић Врањска Бања", 1)
            ],
            "ПРОГРАМ 14: РАЗВОЈ СПОРТА И ОМЛАДИНЕ": [
                ("Пројекат: Изградња спортских терена на Бесној Кобили", 1),
                ("Програмска активност: Додатно образовање и усавршавање омладине", 10),
                ("Пројекат: Летња школа за најбоље полазнике РЦТ на Бесној Кобили", 3),
                ("Пројекат: Организовање Регионалне смотре талената", 2)
            ],
            "ПРОГРАМ 10 - СРЕДЊЕ ОБРАЗОВАЊЕ": [
                ("Програмска активност: Функционисање средњих школа", 9),
                ("Пројекат: Санирање школских спортских терена и сала", 1),
                ('Пројекат: Изградња система за наводњавање локалним квашењем земљишта школског имања "Златокоп" Пољопривредно-ветеринарске школе', 1)
            ]
    }

    # Json container for each zvezdara parent category
    zvezdara_counts_of_parents = {
        "РАСХОДИ ЗА ЗАПОСЛЕНЕ": 6,
        "КОРИШЋЕЊЕ РОБА И УСЛУГА": 6,
        "ОТПЛАТА КАМАТА": 1,
        "ДОНАЦИЈЕ ,ДОТАЦИЈЕ И ТРАНСФЕРИ": 2,
        "ОСНОВНА СРЕДСТВА": 3,
        "ПРАВА ИЗ СОЦИЈАЛНОГ ОСИГУРАЊА": 1,
        "ОСТАЛИ РАСХОДИ": 1,
        "Порези, таксе, казне наметнуте од власти": 3,
        "ОТПЛАТА ГЛАВНИЦЕ": 1,
        "РЕЗЕРВА": 2
    }

    # Json container for each indjia parent category
    idjia_counts_of_parents = {
        "РАСХОДИ ЗА ЗАПОСЛЕНЕ": 6,
        "КОРИШЋЕЊЕ УСЛУГА И РОБА": 6,
        "АМОРТИЗАЦИЈА И УПОТРЕБА СРЕДСТАВА ЗА РАД": 1,
        "ОТПЛАТА КАМАТА И ПРАТЕЋИ ТРОШКОВИ ЗАДУЖИВАЊА": 2,
        "СУБВЕНЦИЈЕ": 2,
        "ДОНАЦИЈЕ, ДОТАЦИЈЕ И ТРАНСФЕРИ": 3,
        "СОЦИЈАЛНО ОСИГУРАЊЕ И СОЦИЈАЛНА ЗАШТИТА": 1,
        "ОСТАЛИ РАСХОДИ": 4,
        "АДМИНИСТРАТИВНИ ТРАНСФЕРИ ИЗ БУЏЕТА И СРЕДСТВА РЕЗЕРВЕ": 1,
        "ОСНОВНА СРЕДСТВА": 4,
        "ЗАЛИХЕ": 1,
        "ПРИРОДНА ИМОВИНА": 1,
        "ОТПЛАТА ГЛАВНИЦЕ": 1,
        "НАБАВКА ФИНАНСИЈСКЕ ИМОВИНЕ": 1
    }

    # Json container for each Valjevo parent category
    valjevo_counts_of_parents = {
        "РАСХОДИ ЗА ЗАПОСЛЕНЕ": 8,
        "КОРИШЋЕЊЕ УСЛУГА И РОБА": 6,
        "УПОТРЕБА ОСНОВНИХ СРЕДСТАВА": 5,
        "ОТПЛАТА КАМАТА": 4,
        "СУБВЕНЦИЈЕ": 5,
        "ДОНАЦИЈЕ И ТРАНСФЕРИ": 6,
        "СОЦИЈАЛНА ПОМОЋ": 1,
        "ОСТАЛИ РАСХОДИ": 6,
        "АДМИНИСТРАТИВНИ ТРАНСФЕРИ БУЏЕТА": 6,
        "ОСНОВНА СРЕДСТВА": 5,
        "ЗАЛИХЕ": 4,
        "ПРИРОДНА ИМОВИНА": 3,
        "Неф. Имов. која се фин. из сред. за реализ. нип-а": 1,
        "ОТПЛАТА ГЛАВНИЦЕ": 3,
        "Набавка финансијске имовине": 1
    }

    def test_counts_for_parent_categories(self):
        # Test parent counts for municipality of Vranje
        for parent in self.vranje_counts_of_parents:
            self.asserts_for_parent_categories_elements("Vranje", parent, self.vranje_counts_of_parents[parent])

        # Test counts for municipality of Novi Beograd
        for parent in self.novi_beograd_counts_of_parents:
            self.asserts_for_parent_categories_elements("Novi Beograd", parent, self.novi_beograd_counts_of_parents[parent])

        # Test counts for municipality of Zvezdara
        for parent in self.zvezdara_counts_of_parents:
            self.asserts_for_parent_categories_elements("Zvezdara", parent, self.zvezdara_counts_of_parents[parent])

        # Test counts for municipality of Kraljevo
        self.asserts_for_parent_categories_elements("Kraljevo", "Скупштина општине", 37)

        # Test counts for municipality of Čačak
        self.asserts_for_parent_categories_elements("Čačak", "Скупштина општине", 35)

        # Test counts for municipality of Inđija
        for parent in self.idjia_counts_of_parents:
            self.asserts_for_parent_categories_elements("Inđija", parent, self.idjia_counts_of_parents[parent])

        # Test counts for municipality of Valjevo
        for parent in self.valjevo_counts_of_parents:
            self.asserts_for_parent_categories_elements("Valjevo", parent, self.valjevo_counts_of_parents[parent])

        # Test counts for municipality of Loznica
        self.asserts_for_parent_categories_elements("Loznica", "Скупштина општине", 578)

        # Test program counts for municipality of Vranje

        for program in self.vranje_programs:
            for index, sub_program in enumerate(self.vranje_programs[program]):
                self.asserts_for_sub_programs_elements("Врање", program, sub_program[0], sub_program[1])

    def asserts_for_parent_categories_elements(self, municipality, parent_category, expected_value):
        '''
        :param municipality: The municipality we want to test
        :param parent_category: The parent category of the elements we want to test
        :param expected_value: The expected value of all the elements of the related parent category
        :return:
        '''
        result = mongo.datacentar.opstine.find(
            {
                "opstina.latinica": municipality,
                "kategorijaRoditelj.opis.cirilica": parent_category
            }
        ).count()

        self.assertEqual(result, expected_value)


    """
    def asserts_for_sub_programs_elements(self, municipality, program, sub_program, expected_value):


        :param municipality:
        :param program:
        :param sub_program:
        :param expected_value:
        :return:



        result = mongo.datacentar.opstine.find(
            {
                "program.cirilica": program,
                "potProgram.cirilica": sub_program,
                "opstina.latinica": municipality
            }
        ).count()

        self.assertEqual(result, expected_value)
    """