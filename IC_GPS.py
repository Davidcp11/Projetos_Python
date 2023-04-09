import F_GPS
'''----------------------------------------------------------------------'''
# arquivo in (x for x in arquivos if 'Cmn' in x)
'''Ler todos os arquivos da pasta'''
F_GPS.Vtec_vs_t(['braz'], 14, 1)
# Brasilia, Belém, Uruaçu, Goiânia, Florianópolis, Porto Alegre, Lages, Marabá
F_GPS.ROT(['bele',  'gour', 'braz', 'gogy', 'ifsc', 'poal'], [13, 14, 15, 16, 17, 18], 1)
F_GPS.ROTi('braz', 14, 1)
dias_calmos = [5, 6, 7, 10, 11, 12, 13, 24]
F_GPS.Tec_vs_tec_medio(['bele', 'maba', 'gour', 'braz', 'gogy', 'ifsc', 'poal'], 13, 18, dias_calmos, 1)