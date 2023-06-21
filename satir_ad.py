def satir_ad(data):
    satir_isim = []
    
    for colName, colData in data.iteritems():
        satir_isim.append(colData.values)
        
    return satir_isim

