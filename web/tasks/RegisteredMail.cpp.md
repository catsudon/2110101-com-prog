
# Task: RegisteredMail.cpp

``` cpp
#include<bits/stdc++.h>
using namespace std;

int main()
{
  ios_base::sync_with_stdio(0); cin.tie(0);
  int n; cin >> n;
  int ans = 0;
  if(n > 2000) {
    cout << "Reject";
    return 0;
  }
  if(n <= 2000) ans = 58;
  if(n <= 1000) ans = 38;
  if(n <= 500) ans = 28;
  if(n <= 250) ans = 22;
  if(n <= 100) ans = 18;
  cout << ans;
}

// pythonกาก
```
    