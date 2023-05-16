// 1108. Defanging an IP Address
// https://leetcode.com/problems/defanging-an-ip-address/description/

function defangIPaddr(address: string): string {
  let newValue = '';
  for (let i = 0; i < address.length; i++) {
    if (address[i] === '.') {
      newValue += '[.]';
    } else {
      newValue += address[i];
    }
  }

  return newValue;
}
