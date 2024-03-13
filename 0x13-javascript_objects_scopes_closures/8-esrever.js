#!/usr/bin/node

/* returns reversed version of list */
exports.esrever = function (list) {
  let i = list.length - 1;
  /* push reversed list */
  while (i >= 0) {
    list.push(list[i]);
    i--;
  }
  /* remove original list */
  list.splice(0, list.length / 2);
  return list;
};
