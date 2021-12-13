def nthroot(x,n):
    ok=0
    ng=x
    while ng-ok>1:
        mid=(ng+ok)//2
        if(mid**n<=x):
            ok=mid
        else:
            ng=mid

    if ok**n!=x: ok=-1

    return ok