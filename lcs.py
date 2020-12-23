def lcs(x,y):
    if (len(x)==0 or len(y)==0):
        return 0
    if (x[-1]==y[-1]):
        return 1+lcs(x[:len(x)-1],y[:len(y)-1])
    return max(lcs(x,y[:len(y)-1]),lcs(x[:len(x)-1],y))
global C
#C= [ [0 for i in range(len(x)+1)] for j in range(len(y)+1)]
def lcsMem(x,y,m,n,C):
    #C = [ [0 for i in range(len(x)+1)] for j in range(len(y)+1)]
        if(m==0 or n==0):
            return 0
        if C[m-1][n-1] != -1:
            return C[m-1][n-1]
        if(x[m-1]==y[n-1]):
            C[m-1][n-1] = 1 + lcsMem(x,y,m-1,n-1,C)
            return C[m-1][n-1]
        else:
            C[m-1][n-1] = max (lcsMem(x,y,m,n-1,C),lcsMem(x,y,m-1,n,C))
            return C[m-1][n-1]
        
        
        

def lcsDP(x,y):
    L = [[0 for i in range(len(y)+1)] for i in range( len(x)+1)]
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if (i==0 or j==0):
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])

    return L[len(x)][len(y)]
    

x = 'abccddeffffffhueshjhsuvsnruyrhyughyuhguihresguiherusvy8ghyuregyugehsyugyurehyugeyusgyusgyureyugyuefgyuaegyufgsyuihsufhgsiuhuafviwojiugheuishuighsuirehguirehiuhgeuirahorgiureughdyuohsughoyusehogyrhdyshouipghresuihgjerbgsoughyregyirejsiwhgiseugawhuihregrehuhgeuhreuxfknvsdhiohruvshogreuioghsvdjuirhuihsuighurhuahguhyurhughruhgurhfuigrhfuigohguhruohgurhorzuoghuiuirojugsheruohrsuhgyurheusghuiroghuriehgiushruiokklfxxxxxx'
y = 'iamfurryfjkljknesuihruisjsioejgisrjiojgiojsiojsegiojeiosjgiojieosjgiohsuishujlkjjdfrbiuhersugushgurehygsy8ghreuihsuoheruighouiohgriuoshuighreuhrsuihguirsheuigsoehuighsuioghuishreiukljvjdnsvdreiuhsguirenuyre8usnhergbuyrsehguirbseyuhgjueirngusjresnjifsoenutojubinhsohguierhijnrsijhuigrujisgjruisnjvsdeuihruhfyugyufkyhauhfyrhfiusygfrohgiurhuisghuireshiugrshuisiojdiojfiojsfiofxx'
print(lcsDP(x,y))
C= [ [-1 for i in range(len(y
                            )+1)] for j in range(len(x)+1)]
print(lcsMem(x,y,len(x),len(y),C))
#print(lcs(x,y))

