
import java.util.ArrayList;


class MyGenerics<T1>{
    private T1 t1;
    int val;
    MyGenerics( int val,T1 t1){
        this.val = val;
        this.t1 = t1;
    }
    T1 getT1(){
        return t1;
    }
}



public class Day_21_Generics {
    public static void main(String[] args) {
        // List<String> is a generic type
        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(3);
        System.out.println(list);
    }
}