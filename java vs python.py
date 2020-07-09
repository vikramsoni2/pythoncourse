



public static void main(String[] args){
    souble x = z(1, 100, 3);
}

public static double z(int a, int b, int c){
    double d = 0.0;
    double e = 0.0;

    for(int i=a; i < b-a; i++){
        if(i % c == 0){
            d = d + 1
        }
        else{
            e = e + 1
        }
    }
    if(d > e){
        return d;
    else{
        return e;
    }
}








