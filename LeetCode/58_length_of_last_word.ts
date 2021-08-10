// 58. Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

function lengthOfLastWord(s: string): number {
  const words = s.split(' ');

  for (let i = words.length; 0 < i; i--) {
    if (words[i - 1] === '') continue;
    return words[i - 1].length;
  }

  return -1;
}
