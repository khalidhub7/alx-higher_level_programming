const mylist = [];
let nums = 0;

/* extract elements in command line */
process.argv.forEach((value, key) => {
  if (key >= 2) { // Start from index 2 to skip the first two elements (node executable and script file)
    nums = value;
    mylist.push(Number(nums));
  }
});

if (process.argv.length < 4) {
  console.log('0');
} else {
  const NewList = [];
  let i = 2;
  /* removing index 0 && index 1 in list  */
  while (i < process.argv.length) {
    NewList.push(mylist[i - 2]); // Adjusting index to match mylist
    i++;
  }
  NewList.sort();
  NewList.reverse();
  console.log(`${NewList[1]}`);
}
