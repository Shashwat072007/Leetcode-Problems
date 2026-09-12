class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0){
            return false;
        }
        long long int r=0;
        int d;
        int original=x;
        while(x!=0){
            d=x%10;
            r=r*10+d;
            x=x/10;
        }
        if (original==r){
            return true;
        }
        else{
            return false;
        }
        
    }
};