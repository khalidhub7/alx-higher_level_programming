const { argv } = require('node:process');
const mylist = [];

// Extract elements from command line
argv.slice(2).forEach((value) => {
  const num = Number(value);
  if (!isNaN(num)) { // Check if the value is a valid number
    mylist.push(num);
  }
});

if (mylist.length < 2) {
  console.log(0);
} else {
  const sortedList = mylist.sort((a, b) => b - a); // Sort in descending order
  console.log(sortedList[1]);
}
