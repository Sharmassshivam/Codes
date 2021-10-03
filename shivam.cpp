#include <bits/stdc++.h>
#include<iostream>
#define ll long long
#define pi 3.1415926535897932384626
#define mod 1e9+7
#define endl "\n"

using namespace std;

void solve()
{
    ll anmol,p;
    cin>>anmol>>p;
    ll total=pow(2,anmol)-1;
    ll count=0;
    ll ans=0;
    for(ll i=0;i<anmol;i++)
    {
        ll value=pow(2,i);
        if(value>p)
         break;
        count+=value;
        ans++;
    }
    total=total-count;
    if(total%p!=0)
     ans++;
    ans+=(total/p);
    cout<<ans<<endl;
}



int main()
{
   ll t;
   cin>>t;
   while(t--)
   {
       solve();
   }
   return 0;
}
