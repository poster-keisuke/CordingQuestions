type DateObject = {
  day: string;
  month: string;
  year: string;
};

const getformatedDate = (current: Date): DateObject => {
  const day =
    current.getDate() < 10
      ? `0${current.getDate()}`
      : current.getDate().toString();
  const month =
    current.getMonth() + 1 < 10
      ? `0${current.getMonth() + 1}`
      : (current.getMonth() + 1).toString();
  const year = current.getFullYear().toString();

  return {
    day,
    month,
    year,
  };
};

function* dateRangeGenerator(
  start: string,
  end: string,
  step: number
): Generator<string> {
  const startDate = new Date(start);
  const endDate = new Date(end);

  let date = new Date(startDate.getTime());
  while (endDate.getTime() >= date.getTime()) {
    const formated = getformatedDate(date);
    yield `${formated.year}-${formated.month}-${formated.day}`;

    const addingDay = 60 * 60 * 24 * 1000 * step;
    date = new Date(date.getTime() + addingDay);
  }
}

/**
 * const g = dateRangeGenerator('2023-04-01', '2023-04-04', 1);
 * g.next().value; // '2023-04-01'
 * g.next().value; // '2023-04-02'
 * g.next().value; // '2023-04-03'
 * g.next().value; // '2023-04-04'
 * g.next().done; // true
 */
