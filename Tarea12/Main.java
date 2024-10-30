import java.util.ArrayList;
import java.util.List;

public class Main {
    public static ArrayList mergeSort(ArrayList data) {
        if(data.size() > 1){
            int mitad = data.size() / 2;
            ArrayList<Integer> izq = new ArrayList<>();
            ArrayList<Integer> der = new ArrayList<>();
            for (int i = 0; i < mitad; i++) {
                izq.add((int) data.get(i));
            }
            int restante = data.size() - mitad;
            for (int i = 0; i < restante; i++) {
                der.add((int) data.get(i + mitad));
            }
            System.out.println(izq + "  " + der);
            mergeSort(izq);
            mergeSort(der);
            int i = 0;
            int d = 0;
            int k = 0;
            while (i < izq.size() && d < der.size()) {
                if (izq.get(i) < der.get(d)) {
                    data.set(k,izq.get(i));
                    i++;
                } else {
                    data.set(k,der.get(d));
                    d++;
                }
                k++;
            }
            while (i < izq.size()){
                data.set(k,izq.get(i));
                i++;
                k++;
            }
            while (d < der.size()){
                data.set(k,der.get(d));
                d++;
                k++;
            }
        }
        System.out.println("regreso de rec :" + data);
        return data;
    }

    public static void main(String[] args) {
        ArrayList info = new ArrayList<>();
        List<Integer> lista = List.of(1,11,13,10,3,9,36,8,21,7,15);
        for (Integer item: lista){
            info.add(item);
        }
        mergeSort(info);
    }
}