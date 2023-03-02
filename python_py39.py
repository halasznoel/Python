szavak = ["alma", "körte", "barack", "szilva", "eper"]
nagybetus_szavak = list(map(lambda szo: szo.upper() if len(szo) > 3 else szo, szavak))

print("Eredeti lista: ", szavak)
print("Nagybetűs lista: ", nagybetus_szavak)
