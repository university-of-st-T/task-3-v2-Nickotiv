def calculate_total(prices, *discounts, **options):
    summa = sum(i for i in prices)
    for i in discounts:
        summa *= ((100-i)/100)
    if options:
        for i in range(len(list(options))):
            if (list(options)[i]) == "tax":
                summa *= (1 + (options["tax"])/100)
            if (list(options)[i]) == "round_to":
                if options["round_to"] == None:
                    summa = int(summa) + float(str(summa - int(summa))[:4])
                else:
                    summa = int(summa) + float(str(summa - int(summa))[:(options["round_to"])+2])

    return summa
