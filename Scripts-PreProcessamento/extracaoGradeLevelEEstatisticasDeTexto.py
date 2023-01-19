from readability import Readability

texto = "The wolf (Canis lupus) is a mammal of the order Carnivora. It is sometimes called timber wolf or grey wolf, It is the ancestor of the domestic dog. A recent study found that the domestic dog is descended from wolves tamed less than 16,300 years ago south of the Yangtze River in China, There are many different wolf subspecies, such as the Arctic wolf. Some subspecies are listed on the endangered species list, but overall, Canis lupus is IUCN graded as 'least concern'. Adult wolves are usually 1.4 to 1.8 metres (4.6 to 5.9 ft) in length from nose to tail depending on the subspecies.[3] Wolves living in the far north tend to be larger than those living further south"
r = Readability(texto)

#grade levels
fk = r.flesch_kincaid()
f = r.flesch()
gf = r.gunning_fog()
cl = r.coleman_liau()
dc = r.dale_chall()
ari = r.ari()
lw = r.linsear_write()
#smg = r.smog(all_sentences=True)
spa = r.spache()

# Mostrando valores das grade levels
print("\n # Grade Levels #")
print("Flesch Kincaid Grade Level: " + str(fk.grade_level))
print("Flesch Reading Ease: " + str(f.grade_levels))
print("Gunning Fog: " + str(gf.grade_level))
print("Coleman Liau Index: " + str(cl.grade_level))
print("Dale Chall Readability: " + str(dc.grade_levels))
print("Automated Readability Index: " + str(ari.grade_levels))
print("Linsear Write: " + str(lw.grade_level))
#print("SMOG: " + str(smg.grade_level))
print("Spache: " + str(spa.grade_level))
print("\n")

#estatisticas do texto
silabasXpalavra = r._statistics.avg_syllables_per_word
palavrasXsentencas = r._statistics.avg_words_per_sentence
complexoDaleChall = r._statistics.num_dale_chall_complex
complexoGunning = r._statistics.num_gunning_complex
complexoSpache = r._statistics.num_spache_complex
qtdLetras = r._statistics.num_letters
polySilabasXpalavras = r._statistics.num_poly_syllable_words
numSentencas = r._statistics.num_sentences
qtdSilabas = r._statistics.num_syllables
qtdPalavras = r._statistics.num_words

# Mostrando valores das estatísticas
print("\n # Estatísticas #")
print("Média de sílabas por palavra: " + str(silabasXpalavra))
print("Média de palavras por sentença: " + str(palavrasXsentencas))
print("Complexo de Dale Chall: " + str(complexoDaleChall))
print("Complexo de Gunning: " + str(complexoGunning))
print("Complexo de Spache: " + str(complexoSpache))
print("Número de letras: " + str(qtdLetras))
print("Número de polisílabas por palavras: " + str(polySilabasXpalavras))
print("Número de sentenças: " + str(numSentencas))
print("Quantidade de sílabas: " + str(qtdSilabas))
print("Quantiade de palavras: " + str(qtdPalavras))
print("\n")