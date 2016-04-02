def findIndex(arr,condFunc):
    retIndex = [i for i in range(len(arr)) if condFunc(arr[i])]
    return retIndex


def maxCountItem(myList):
    mySet = set(myList)
    count = {x:myList.count(x) for x in mySet}
    arr = sorted(count.items(),key=lambda x:x[1],reverse=True)
    res = [arr[i][0] for i in range(len(arr)) if arr[i][1]==arr[0][1]]
    return res


def sumif(arr,condFunc):
    condArr = filter(condFunc,arr)
    res = sum(condArr)
    return res


def countif(arr,condFunc):
    subArr = filter(condFunc,arr)
    count = len(subArr)
    return count


def lineRegress(matX,vecY):
    import statsmodels.api as sm
    matX = sm.add_constant(matX)
    res = sm.OLS(vecY,matX).fit()
    print res.summary()
    return res.params
   

    
def loadDataSet(filename):
    import pandas as pd
    df = pd.read_csv(filename)
    inX = df.iloc[:,:-1].values
    Y = df.iloc[:,-1].values
    return inX,Y


def findAll(string,target):
    targetList = [i for i in range(len(string)) if string[i] == target]
    return targetList


def netEasePic(url):
    photo = ul.urlopen(url)
    bs = BeautifulSoup(photo)
    girl = bs.findAll('img',{"class":"z-tag data-lazyload-src"})
    for img in girl:
        link = img.get('data-lazyload-src')
        content2 = ul.urlopen(link).read()
        with open(u'D:\myimg'+'/'+link[-15:],'wb') as code:
            code.write(content2)