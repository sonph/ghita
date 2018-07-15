/**
 * Transpose a list of lists, for table display in Vue.
 * @params {Array.<any>} arrays
 * @params {any} fill
 *
 * @example
 * // returns [['a', 1], ['b', 2], [null, 3]]
 * transpose([['a', 'b'], [1, 2, 3]])
 *
 * @returns {Array.<Array.<any>>}
 */
export function tranpose(arrays, fill=null) {
  const longestLength = arrays[0].length;

  arrays.forEach(function(array) {
    longestLength = Math.max(longestLength, array.length);
  });

  const ret = [];

  for (let i=0; i<longestLength; i+=1){
    ret.push([]);
    arrays.forEach(function(array) {
      const value = i < array.length ? array[i] : fill;
      ret[i].push(value);
    });

    return ret;
  }
}

/**
 * Shifts elements to the left, cycling to the back, returning a new array.
 * @param {Array.<any>} array
 * @param {number} num
 *
 * @example
 * // returns [3,4,5,1,2]
 * @returns {Array.<any>}
 */
export function rotate(array, num) {
  const index = num % array.length;
  return array.slice(index).concat(array.slice(0, index));
}
