// 2758. Next Day
// https://leetcode.com/problems/next-day/

Date.prototype.nextDay = function () {
    const currentDate = new Date(this.setDate(this.getDate() + 1));

    return `${currentDate.getFullYear()}-${String(currentDate.getMonth() + 1).padStart(2, '0')}-${String(currentDate.getDate()).padStart(2, '0')}`
}

/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */