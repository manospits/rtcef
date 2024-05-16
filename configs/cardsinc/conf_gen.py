months_params = [
    [4, 0.2544979282465525, 0.006565220807138541, 0.004379156591226979],        # 0
    [4, 0.08186803478069894, 0.0001, 0.0045964762238296835],                    # 1
    [4, 0.30135198814574904, 0.0005966806508003126, 0.00033723114890161625],    # 2
    [3, 0.10519664937761039, 0.0013127105891629872, 0.007886995346600822],      # 3
    [5, 0.13751514717383212, 0.0001, 0.0001],                                   # 4
    [4, 0.09200060121075973, 0.002711565340401184, 0.008694960780476964],       # 5
    [1, 0.19158914346454342, 0.0006840319055633757, 0.00648906487974291],       # 6
    [3, 0.5086408253200942, 0.0005290358481379911, 0.005661051455064854],       # 7
    [3, 0.4330325405200162, 0.0001, 0.0006316522666548625],                     # 8
    [4, 0.14383140292682148, 0.007097002025942645, 0.007423356206711594],       # 9
    [4, 0.11455527733431087, 0.007424974451603422, 0.0069985474095819455],
    [4, 0.11416675416709982, 0.0017356616304038015, 0.008010863489690092],
    [4, 0.13451259471311874, 0.004480319995828784, 0.007974223887890272],
    [1, 0.15248002813630532, 0.0018877584475192413, 0.006848353604774837],
    [4, 0.1689103996137077, 0.001979631047657623, 0.008228125868863416],
    [4, 0.10786048107673, 0.0070734731794023726, 0.007062880665306511],
    [5, 0.17216882018073895, 0.003659312903573493, 0.005933283857671361],
    [5, 0.3362985982546938, 0.003096663411335138, 0.0008307197782892996],
    [4, 0.09233449387852534, 0.0024575074205470363, 0.008635129553580222],
    [1, 0.19561029597236337, 0.000568801392801762, 0.006780932008025942],
    [1, 0.18724635393642874, 0.0002833224817647902, 0.007162926681273668]
]

for month in range(len(months_params)):
    with open("conf_tmpl.ini") as inp, open(f"conf_{month}.ini","w") as out:
        for line in inp:
            res = line.replace("****month****", str(month))
            res = res.replace("****conf****", str(months_params[month][1]))
            res = res.replace("****order****", str(months_params[month][0]))
            res = res.replace("****pmin****", str(months_params[month][2]))
            res = res.replace("****gamma****", str(months_params[month][3]))
            res = res.replace("****gamma****", str(months_params[month][3]))
            res = res.replace("****param_list****", str(months_params[month]))
            out.write(res)