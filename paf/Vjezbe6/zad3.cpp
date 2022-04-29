#include <iostream>
#include <list>
#include <iterator>
#include <algorithm>

using namespace std;

void field(list <int> thelist){

    list <int> :: iterator it;
    for(it = thelist.begin(); it != thelist.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
}

int main() {

    list<int> thelist;
    thelist.push_back(3);
    thelist.push_back(-3);
    thelist.push_back(4);
    thelist.push_back(-9);
    thelist.push_back(8);
    thelist.push_back(1);

    cout << "\n The list : ";
    field(thelist);

    cout << "\n the list after changing the order : ";
    thelist.reverse();
    field(thelist);

    cout << "\n the list after switching order : ";
    using std::swap;
    for (auto it = std::begin(thelist); it != std::end(thelist); it = std::adjacent_find(it, std::end(thelist), std::less<int>{})) {
    swap(*it, *std::next(it));
    }
    field(thelist);

    cout << "\n the list after sorting : ";
    thelist.sort();
    field(thelist);

    return 0;

}