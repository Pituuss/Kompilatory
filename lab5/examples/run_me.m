N = 10;
A = [[1,2,3,4],[5,6,7,8]];
A[0,3] = N;
print A';
M = 20;
for i = 1:N {
    for j = i:M {
        print i, j;
    }
}

if(N==10){

    print "N==10";
}
else if(N!=10)
    print "N!=10";

if(N>5)
    print "N>5";
else if(N>=0)
    print "N>=0";

if(N<10)
    print "N<10";
else if(N<=15)
    print "N<=15";


k=3;
while(k>0) {
    if(k<5)
        i = 1;
    else if(k<10)
        i = 2;
    else
        i = 3;
    print k;
    k = k - 1;
}