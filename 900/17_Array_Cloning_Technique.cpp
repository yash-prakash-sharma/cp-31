// https://codeforces.com/problemset/problem/1665/B
#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll t;
    cin >> t;
    while(t--){
        ll n;
        cin >> n;
        vector<ll> a(n);
        for(ll i=0; i<n; ++i) cin >> a[i];
        map<ll, ll> mp;
        ll freq=0;
        for(ll i=0;i<n;++i){
            mp[a[i]]++;
            if(mp[a[i]]>freq){
                freq=max(mp[a[i]], freq);
            }
        }
        ll ops=0;
        ll left_places=n-freq;
        ll cur_copy=freq;
        while(left_places>0){
            ops+=1;
            ops+=min(left_places,cur_copy);
            left_places-=min(left_places,cur_copy);
            cur_copy<<=1;
        }
        cout << ops << endl;
    }
}