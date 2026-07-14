class Solution {
public:
    bool isLeap(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }

    int daysFrom1971(string date) {
        int year = stoi(date.substr(0, 4));

        static vector<int> daysInMonth = {
            31,28,31,30,31,30,31,31,30,31,30,31
        };

        int days = 0;

        for (int y = 1971; y < year; y++)
            days += isLeap(y) ? 366 : 365;

        for (int m = 1; m < stoi(date.substr(5, 2)); m++) {
            days += daysInMonth[m - 1];
            if (m == 2 && isLeap(year))
                days++;
        }

        days += stoi(date.substr(8, 2));

        return days;
    }

    int daysBetweenDates(string date1, string date2) {
        return abs(daysFrom1971(date1) - daysFrom1971(date2));
    }
};