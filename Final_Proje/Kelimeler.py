
# KOLAY (4-5)

dort_harfli_esya = ['masa', 'ayna', 'vazo', 'kase', 'sıra', 'örtü','örgü', 'askı', 'priz', 'kapı', 'iğne', 'odun',
                    'halı', 'alçı']
dort_harfli_giysi = ['etek', 'bluz']
dort_harfli_hayvan = ['deve', 'keçi', 'kuzu', 'eşek', 'kene', 'pire', 'dana', 'öküz', 'inek', 'fare', 'kurt']
dort_harfli_meyve = ['üzüm', 'ayva', 'elma', 'erik', 'kivi', 'iğde']
dort_harfli_sebze = ['roka', 'pazı']


bes_harfli_esya = ['çanta', 'tahta', 'çekiç', 'radyo', 'kağıt', 'sehpa', 'dolap', 'kalem', 'kaşık', 'bıçak', 'tabak',
                   'tablo', 'lamba', 'tepsi', 'kilit', 'rende', 'makas']
bes_harfli_giysi = ['kazak', 'hırka', 'ceket', 'kemer', 'fular', 'kaban', 'palto']
bes_harfli_hayvan = ['yılan', 'köpek', 'domuz', 'akrep', 'serçe', 'tavuk', 'horoz', 'hindi', 'şahin', 'koyun', 'manda',
                     'tilki', 'geyik', 'kirpi']
bes_harfli_meyve = ['hurma', 'armut', 'kiraz', 'çilek', 'vişne', 'kavun']
bes_harfli_sebze = ['biber', 'marul', 'soğan', 'bamya']

dort_harfli = dort_harfli_esya + dort_harfli_giysi + dort_harfli_hayvan + dort_harfli_meyve + dort_harfli_sebze
bes_harfli = bes_harfli_esya + bes_harfli_giysi +bes_harfli_hayvan + bes_harfli_meyve + bes_harfli_sebze

kolay = dort_harfli + bes_harfli

kolay_esya = dort_harfli_esya + bes_harfli_esya
kolay_giysi = dort_harfli_giysi + bes_harfli_giysi
kolay_hayvan = dort_harfli_hayvan + bes_harfli_hayvan
kolay_meyve = dort_harfli_meyve + bes_harfli_meyve
kolay_sebze = dort_harfli_sebze + bes_harfli_sebze


# ORTA (6-7)

alti_harfli_esya = ['terlik', 'bardak', 'cımbız', 'gözlük', 'koltuk', 'sandık', 'demlik', 'yorgan', 'yastık', 'parfüm',
                    'sürahi', 'küllük', 'balyoz']
alti_harfli_giysi = ['pijama', 'eşofman', 'pardösü', 'gömlek', 'halhal']
alti_harfli_hayvan = ['akbaba', 'balina', 'leylek', 'pirana', 'bülbül', 'maymun', 'kaplan', 'yarasa', 'timsah']
alti_harfli_meyve = ['kayısı', 'karpuz']
alti_harfli_sebze = ['mantar', 'lahana', 'pancar', 'pırasa']


yedi_harfli_esya = ['mengene', 'ışıldak', 'testere', 'tencere', 'mobilya', 'telefon', 'karyola']
yedi_harfli_hayvan = ['karınca', 'papağan', 'örümcek', 'penguen', 'balaban', 'pelikan', 'kukumav']
yedi_harfli_meyve = ['avokado', 'muşmula', 'şeftali']
yedi_harfli_sebze = ['domates', 'brokoli', 'dereotu', 'ıspanak', 'kereviz', 'patates']

alti_harfli = alti_harfli_esya + alti_harfli_giysi + alti_harfli_hayvan + alti_harfli_meyve + alti_harfli_sebze
yedi_harfli = yedi_harfli_esya + yedi_harfli_hayvan + yedi_harfli_meyve + yedi_harfli_sebze

orta = alti_harfli + yedi_harfli

orta_esya = alti_harfli_esya + yedi_harfli_esya
orta_giysi = alti_harfli_giysi
orta_hayvan = alti_harfli_hayvan + yedi_harfli_hayvan
orta_meyve = alti_harfli_meyve + yedi_harfli_meyve
orta_sebze = alti_harfli_sebze + yedi_harfli_sebze

# ZOR (8-9)

sekiz_harfli_esya = ['ayakkabı', 'kalemlik', 'sandalye', 'kerpeten', 'kitaplık', 'merdiven', 'kulaklık', 'akordeon']
sekiz_harfli_giysi = ['pantolon', 'bindallı']
sekiz_harfli_hayvan = ['kırkayak', 'güvercin', 'saksağan', 'gergedan', 'şempanze', 'gelincik', 'kelaynak']
sekiz_harfli_meyve = ['bergamot', 'frambuaz', 'greyfurt', 'kızılcık', 'kuşburnu', 'portakal']
sekiz_harfli_sebze = ['maydanoz', 'patlıcan', 'semizotu', 'sarımsak', 'zencefil']


dokuz_harfli_esya = ['jeneratör', 'portmanto', 'yağmurluk', 'kalorifer']
dokuz_harfli_hayvan = ['tarantula', 'hipopotam', 'orangutan', 'salyangoz', 'bukalemun', 'bıldırcın']
dokuz_harfli_meyve = ['böğürtlen', 'balkabağı', 'mandalina']
dokuz_harfli_sebze = ['salatalık', 'kuşkonmaz']

sekiz_harfli = sekiz_harfli_esya + sekiz_harfli_giysi + sekiz_harfli_hayvan + sekiz_harfli_meyve + sekiz_harfli_sebze
dokuz_harfli = dokuz_harfli_esya + dokuz_harfli_hayvan + dokuz_harfli_meyve + dokuz_harfli_sebze

zor = sekiz_harfli + dokuz_harfli

zor_esya = sekiz_harfli_esya + dokuz_harfli_esya
zor_giysi = sekiz_harfli_giysi
zor_hayvan = sekiz_harfli_hayvan + dokuz_harfli_hayvan
zor_meyve = sekiz_harfli_meyve + dokuz_harfli_meyve
zor_sebze = sekiz_harfli_sebze + dokuz_harfli_sebze