class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        vector<int> result;

        unordered_map<int, int> mp1;
        unordered_map<int, int> mp2;

        for(auto i : nums1) {
            mp1[i]++;
        }

        for(auto i : nums2) {
            mp2[i]++;
        }

        for(auto i : mp1){
            if (mp2.find(i.first)!=mp2.end()){
                result.push_back(i.first);
            }
        }

        return result;
    }
};