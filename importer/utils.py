# coding=utf-8

class ImporterUtils():

    def __init__(self):
        pass

    @staticmethod
    def program_categories_for_prijepolje():
        programs = {
            "Програмска активност 0001-Функционисање локалне самоуправе": ["Извршни и законодавни органи", "Извршни и законодавни   орган"],
            "Прогрмска активн.0001-Функционисање локалне самоуправе": ["Извршни и законодавни органи"],
            "КАНЦЕЛАРИЈА ЗА МЛАДЕ": ["Програмска актив.0007-Канцеларија за младе"],
            "ОПШТИНСКА  УПРАВА ПРОГРАМ 15-ЛОКАЛНА САМОУПРАВА": ["Програмска активност 0001-Функционисање локалне самоуправе", "Програмска активност 0008-Програми националних мањина"],
            "ОСНОВНО ОБРАЗОВАЊЕ ПРОГРАМ 9": ["Програмска активност-Функционисање основних школа"],
            "СРЕДЊЕ ОБРАЗОВАЊЕ ПРОГРАМ 10": ["Програмска активност-Функц.средњих школа"],
            "ДОМ   КУЛТУРЕ ПРОГРАМ 13-РАЗВОЈ КУЛТУРЕ": ["Програмска активност 0001-Функционисање локалних установа културе"],
            "МАТИЧНА  БИБЛИОТЕКА ПРОГРАМ 13-РАЗВОЈ КУЛТУРЕ": ["Програмска активност 0001-Функционисање локалних установа културе"],
            " М  У  З  Е  Ј  ПРОГРАМ 13-РАЗВОЈ КУЛТУРЕ": ["Програмска активност 0001-Функционисање локалних установа културе"],
            "ИСТОРИЈСКИ АРХИВ ПРОГРАМ 13-РАЗВОЈ КУЛТУРЕ": ["Функционисање локалних установа културе"],
            "ДЕЧЈИ  ВРТИЋ ПРОГРАМ 8-ПРЕДШК.ВАСП.": ["Програмска активност 0001-Функц.предш.установа"],
            "ЦЕНТАР ЗА СОЦ.РАД ПРОГРАМ 11-СОЦ.И ДЕЧ.ЗАШТИТА": ["Програмска активност-Социјалне помоћи"],
            "РАЗВОЈ ЗАЈЕДНИЦЕ ПРОГРАМ 3-ЛОКАЛНИ ЕКОНОМСКИ РАЗВОЈ": ["Програмска активност 0002-Унапређење привредног амбијента"],
            "МЕСНЕ ЗАЈЕДНИЦЕ": ["Програмска активност 0002-Месне Заједнице "],
            "ЈАВНИ РЕД И БЕЗБЕДНОСТ ПРОГРАМ 15-ФУНКЦИОНИСАЊЕ ЛОК. САМОУПРАВЕ": ["Програмска активност 0001-Функ.ЛС"],
            "ДИРЕКЦИЈА ЗА ИЗГРАДЊУ ПРОГРАМ 1-ЛОКАЛНИ РАЗВОЈ И ПРОСТОРНО ПЛАНИРАЊЕ": ["Програмска активност 0002-Уређивање грађ.земљишта"],
            "ДИРЕКЦИЈА ЗА ИЗГРАДЊУ ПРОГРАМ 7-ПУТНА ИНФРАСТРУКТУРА": ["Програмска активност 0002-Одржавање путева"],
            "KOMУНАЛНА ДЕЛАТНОСТ ПРОГРАМ 2- КОМУНАЛНА ДЕЛАТНОСТ": [
                "Програмска активност 0008-Јавна хигијена",
                "Програмска активност 0004-Даљинско грејање",
                "Програмска активност 0003 -Одржавање депонија",
                "Програмска активност 0009-Уређење и одржавање зеленила"
            ],
            "ЗАШТИТА ЖИВОТНЕ СРЕДИНЕ ПРОГРАМ 6": ["Програмска активност 0004-Заштита природних вредности и унапређење подручја са природним свост"],
            "JAВНА   РАСВЕТА ПРОГРАМ 2-КОМУНАЛНА ДЕЛАТНОСТ": ["Програмска активност 0010-Јавна расвета"],
            "ЛОКАЛНИ  ПРЕВОЗ ПРОГРАМ 2-КОМУНАЛНА ДЕЛАТНОСТ": ["Програмска активност 0005-Јавни превоз"],
            "ИНФОРМИСАЊЕ ПРОГРАМ 15-ЛОКАЛНАСАМОУПРАВА": ["Програмска активност 0006-Информисање"],
            "ТУРИСТИЧКА ОРГАНИЗАЦИЈА ПРОГРАМ 4-РАЗВОЈ РАЗВОЈ ТУРИЗМА": ["Програмска активност 0002-Туристичка промоција"],
            "ЗАШТИТА    ЖИВОТНЕ   СРЕДИНЕ ПРОГРАМ 6": ["Програмска активност 0001-Управљање заштитом животне сред. И природних вред."],
            "РАЗВОЈ ПОЉОПРИВРЕДЕ ПРОГРАМ 5": ["Програмска активност-0002- Подстицаји пољ.произв."],
            "РАЗВОЈ СПОРТА И ОМЛАДИНЕ ПРОГРАМ 14 ":["ПА-Подршка л.с.о.у.и с."],
            "ДОМ ЗДРАВЉА ПРОГРАМ 12-ПРИМАРНА ЗДРАВСТВЕНА ЗАШТИТА": ["ПА 0001-Функцион.установа примарне здрав.заштите"],
            "СОЦ.И ДЕЧИЈА ЗАШТИТА ПРОГРАМ 11 ": ["Програмска активност Дечија заштита"],
            "ЦРВЕНИ  КРСТ ПРОГРАМ 11-СОЦИЈАЛНА И ДЕЧИЈА ЗАШТИТА": ["ПА 0005-Активности Црвеног крста"]

        }
        return programs

    @staticmethod
    def parent_categories_for_vranje():
        valjevo_parents = {
            "41": "РАСХОДИ ЗА ЗАПОСЛЕНЕ",
            "42": "КОРИШЋЕЊЕ РОБА И УСЛУГА",
            "44": "НЕГ. КУРС.РАЗЛИКЕ",
            "45": "СУБВЕНЦИЈЕ",
            "46": "ДОТАЦИЈЕ ИЗ БУЏЕТА",
            "47": "СОЦИЈАЛНЕ ПОМОЋИ",
            "48": "ОСТАЛИ РАСХОДИ",
            "49": "РЕЗЕРВЕ",
            "51": "ОСНОВНА СРЕДСТВА У ИЗГРАДЊИ"
        }

        return valjevo_parents


    @staticmethod
    def program_categories_for_vranje():
        vranje_programs = {
            "ПРОГРАМ 15: ЛОКАЛНА САМОУПРАВА": [
                "Програмска активност: Функционисање локалне самоуправе и градских општина",
                "Пројекат: Прослава Дана особођења Града и државних празника",
                "Програмска активност: Управљање јавним дугом",
                "Програмска активност: Информисање",
                "Програмска активност: Програми националних мањина",
                "Програмска активност: Заштитник грађана",
            ],
            "ПРОГРАМ 1: ЛОКАЛНИ РАЗВОЈ И ПРОСТОРНО ПЛАНИРАЊЕ": [
                "Пројекат: Експропријација земљишта за потребе Фабрике за прераду отпадних вода и заобилазнице до индустријске зоне Бунушевац",
                "Програмска активност: Стратешко, просторно и урбанистичко планирање",
                "Партерно уређење платоа у Врањској Бањи",
                "Програмска активност: Уређивање грађевинског земљишта",
                "Пројекат : Реконструкција шеталишта у улици Краља Стефана Првовенчаног од Робне куће до зграде ЈП Дирекције",
            ],
            "ПРОГРАМ 3: ЛОКАЛНИ ЕКОНОМСКИ РАЗВОЈ": [
                "Програмска активност: Унапређење привредног амбијента",
                "Програмска активност: Подстицаји за развој предузетништва",
                "Програмска активност: Одржавање економске инфраструктуре",
                "Програмска активност: Финансијска подршка локалном економском развоју",
                "Пројекат: Стручна пракса 2015",
            ],
            "ПРОГРАМ 7 - ПУТНА ИНФРАСТРУКТУРА": [
                "Пројекат: Увођење видео надзора у центру Града",
                "Програмска активност: Управљање саобраћајном инфраструктуром",
                "Програмска активност: Одржавање путева",
                "Пројекат: Периодично одржавање путева  Златокоп -Ћуковац-Врањска Бања и Бунушевац-Содерце, Миланово-Буштрање",
            ],
            "ПРОГРАМ 11: СОЦИЈАЛНА И ДЕЧЈА ЗАШТИТА": [
                "Програмска активност: Социјалне помоћи",
                "Програмска активност: Подршка социо-хуманитарним организацијама",
                "Програмска активност: Активности Црвеног крста",
                "Пројектат: Смањење сиромаштва и унапређење могућности запошљавања маргинализованих и угрожених група становништва са фокусом на ресоцијализацију осуђеника",
                "Пројекат: Смањење сиромаштва и унапређење могућности запошљавања маргинализованих и угрожених група становништва са фокусом на Ромкиње у Србији",
                "Пројекат: Изградња монтажних објеката за трајно решавање смештаја избелих и расељених лица",
                "Програмска активност: Прихватилишта, прихватне станице и друге врсте смештаја"
            ],
            "ПРОГРАМ 12: ПРИМАРНА ЗДРАВСТВЕНА ЗАШТИТА": [
                "Програмска активност: Функционисање установа примарне здравствене заштите",
                "Пројекат: Суфинансирање вантелесне оплодње"
            ],
            "ПРОГРАМ 14 - РАЗВОЈ СПОРТА И ОМЛАДИНЕ": [
                "Програмска активност: Подршка локалним спортским организацијама, удружењима и савезима",
                "Програмска активност: Подршка предшколском, школском и рекреативном спорту и масовној физичкој култури",
                "Програмска активност: Одржавање спортске инфраструктуре"
            ],

            "ПРОГРАМ 15 - ЛОКАЛНА САМОУПРАВА":[
                "Функционисање локалне самоуправе и градских општина",
                "Пројекат: Градска слава - Света Тројица",
                "Програмска активност: Општинско јавно правобранилаштво",
                "Програмска активност: Функционисање локалне самоуправе и градских општина",
                "СКУПШТИНА ОПШТИНЕ",
                "ПРЕДСЕДНИК ОПШТИНЕ И ОПШТИНСКО ВЕЋЕ",
                "ОПШТИНСКА УПРАВНА ЈЕДИНИЦА",
                "УПРАВА БАЊЕ",
                "Друмски саобраћај",
                "Изградња Балон сале - завршетак I и II фаза",
                "Уређивање и одржавање зеленила",
                "Уређење водотокова",
                "Екпропријација и припремање грађевинског земљишта",
                "Изградња канализационе мреже",
                "Улична расвета",
                "Програмска активност: Месне заједнице",
                "Програмска активност: Канцеларија за младе"
            ],
            "ПРОГРАМ 2: КОМУНАЛНЕ ДЕЛАТНОСТИ":[
                "Програмска активност: Јавна расвета",
                "Програмска активност: Водоснабдевање",
                "Програмска активност: Управљање отпадним водама",
                'Пројекат: "ESCO" пројекат побољшања енергетског учинка јавне расвете',
            ],
            "ПРОГРАМ 7: ПУТНА ИНФРАСТРУКТУРА":[
                "Програмска активност: Одржавање путева",
                "Пројекат: Асфалтирање путева у сеоским МЗ",
                "Програмска активност: Управљање саобраћајном инфраструктуром",
            ],
            "ПРОГРАМ 5: РАЗВОЈ ПОЉОПРИВРЕДЕ": [
                "Програмска активност: Унапређење  услова за пољопривредну делатност",
            ],
            "ПРОГРАМ 6: ЗАШТИТА ЖИВОТНЕ СРЕДИНЕ": [
                "Програмска активност: Управљање заштитом животне средине и природних вредности",
                "Програмска активност: Праћење квалитета елемената животне средине",
                "Пројекат: Набавка контејнера за изношење смећа",
                'Пројекат: Изградња санитарног контејнера и биолошког пречишћивача отпадних вода у насељу "Цигански рид" у Врању',
                "Пројекат: Набавка уличних канти за отпатке и бетонских мобилијера",
                "Пројекат: Озелењавање јавних површина",
                "Пројекат: Набавка камиона аутосмећара",
                "Пројекат: Очување животне средине уређењем отпадних вода",
                "Пројекат: Компостно поље",
            ],
            "ПРОГРАМ 4 - РАЗВОЈ ТУРИЗМА":[
                "Програмска активност: Управљањем развојем туризма",
                "Дани Врања и Дани Врања у Београду",
                "Прослава Дана Града",
                "Програмска активност: Туристичка промоција",
                "Пројекат: Доградња планинарског дома",
                "Пројекат: Уградња соларних панела",
                "Пројекат: Изградња платоа испред планинарског дома",
                "Пројекат: Постављање жичаре Дубока 2"
            ],
            "ПРОГРАМ 2 - КОМУНАЛНА ДЕЛАТНОСТ": [
                "Програмска активност: Водоснабдевање",
                "Програмска активност: Управљање отпадним водама",
                "Програмска активност: Паркинг сервис",
                "Програмска активност: Уређење, одржавање и коришћење пијаца",
                "Програмска активност: Уређење и одржавање зеленила",
                "Програмска активност: Јавна расвета",
                "Програмска активност: Одржавање гробаља, и погребне услуге",
            ],
            "ПРОГРАМ 13 - РАЗВОЈ КУЛТУРЕ": [
                "Програмска активност: Подстицаји културном и уметничком стваралаштву",
                "Програмска активност: Функционисање локалних установа културе",
                "Пројекат: '35. Борини позоришни дани'",
                "Пројекат: Изградња и опремање зграде Позоришта",
                "Пројекат: Светосавска недеља 2016",
                "Програм социјалне укључености лица са инвалидитетом,  посебним потребама  и  радно способних лица",
                "Пројекат: Еколошки кутак и еколошка едукација",
                "Пројекат: Набавка архивских кутија",
                'Манифестација "Златни пуж 2015."'
            ],
            "ПРОГРАМ 8 - ПРЕДШКОЛСКО ОБРАЗОВАЊЕ": [
                "Програмска активност: Функционисање предшколских установа",
                'Пројекат: Санација отворене терасе на вртићу "Чаролија"',
            ],
            "ПРОГРАМ 9 - ОСНОВНО ОБРАЗОВАЊЕ": [
                "Програмска активност: Функционисање основних школа",
                "Пројекат: Поправка инсталације грејања, котла и димњака у ОШ 20. октобар Власе",
                "Пројекат: Санирање и опремање школске кухиње ЈЈ Змај",
                "Пројекат: Реконструкција санитарног чвора у ОШ 20. октобар Власе и ОШ Предраг Девеџић Врањска Бања",
                "Програмска активност: Функционисање средњих школа",
                "Пројекат: Санирање школских спортских терена и сала",
                'Пројекат: Изградња система за наводњавање локалним квашењем земљишта школског имања "Златокоп" Пољопривредно-ветеринарске школе',
            ],
            "ПРОГРАМ 14: РАЗВОЈ СПОРТА И ОМЛАДИНЕ": [
                "Пројекат: Изградња спортских терена на Бесној Кобили",
                "Програмска активност: Додатно образовање и усавршавање омладине",
                "Пројекат: Летња школа за најбоље полазнике РЦТ на Бесној Кобили",
                "Пројекат: Организовање Регионалне смотре талената",
            ],
            "ПРОГРАМ 10 - СРЕДЊЕ ОБРАЗОВАЊЕ": [
                "Програмска активност: Функционисање средњих школа",
                "Пројекат: Санирање школских спортских терена и сала",
                'Пројекат: Изградња система за наводњавање локалним квашењем земљишта школског имања "Златокоп" Пољопривредно-ветеринарске школе',
            ]
        }
        return vranje_programs

    @staticmethod
    def sombor_programs():
        descriptions = {
            "ПРОГРАМ 15 - ЛОКАЛНА САМОУПРАВА": [
                "Функционисање локалне самоуправе и градских општина",
                "Информисање",
                "Градско (општинско) јавно правобранилаштво",
                "Информисање",
                "Програми националних мањина",
                "Канцеларија за младе",
                "Управљање јавним дугом",
                "Месне заједнице",
                "МЗ ''АЛЕКСА ШАНТИЋ''",
                "МЗ ''БАЧКИ БРЕГ''",
                "МЗ ''БАЧКИ МОНОШТОР''",
                "МЗ 'БЕЗДАН''",
                "МЗ 'ДОРОСЛОВО''",
                "МЗ ''ГАКОВО''",
                "МЗ ''КЉАЈИЋЕВО''",
                "МЗ ''КОЛУТ''",
                "МЗ ''РАСТИНА''",
                "МЗ ''РИЂИЦА''",
                "МЗ ''СВЕТОЗАР МИЛЕТИЋ''",
                "МЗ ''СТАНИШИЋ''",
                "МЗ ''СТАПАР''",
                "МЗ ''ТЕЛЕЧКА''",
                "МЗ ''ЧОНОПЉА''",
                "МЗ ''ВЕНАЦ''",
                "МЗ ''СЕЛЕНЧА''",
                "МЗ ''ГОРЊА ВАРОШ''",
                "МЗ ''СТАРА СЕЛЕНЧА''",
                "МЗ ''МЛАКЕ''",
                "МЗ ''ЦРВЕНКА''",
                "МЗ ''НОВА СЕЛЕНЧА ''"
            ],
            "ПРОГРАМ 2 - КОМУНАЛНА ДЕЛАТНОСТ": [
                "Остале комуналне услуге", "Водоснабдевање"
            ],
            "ПРОГРАМ 6 - ЗАШТИТА ЖИВОТНЕ СРЕДИНЕ": [
                "Управљање заштитом животне средине и природних вредности",
                "Праћење квалитета елемената животне средине",
                "Остале комуналне услуге",
                "Паркинг сервис",
                "Даљинско грејање",
                "Остале комуналне услуге",
                "Одржавање депонија",
                "Јавна хигијена",
                "Уређење и одржавање зеленила",
                "Јавна расвета",
                "Одржавање гробаља",
                "Остале комуналне услуге",
                ""
            ],
            "ПРОГРАМ 7 - ПУТНА ИНФРАСТРУКТУРА": [
                "Одржавање путева",
                ""
            ],
            "ПРОГРАМ 1 - ЛОКАЛНИ РАЗВОЈ И ПРОСТОРНО ПЛАНИРАЊЕ": [
                "Стратешко, просторно и урбанистичко планирање",
                ""
            ],
            "ПРОГРАМ 11 - СОЦИЈАЛНА И ДЕЧИЈА ЗАШТИТА": [
                "Социјалне помоћи",
                "Прихватилишта, прихватне станице и др.врсте смештаја",
                "Саветодавно-терапијске и социјално-едукативне услуге",
                "Социјалне помоћи",
                "Прихватилипта, прихватне станице и др.врсте смештаја",
                "Подршка социјално хуманитарним организацијама",
                "Саветодавно-терапијске и социјално-едукативне услуге",
                "Активности Црвеног крста",
                "Дечија заштита"
            ],
            "ПРОГРАМ 13 - РАЗВОЈ КУЛТУРЕ": [
                "Функционисање локалних установа културе",
                "Библиотека ''КАРЛО БИЈЕЛИЦКИ'' Сомбор",
                "НАРОДНО ПОЗОРИШТЕ Сомбор",
                "ГРАДСКИ МУЗЕЈ Сомбор",
                "КУЛТУРНИ ЦЕНТАР ''ЛАЗА КОСТИЋ'' Сомбор",
                "ИСТОРИЈСКИ АРХИВ Сомбор",
                "Галерија ''МИЛАН КОЊОВИЋ'' Сомбор",
                "Подстицаји културном и уметничком стваралаштву",

            ],
            "ПРОГРАМ 14 - РАЗВОЈ СПОРТА И ОМЛАДИНЕ": [
                "",
                'Спортски центар ''СОКО'' Сомбор',
                'Средства за спортске активности'
            ],
            "ПРОГРАМ 8 - ПРЕДШКОЛСКО ОБРАЗОВАЊЕ": [
                "Функционисање предшколских установа"
            ],
            "ПРОГРАМ 9 - ОСНОВНО ОБРАЗОВАЊЕ": [
                "Функционисање основних школа",
                "ОШ ''АВРАМ МРАЗОВИЋ'' СОМБОР",
                "ОШ ''БРАТСТВО-ЈЕДИНСТВО'' СОМБОР",
                "ОШ ''ДОСИТЕЈ ОБРАДОВИЋ'' СОМБОР",
                "ОШ ''ИВО ЛОЛА РИБАР'' СОМБОР",
                "ОШ ''НИКОЛА ВУКИЋЕВИЋ'' СОМБОР",
                "ОШ ''АЛЕКСА ШАНТИЋ'' АЛЕКСА ШАНТИЋ",
                "ОШ ''22.ОКТОБАР'' БАЧКИ МОНОШТОР",
                "ОШ ''МОША ПИЈАДЕ'' БАЧКИ БРЕГ",
                "ОШ ''ЛАЗА КОСТИЋ'' ГАКОВО",
                "ОШ ''ПЕТЕФИ ШАНДОР'' ДОРОСЛОВО",
                "ОШ ''БРАТСТВО-ЈЕДИНСТВО'' БЕЗДАН",
                "ОШ ''НИКОЛА ТЕСЛА'' КЉАЈИЋЕВО",
                "ОШ ''ОГЊЕН ПРИЦА'' КОЛУТ",
                "ОШ ''НИКОЛА ТЕСЛА'' КЉАЈИЋЕВО",
                "ОШ ''ОГЊЕН ПРИЦА'' КОЛУТ",
                "ОШ ''ПЕТАР КОЧИЋ'' РИЂИЦА",
                "ОШ ''БРАТСТВО-ЈЕДИНСТВО'' СВЕТОЗАР МИЛЕТИЋ",
                "ОШ ''ИВАН ГОРАН КОВАЧИЋ'' СТАНИШИЋ",
                "ОШ ''БРАНКО РАДИЧЕВИЋ'' СТАПАР",
                "ОШ ''КИШ ФЕРЕНЦ'' ТЕЛЕЧКА",
                "ОШ ''МИРОСЛАВ АНТИЋ'' ЧОНОПЉА",
                "СОШ '''ВУК КАРАЏИЋ'' СОМБОР",
                "ОСНОВНА МУЗИЧКА ШКОЛА ''ПЕТАР КОЊОВИЋ'' СОМБОР",
                'ШК.ЗА ОСНОВНО ОБРАЗ.ОДРАСЛИХ СОМБОР',
                "НАКНАДЕ ЗА ПРЕВОЗ, СМЕШТАЈ И АНГАЖОВАЊЕ ЛИЧНИХ ПРАТИЛАЦА ДЕЦЕ И УЧЕНИКА"
            ],
            "ПРОГРАМ 10 - СРЕДЊЕ ОБРАЗОВАЊЕ": [
                "Функционисање средњих школа",
                "СМШ ''ДР РУЖИЦА РИП'' СОМБОР",
                "ГИМНАЗИЈА ''ВЕЉКО ПЕТРОВИЋ'' СОМБОР",
                "СРЕДЊА ПОЉ.ПРЕХ.ШКОЛА СОМБОР",
                "СРЕДЊА ШКОЛА ''СВЕТИ САВА'' СОМБОР",
                "СРЕДЊА ЕКОНОМСКА ШКОЛА",
                "СРЕДЊА ТЕХНИЧКА ШКОЛА СОМБОР",
                "СОШ ''ВУК КАРАЏИЋ'' Сомбор",
                "СРЕДЊА МУЗИЧКА ШКОЛА СОМБОР",
                "Функционисање средњих школа",
                "Функционисање средњих школа"

            ],
            "ПРОГРАМ 12 - ПРИМАРНА ЗДРАВСТВЕНА ЗАШТИТА":[
                "Функционисање установа прим.здравствене заштите"
            ],
            "ПРОГРАМ 4 - РАЗВОЈ ТУРИЗМА": [
                "Управљање развојем туризма",
                "Туристичка промоција"
            ],
            "ПРОГРАМ 3- ЛОКАЛНИ ЕКОНОМСКИ РАЗВОЈ": [
                "Унапређење привредног амбијента",
                "Подстицаји за развој предузетништва",
                "Финансијска подршка локалном економском развоју"
            ],
            "ПРОГРАМ 5 - РАЗВОЈ ПОЉОПРИВРЕДЕ": [
                "Унапређење услова за пољопривредну делатност"
            ]
        }
        return descriptions

    @staticmethod
    def prihodi_parent_categories_for_valjevo():
        valjevo_parents = {
            "791110": "ПРИХОДИ ИЗ БУЏЕТА",
            "810000": "ПРИМАЊА ОД ПРОДАЈЕ ОСНОВНИХ СРЕДСТАВА",
            "821000": "ПРИМАЊА ОД ПРОДАЈЕ РОБНИХ РЕЗЕРВИ",
            "840000": "ПРИМАЊА ОД ПРОДАЈЕ ПРИРОДНЕ ИМОВИНЕ",
            "910000": "ПРИМАЊА ОД ЗАДУЖИВАЊА ",
            "920000": "ПРИМАЊА ОД ПРОДАЈЕ ФИН. ИМОВИНЕ"
        }

        return valjevo_parents

    @staticmethod
    def prihodi_parent_categories_for_kraljevo():
        kraljevo_parents = {
            "711000": "Порез на доходак, добит и капиталне добитке",
            "713000": "Порез на имовину",
            "714000": "Порез на добра и услуге",
            "716000": "Други порези",
            "731000": "Донације од иностраних држава",
            "732000": "Донације од међународних органзација",
            "733000": "Трансфери од других нивоа власти",
            "741000": "Приходи од имовине",
            "742000": "Приходи од продаје добара и услуга",
            "743000": "Новчане казне и одузета имовинска корист",
            "744000": "Добровољни трансфери од физичких и правних лица",
            "745000": "Мешовити и неодређени приходи",
            "771000": "Меморандумске ставке за рефундацију расхода",
            "772000": "Меморандумске ставке за рефундацију расхода из претходне године",
            "811000": "Примања од продаје непокретности",
            "812000": "Примања од продаје покретне имовине",
            "813000": "Примања од продаје осталих основних средстава",
            "841000": "Примања од продаје земљишта",
            "911000": "Примања од домаћих задужења",
            "921000": "Примања од продаје домаће финансијске имовине"
        }

        return kraljevo_parents

    @staticmethod
    def cacak_parent_catecories():

        categories = {
            "710000": [
                "1. Порески приходи",
                "1.1. Порез на доходак, добит и капиталне добитке (осим самодоприноса)",
                "1.2. Самодопринос",
                "1.3. Порез на фонд зарада",
                "1.4. Порез на имовину",
                "1.5. Порез на добра и услуге у чему:",
                "-накнаде које се користе преко Буџетског фонда за заштиту и унапређење животне средине",
                "1.6. Остали порески приходи"
            ],
            "": [
                "2. Непорески приходи у чему:",
                 "- поједине врсте прихода са одређеном наменом (наменски приходи)",
                 "6. Меморандумске ставке за рефундацију расхода",
                 "4. Издаци за набавку финансијске имовине (осим 6211)",
                "2.1.Задуживање код домаћих кредитора"
            ],
            "731+732": "3. Примања од продаје нефинансијске имовине",
            "733000": "4. Донације",
            "770000": "5. Трансфери",
            "41": [
                "1.1. Расходи за запослене",
                "1.2. Коришћење роба и услуга",
                "1.3. Употреба основних средстава",
                "1.4. Отплата камата",
                "1.5. Субвенције",
                "1.6. Социјална заштита из буџета",
                "1.7. Остали расходи, у чему:",
            ],
            "5": "2. Трансфери",
            "6200000": "3. Издаци за набавку нефинансијске имовине",
            "920000": "ПРИМАЊА ОД ПРОДАЈЕ ФИНАНСИЈСКЕ ИМОВИНЕ И ЗАДУЖИВАЊА ",
            "910000": "1. Примања по основу отплате кредита и продаје финансијске имовине",
            "611000": [
                "3.1. Отплата дуга домаћим кредиторима",
                "3.2. Отплата дуга страним кредиторима",
                "3.3. Отплата дуга по гаранцијама"
            ]
        }

        return categories
