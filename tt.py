def mf(str1,str2):
    print(str1,str2)
    if len(str1)==0:
        return True
    if str1[0] ==str2[-1]:
        return mf(str1[1:],str2[:-1])
    else:
        return False


print(mf("giri","irig"))
