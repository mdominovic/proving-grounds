#define INT_MAX 2147483647
#define INT_MIN -2147483648

class ReverseInteger {
public:
    int reverse(int x) {
        
        int modul, result = 0, prefix = 1;
        int upper = INT_MAX;
        int lower = INT_MIN;

        if (x < 0){
            if (x == lower){
                return 0;
            }
            prefix = -1;
            x = -x;
        }

        do{
            if (result > upper/10){
                return 0;
            }
            result *= 10;
            modul = x % 10;
            
            if (result > upper-modul){
                return 0;
            }
            result += modul;
            x /= 10;
        }while (x > 0);
        
        return result * prefix;
    }
};