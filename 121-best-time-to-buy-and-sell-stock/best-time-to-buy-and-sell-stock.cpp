class Solution {
public:
    int maxProfit(vector<int>& prices) {
     int minprice= prices[0];
        int maxp=0;
        int n = prices.size();
        for(int i = 0 ; i<n ; i++){
            if(prices[i]<minprice){
                minprice= prices[i];
            }
            else{
                int profit = prices[i]-minprice;
                maxp=max(maxp , profit);
            }
        }
        return maxp;
    }
};