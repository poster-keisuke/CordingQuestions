// 28. Implement strStr()
// https://leetcode.com/problems/implement-strstr/

function strStr(haystack: string, needle: string): number {
  if (needle === haystack) return 0;
  if (needle === '') return 0;
  if (needle.length > haystack.length) return -1;

  for (let i = 0; i < haystack.length; i++) {
    if (needle === haystack.slice(i, i + needle.length)) return i;
  }

  return -1;
}

function strStr2(haystack: string, needle: string): number {
  if (needle === '') return 0;

  return haystack.indexOf(needle);
}
