# _*_ coding: utf_8 _*_

ALL = -1
NUM_ENTRIES = 25  # Entries per page. This is the ammount set in iRacing site. We shouldn't increase it.
WAIT_TIME = 0.3  # Minimum time in seconds between two consecutive requests to iRacing site (we don't want to flood/abuse the service). I'm not sure about the minimum value for this, I'll have to ask a dev.

IRATING_OVAL_CHART = 1
IRATING_ROAD_CHART = 2

RACE_TYPE_OVAL = 1
RACE_TYPE_ROAD = 2

LIC_ROOKIE = 1
LIC_D = 2
LIC_C = 3
LIC_B = 4
LIC_A = 5
LIC_PRO = 6
LIC_PRO_WC  = 7

SORT_IRATING = 'irating'
SORT_TIME = 'start_time'
SORT_POINTS = 'points'
ORDER_DESC  = 'desc'
ORDER_ASC = 'asc'

#OTHER
EVENT_TEST = 1
EVENT_PRACTICE = 2
EVENT_QUALY = 3
EVENT_TTRIAL = 4
EVENT_RACE = 5
EVENT_OFFICIAL = 6
EVENT_UNOFFICIAL = 7

#INCIDENT FLAGS
#these are used in the laps data
FLAG_PITTED = 2
FLAG_OFF_TRACK = 4
FLAG_BLACK_FLAG = 8
FLAG_CAR_RESET = 16
FLAG_CONTACT = 32
FLAG_CAR_CONTACT = 64
FLAG_LOST_CONTROL = 128
FLAG_DISCONTINUITY = 256
FLAG_INTERPOLATED_CROSSING = 512
FLAG_CLOCK_SMASH = 1024
FLAG_TOW = 2048

INC_FLAGS = {
    0: "clean",
    2: "pitted",
    4: "off track",
    8: "black flag",
    16: "car reset",
    32: "contact",
    64: "car contact",
    128: "lost control",
    256: "discontinuity",
    512: "interpolated crossing",
    1024: "clock smash",
    2048: "tow"
}

#initilized variables for string formatting 
custid = ''
category = ''
carid = ''
trackid = ''
seasonID = ''
subsession = ''
sessnum = ''
seasonquarter = ''
year = ''
series = ''
event = ''
unixMs = ''

#URLS
URL_IRACING_LOGIN = 'https://members.iracing.com/membersite/login.jsp'
URL_IRACING_LOGIN2 = 'https://members.iracing.com/membersite/Login'
URL_IRACING_HOME = 'https://members.iracing.com/membersite/member/Home.do'
URL_CURRENT_SERIES = 'https://members.iracing.com/membersite/member/Series.do'
URL_STATS_CHART = f'https://members.iracing.com/memberstats/member/GetChartData?custId={custid}&catId={category}&chartType=1'
URL_DRIVER_COUNTS = 'https://members.iracing.com/membersite/member/GetDriverCounts'
URL_CAREER_STATS = f'https://members.iracing.com/memberstats/member/GetCareerStats?custid={custid}'
URL_YEARLY_STATS = f'https://members.iracing.com/memberstats/member/GetYearlyStats?custid={custid}'
URL_CARS_DRIVEN = f'https://members.iracing.com/memberstats/member/GetCarsDriven?custid={custid}'
URL_PERSONAL_BEST = f'https://members.iracing.com/memberstats/member/GetPersonalBests?carid={carid}&custid={custid}'

#unable to return results utlizing var "drivername" in GetDriverStatus
#using "?friends=1&studied=1&blacklisted=1" returned results -JA
URL_DRIVER_STATUS = 'https://members.iracing.com/membersite/member/GetDriverStatus?%s'

URL_DRIVER_STATS = 'https://members.iracing.com/memberstats/member/GetDriverStats'
URL_LASTRACE_STATS = f'https://members.iracing.com/memberstats/member/GetLastRacesStats?custid={custid}'
URL_RESULTS_ARCHIVE = 'https://members.iracing.com/memberstats/member/GetResults'
URL_SEASON_STANDINGS = 'https://members.iracing.com/memberstats/member/GetSeasonStandings'
URL_SEASON_STANDINGS2 = 'https://members.iracing.com/membersite/member/statsseries.jsp'
URL_HOSTED_RESULTS = 'https://members.iracing.com/memberstats/member/GetPrivateSessionResults'
URL_SELECT_SERIES = f'https://members.iracing.com/membersite/member/SelectSeries.do?&season={seasonID}&view=undefined&nocache=%s'
URL_SESSION_TIMES = f'https://members.iracing.com/membersite/member/GetSessionTimes?season={seasonID}'#T-m-d
URL_SERIES_RACERESULTS = 'https://members.iracing.com/memberstats/member/GetSeriesRaceResults'

