def bands(signatureLength:int):
    i=1
    count=1
    while i<=signatureLength:
        if signatureLength%i==0:
            print(f"Bands: {i}---rows: {int(signatureLength/i)}")
            count+=1
        i+=1
        
    print(count)


bands(1113)