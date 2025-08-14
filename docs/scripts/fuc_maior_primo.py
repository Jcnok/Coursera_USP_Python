def maior_primo(x):
    while x > 2:
        if (x%2==0) or (x%100==1):
            x=x-1
        else:
            if(x%10>1) and x%(x%10)==0:
                x=x-1
            else:
                return(x)
                break
    return(x)