URL_GET_EVENTRESULTS_CSV = f'https://members.iracing.com/membersite/member/GetEventResultsAsCSV?subsessionid={subsession}&simsesnum={sessnum}&includeSummary=1'
URL_GET_EVENTRESULTS = f'https://members.iracing.com/membersite/member/EventResult.do?&subsessionid={subsession}'

URL_GET_LAPS_SINGLE = f'https://members.iracing.com/membersite/member/GetLaps?&subsessionid={subsession}&groupid={custid}&simsessnum={sessnum}'
URL_GET_LAPS_ALL = f'https://members.iracing.com/membersite/member/GetLapChart?&subsessionid={subsession}&carclassid=-1'

URL_GET_PASTSERIES = 'https://members.iracing.com/membersite/member/PreviousSeasons.do'

URL_GET_WORLDRECORD = f'https://members.iracing.com/memberstats/member/GetWorldRecords?seasonyear={year}&seasonquarter={seasonquarter}&carid={carid}&trackid={trackid}&custid={custid}&format=json&upperbound=1'

#with provided seriesID, eventType (5 for race), and unix time (in milliseconds) it returns next session ID & regcount
URL_GET_NEXTEVENT = f'https://members.iracing.com/membersite/member/GetNextEvent?seriesID={series}&evtType={event}&date={unixMs}'

HEADERS = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17'
        , 'Referer': 'https://members.iracing.com/membersite/login.jsp', 'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Cache-Control': 'max-age=0', 'Host': 'members.iracing.com','Accept-Encoding': 'gzip,deflate,sdch', 'Origin': 'members.iracing.com', 'Accept-Language': 'en-US,en;q=0.8'}


