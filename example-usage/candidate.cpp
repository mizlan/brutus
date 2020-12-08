#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;
using num = long long;

void fileio(const string& p) {
#ifndef FEAST_LOCAL
  freopen((p + ".in").c_str(), "r", stdin);
  freopen((p + ".out").c_str(), "w", stdout);
#endif
}

const num MOD = 1e9+7;
enum EventType { START, END };

array<num, (int)(1e5 + 1)> two_pow;

int main() {
  two_pow[0] = 1;
  for (int i = 1; i <= (int)(1e5 + 1); i++) {
    two_pow[i] = 2 * two_pow[i - 1] % MOD;
  }
  fileio("help");
  int N; cin >> N;
  vector<pair<num, EventType>> a; a.reserve(2 * N);
  num numEnded = 1;
  num ans = 0;
  for (int i = 0; i < N; i++) {
    num s, e; cin >> s >> e;
    a.emplace_back(s, START);
    a.emplace_back(e, END);
  }
  sort(a.begin(), a.end());
  for (const auto& p: a) {
    num pos = p.first;
    EventType etype = p.second;
    if (etype == START) {
      ans *= 2;
      ans += two_pow[numEnded - 1];
      ans %= MOD;
    } else {
      // etype == END
      numEnded++;
    }
  }
  cout << ans << '\n';
}
