def luckyCustomer(productTypes,numk,prices):
    frq={}
    for price in prices:
        frq[price]=frq.get(price,0)+1
        count=0

    if numk==0:
        for value in frq:
            f = frq[value]
            count += f * (f - 1) // 2
    else:
        for value in frq:
            if value + numk in frq:
                count += frq[value] * frq[value + numk]

    return count

productTypes = 5
numk = 2
prices = [1, 5, 3, 4, 2]
print(luckyCustomer(productTypes,numk,prices))