#LOCATIONS
LOC_ALL = 'null'
LOC_AFGHANISTAN = 'AF'
LOC_ALAND_ISLANDS = 'AX'
LOC_ALBANIA = 'AL'
LOC_ALGERIA = 'DZ'
LOC_AMERICAN_SAMOA = 'AS'
LOC_ANDORRA = 'AD'
LOC_ANGOLA = 'AO'
LOC_ANGUILLA = 'AI'
LOC_ANTARCTICA = 'AQ'
LOC_ANTIGUA_AND_BARBUDA = 'AG'
LOC_ARGENTINA = 'AR'
LOC_ARMENIA = 'AM'
LOC_ARUBA = 'AW'
LOC_AUSTRALIA = 'AU'
LOC_AUSTRIA = 'AT'
LOC_AZERBAIJAN = 'AZ'
LOC_BAHAMAS = 'BS'
LOC_BAHRAIN = 'BH'
LOC_BANGLADESH = 'BD'
LOC_BARBADOS = 'BB'
LOC_BELARUS = 'BY'
LOC_BELGIUM = 'BE'
LOC_BELIZE = 'BZ'
LOC_BENIN = 'BJ'
LOC_BERMUDA = 'BM'
LOC_BHUTAN = 'BT'
LOC_BOLIVIA_PLURINATIONAL_STATE_OF = 'BO'
LOC_BOSNIA_AND_HERZEGOVINA = 'BA'
LOC_BOTSWANA = 'BW'
LOC_BOUVET_ISLAND = 'BV'
LOC_BRAZIL = 'BR'
LOC_BRITISH_INDIAN_OCEAN_TERRITORY = 'IO'
LOC_BRUNEI_DARUSSALAM = 'BN'
LOC_BULGARIA = 'BG'
LOC_BURKINA_FASO = 'BF'
LOC_BURUNDI = 'BI'
LOC_CAMBODIA = 'KH'
LOC_CAMEROON = 'CM'
LOC_CANADA = 'CA'
LOC_CAPE_VERDE = 'CV'
LOC_CAYMAN_ISLANDS = 'KY'
LOC_CENTRAL_AFRICAN_REPUBLIC = 'CF'
LOC_CHAD = 'TD'
LOC_CHILE = 'CL'
LOC_CHINA = 'CN'
LOC_CHRISTMAS_ISLAND = 'CX'
LOC_COCOS_KEELING_ISLANDS = 'CC'
LOC_COLOMBIA = 'CO'
LOC_COMOROS = 'KM'
LOC_CONGO = 'CG'
LOC_CONGO_THE_DEMOCRATIC_REPUBLIC_OF_THE = 'CD'
LOC_COOK_ISLANDS = 'CK'
LOC_COSTA_RICA = 'CR'
LOC_COTE_DIVOIRE = 'CI'
LOC_CROATIA = 'HR'
LOC_CUBA = 'CU'
LOC_CYPRUS = 'CY'
LOC_CZECH_REPUBLIC = 'CZ'
LOC_DENMARK = 'DK'
LOC_DJIBOUTI = 'DJ'
LOC_DOMINICA = 'DM'
LOC_DOMINICAN_REPUBLIC = 'DO'
LOC_ECUADOR = 'EC'
LOC_EGYPT = 'EG'
LOC_EL_SALVADOR = 'SV'
LOC_EQUATORIAL_GUINEA = 'GQ'
LOC_ERITREA = 'ER'
LOC_ESTONIA = 'EE'
LOC_ETHIOPIA = 'ET'
LOC_FALKLAND_ISLANDS_MALVINAS = 'FK'
LOC_FAROE_ISLANDS = 'FO'
LOC_FIJI = 'FJ'
LOC_FINLAND = 'FI'
LOC_FRANCE = 'FR'
LOC_FRENCH_GUIANA = 'GF'
LOC_FRENCH_POLYNESIA = 'PF'
LOC_FRENCH_SOUTHERN_TERRITORIES = 'TF'
LOC_GABON = 'GA'
LOC_GAMBIA = 'GM'
LOC_GEORGIA = 'GE'
LOC_GERMANY = 'DE'
LOC_GHANA = 'GH'
LOC_GIBRALTAR = 'GI'
LOC_GREECE = 'GR'
LOC_GREENLAND = 'GL'
LOC_GRENADA = 'GD'
LOC_GUADELOUPE = 'GP'
LOC_GUAM = 'GU'
LOC_GUATEMALA = 'GT'
LOC_GUERNSEY = 'GG'
LOC_GUINEA = 'GN'
LOC_GUINEA_BISSAU = 'GW'
LOC_GUYANA = 'GY'
LOC_HAITI = 'HT'
LOC_HEARD_ISLAND_AND_MCDONALD_ISLANDS = 'HM'
LOC_HOLY_SEE_VATICAN_CITY_STATE = 'VA'
LOC_HONDURAS = 'HN'
LOC_HONG_KONG = 'HK'
LOC_HUNGARY = 'HU'
LOC_ICELAND = 'IS'
LOC_INDIA = 'IN'
LOC_INDONESIA = 'ID'
LOC_IRAN_ISLAMIC_REPUBLIC_OF = 'IR'
LOC_IRAQ = 'IQ'
LOC_IRELAND = 'IE'
LOC_ISLE_OF_MAN = 'IM'
LOC_ISRAEL = 'IL'
LOC_ITALY = 'IT'
LOC_JAMAICA = 'JM'
LOC_JAPAN = 'JP'
LOC_JERSEY = 'JE'
LOC_JORDAN = 'JO'
LOC_KAZAKHSTAN = 'KZ'
LOC_KENYA = 'KE'
LOC_KIRIBATI = 'KI'
LOC_KOREA_DEMOCRATIC_PEOPLES_REPUBLIC_OF = 'KP'
LOC_KOREA_REPUBLIC_OF = 'KR'
LOC_KUWAIT = 'KW'
LOC_KYRGYZSTAN = 'KG'
LOC_LAO_PEOPLES_DEMOCRATIC_REPUBLIC = 'LA'
LOC_LATVIA = 'LV'
LOC_LEBANON = 'LB'
LOC_LESOTHO = 'LS'
LOC_LIBERIA = 'LR'
LOC_LIBYAN_ARAB_JAMAHIRIYA = 'LY'
LOC_LIECHTENSTEIN = 'LI'
LOC_LITHUANIA = 'LT'
LOC_LUXEMBOURG = 'LU'
LOC_MACAO = 'MO'
LOC_MACEDONIA_THE_FORMER_YUGOSLAV_REPUBLIC_OF = 'MK'
LOC_MADAGASCAR = 'MG'
LOC_MALAWI = 'MW'
LOC_MALAYSIA = 'MY'
LOC_MALDIVES = 'MV'
LOC_MALI = 'ML'
LOC_MALTA = 'MT'
LOC_MARSHALL_ISLANDS = 'MH'
LOC_MARTINIQUE = 'MQ'
LOC_MAURITANIA = 'MR'
LOC_MAURITIUS = 'MU'
LOC_MAYOTTE = 'YT'
LOC_MEXICO = 'MX'
LOC_MICRONESIA_FEDERATED_STATES_OF = 'FM'
LOC_MOLDOVA_REPUBLIC_OF = 'MD'
LOC_MONACO = 'MC'
LOC_MONGOLIA = 'MN'
LOC_MONTENEGRO = 'ME'
LOC_MONTSERRAT = 'MS'
LOC_MOROCCO = 'MA'
LOC_MOZAMBIQUE = 'MZ'
LOC_MYANMAR = 'MM'
LOC_NAMIBIA = 'NA'
LOC_NAURU = 'NR'
LOC_NEPAL = 'NP'
LOC_NETHERLANDS = 'NL'
LOC_NETHERLANDS_ANTILLES = 'AN'
LOC_NEW_CALEDONIA = 'NC'
LOC_NEW_ZEALAND = 'NZ'
LOC_NICARAGUA = 'NI'
LOC_NIGER = 'NE'
LOC_NIGERIA = 'NG'
LOC_NIUE = 'NU'
LOC_NORFOLK_ISLAND = 'NF'
LOC_NORTHERN_MARIANA_ISLANDS = 'MP'
LOC_NORWAY = 'NO'
LOC_OMAN = 'OM'
LOC_PAKISTAN = 'PK'
LOC_PALAU = 'PW'
LOC_PALESTINIAN_TERRITORY_OCCUPIED = 'PS'
LOC_PANAMA = 'PA'
LOC_PAPUA_NEW_GUINEA = 'PG'
LOC_PARAGUAY = 'PY'
LOC_PERU = 'PE'
LOC_PHILIPPINES = 'PH'
LOC_PITCAIRN = 'PN'
LOC_POLAND = 'PL'
LOC_PORTUGAL = 'PT'
LOC_PUERTO_RICO = 'PR'
LOC_QATAR = 'QA'
LOC_REUNION = 'RE'
LOC_ROMANIA = 'RO'
LOC_RUSSIAN_FEDERATION = 'RU'
LOC_RWANDA = 'RW'
LOC_SAINT_BARTHELEMY = 'BL'
LOC_SAINT_HELENA_ASCENSION_AND_TRISTAN_DA_CUNHA = 'SH'
LOC_SAINT_KITTS_AND_NEVIS = 'KN'
LOC_SAINT_LUCIA = 'LC'
LOC_SAINT_MARTIN_FRENCH_PART = 'MF'
LOC_SAINT_PIERRE_AND_MIQUELON = 'PM'
LOC_SAINT_VINCENT_AND_THE_GRENADINES = 'VC'
LOC_SAMOA = 'WS'
LOC_SAN_MARINO = 'SM'
LOC_SAO_TOME_AND_PRINCIPE = 'ST'
LOC_SAUDI_ARABIA = 'SA'
LOC_SENEGAL = 'SN'
LOC_SERBIA = 'RS'
LOC_SEYCHELLES = 'SC'
LOC_SIERRA_LEONE = 'SL'
LOC_SINGAPORE = 'SG'
LOC_SLOVAKIA = 'SK'
LOC_SLOVENIA = 'SI'
LOC_SOLOMON_ISLANDS = 'SB'
LOC_SOMALIA = 'SO'
LOC_SOUTH_AFRICA = 'ZA'
LOC_SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = 'GS'
LOC_SPAIN = 'ES'
LOC_SRI_LANKA = 'LK'
LOC_SUDAN = 'SD'
LOC_SURINAME = 'SR'
LOC_SVALBARD_AND_JAN_MAYEN = 'SJ'
LOC_SWAZILAND = 'SZ'
LOC_SWEDEN = 'SE'
LOC_SWITZERLAND = 'CH'
LOC_SYRIAN_ARAB_REPUBLIC = 'SY'
LOC_TAIWAN_PROVINCE_OF_CHINA = 'TW'
LOC_TAJIKISTAN = 'TJ'
LOC_TANZANIA_UNITED_REPUBLIC_OF = 'TZ'
LOC_THAILAND = 'TH'
LOC_TIMOR_LESTE = 'TL'
LOC_TOGO = 'TG'
LOC_TOKELAU = 'TK'
LOC_TONGA = 'TO'
LOC_TRINIDAD_AND_TOBAGO = 'TT'
LOC_TUNISIA = 'TN'
LOC_TURKEY = 'TR'
LOC_TURKMENISTAN = 'TM'
LOC_TURKS_AND_CAICOS_ISLANDS = 'TC'
LOC_TUVALU = 'TV'
LOC_UGANDA = 'UG'
LOC_UKRAINE = 'UA'
LOC_UNITED_ARAB_EMIRATES = 'AE'
LOC_UNITED_KINGDOM = 'GB'
LOC_UNITED_STATES = 'US'
LOC_UNITED_STATES_MINOR_OUTLYING_ISLANDS = 'UM'
LOC_URUGUAY = 'UY'
LOC_UZBEKISTAN = 'UZ'
LOC_VANUATU = 'VU'
LOC_VENEZUELA_BOLIVARIAN_REPUBLIC_OF = 'VE'
LOC_VIET_NAM = 'VN'
LOC_VIRGIN_ISLANDS_BRITISH = 'VG'
LOC_VIRGIN_ISLANDS_US = 'VI'
LOC_WALLIS_AND_FUTUNA = 'WF'
LOC_WESTERN_SAHARA = 'EH'
LOC_YEMEN = 'YE'
LOC_ZAMBIA = 'ZM'
LOC_ZIMBABWE = 'ZW'
