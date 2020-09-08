// var str="Aone two";
// //查找"Hello"
// var patt=/\s/g;
// // var pattreplace = '${word2} ${word1}'
// // var result=str.replace(patt, pattreplace);
// // var result = str.match(patt)
// // var result = str.split(patt)
// var result = str.split(' ')
// console.log(result);

// function* gen(x){
//     var y = yield x + 2;
//     return y;
// }

// var g = gen(1);
// console.log(g.next());
// console.log(g.next());

// async function testAsync() {
//     // return "hello async";
// }

// // const result = testAsync().then(v=>{
// //     console.log(v);
// // });
// const result = testAsync();
// console.log(result);

// // 2s 之后返回双倍的值
// function doubleAfter2seconds(num) {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve(2 * num)
//         }, 2000);
//     })
// }

// async function testResult () {
//     let first = await doubleAfter2seconds(10);
//     let second = await doubleAfter2seconds(20);    
//     let res = first + second;
//     return res;
// }

// testResult().then(res => {
//     console.log(res);      
// }).catch(error => {
//     console.log(error);     
// });

// var fs = require('fs');
// var readFile = function (fileName) {
//     return new Promise(function (resolve, reject) {
//         fs.readFile(fileName, function (error, data) {
//             if (error) return reject(error);
//             resolve(data);
//         });
//     });
// };

// var gen = function* () {
//     var f1 = yield readFile('./s.xml');
//     var f2 = yield readFile('./SimpleSample.xml');
//     console.log(f1.toString());
//     console.log(f2.toString());
// };

// function run(gen){
//     var g = gen();
  
//     function next(data){
//       var result = g.next(data);
//       if (result.done) return result.value;
//       result.value.then(function(data){
//         next(data);
//       });
//     }
  
//     next();
//   }
  
//   run(gen);

// var obj = new Proxy({}, {
//     get: function (target, key, receiver) {
//       console.log(`getting ${key}!`);
//       return Reflect.get(target, key, receiver);
//     },
//     set: function (target, key, value, receiver) {
//       console.log(`setting ${key}!`);
//       return Reflect.set(target, key, value, receiver);
//     }
//   });

//   obj.count = 1;
//   ++obj.count;

// var proxy = new Proxy({}, {
//     get: function(target, property) {
//       console.log("target:", target);
//       console.log("pro:", property);
//       return 35;
//     }
//   });

//   proxy.time;
//   console.log(proxy.name);

// var handler = {
//   get: function(target, name) {
//     if (name === 'prototype') {
//       return Object.prototype;
//     }
//     return 'Hello, ' + name;
//   },

//   apply: function(target, thisBinding, args) {
//     return args[0];
//   },

//   construct: function(target, args) {
//     return {value: args[1]};
//   }
// };

// var fproxy = new Proxy(function(x, y) {
//   return x + y;
// }, handler);

// console.log(fproxy(1, 2)) // 1
// console.log(new fproxy(1,2)) // {value: 2}
// console.log(fproxy.prototype === Object.prototype) // true
// console.log(fproxy.foo) // "Hello, foo"

// function createArray(...elements){
//   let handler = {
//     get(target, propKey, receiver){
//       let index = Number(propKey);
//       if(index<0){
//         propKey = String(target.length+index);
//       }
//       return Reflect.get(target, propKey, receiver);
//     }
//   };

//   let target = [];
//   target.push(...elements);
//   return new Proxy(target, handler);
// }

// let arr = createArray('a', 'b', 'c');
// console.log(arr[-1]);

// str = '1234';
// console.log(str[0])

// var twice = {
//   apply(target, ctx, args){
//     return Reflect.apply(...arguments) * 2;
//   }
// };
// function sum(left, right){
//   return left + right;
// }
// var proxy = new Proxy(sum, twice);
// console.log(proxy(1,2))
// proxy.call(null, 5, 6)
// proxy.apply(null, [7, 8])

// let stu1 = {name: '张三', score: 59};
// let stu2 = {name: '李四', score: 99};

// let handler = {
//   has(target, prop){
//     if(prop === 'score' && target[prop] < 60){
//       console.log(`${target.name}不及格`);
//       return false;
//     }
//     return prop in target;
//   }
// }

// let oproxy1 = new Proxy(stu1, handler);
// let oproxy2 = new Proxy(stu2, handler);
// 'score' in oproxy1

// console.log('score' in oproxy2)

// var p = new Proxy(function(){}, {
//   construct: function(target, args){
//     console.log('called: ' + args.join(', '));
//     return {value: args[0] * 10};
//   }
// })

// console.log(new p(1).value)

// var handler = {
//   deleteProperty (target, key) {
//     // let result = invariant(key, 'delete') ? false : true;
//     // return true;
//     return true;
//   }
// };
// function invariant (key, action) {
//   if (key[0] === '_') {
//     console.log(`Invalid attempt to ${action} private "${key}" property`);
//     return true;
//   }
// }

// var target = { _prop: 'foo' };
// var proxy = new Proxy(target, handler);
// delete proxy._prop
// console.log(proxy)

// var handler = {
//   deleteProperty(target,key){
//       console.log('key',key);
//       invariant(key,'delete');
//       delete target[key];
//       // return true;
//   }
// };
// function invariant (key,action) {
//   if(key[0] === '_') {
//       throw new Error(`Invalid attempt to ${action} private "${key}" property`);
//   }
// }

// var target = {_prop:'foo',prop:'foo'};
// var proxy = new Proxy(target,handler);
// console.log("proxy1",proxy);
// console.log("delete1",delete proxy.prop);
// console.log("proxy2",proxy);

// const target = new Date('2015-01-01');
// const handler = {
//   get(target, prop){
//     if(prop === 'getDate'){
//       return target.getDate.bind(target);
//     }
//     return Reflect.get(target, prop);
//   }
// };
// const proxy = new Proxy(target, handler);
// console.log(proxy.getDate())

// var target = { _prop: 'foo' };
// console.log('_prop' in target)
// console.log(Reflect.has(target, '_prop'))

// var obj = {
//   get foo(){return this.bar;},
//   bar: '123'
// }
// var obj2 = {
//   get foo(){return this.bar;},
//   bar: '456'
// }
// console.log(Reflect.get(obj, 'foo', obj2));


// const queuedObservers = new Set();
// const observe = fn => queuedObservers.add(fn);
// const observable = obj => new Proxy(obj, {set});

// function set(target, key, value, receiver){
//   const result = Reflect.set(target, key, value, receiver);
//   queuedObservers.forEach(observer => observer());
//   return result;
// }

// const person = observable({
//   name: '绽放三',
//   age: 20
// });

// function print() {
//   console.log(`${person.name}, ${person.age}`);
// }

// observe(print);
// person.name = '李四';

// [x, y = 'b'] = ['a'];
// console.log(x, y);

// x = [5][0];
// console.log(x);

// var x;
// ({x} = {x:1});
// console.log(x);

// var x=10, y = 20;
// [x,y] = [y,x];
// console.log(x,y)

// console.log("\u{20BB7}")

// var s = "𠮷";
// console.log(s.length);

// var len = 0;
// var s = '𠮷a';
// for (let ch of s) {
//     console.log(ch.codePointAt(0).toString(16));
//     len++;
// }
// console.log(len);

// console.log(String.fromCodePoint(0x20BB7));

// console.log('abc'.charAt(0));

// var s = 'Hello world!';
// console.log(s.startsWith('hello'));
// console.log(s.endsWith("!"));
// console.log(s.includes('o'));

// console.log('x'.padStart(5, 'ab'));

// var total = 30;
// var msg = passthru`the total is ${total} (${total*1.05} with tax)`;
// console.log(msg);
// function passthru(literals){
//     var result = '';
//     var i = 0;
//     while(i<literals.length){
//         result+=literals[i++];
//         if(i<arguments.length){
//             result += arguments[i];
//         }
//     }
//     return result;
// }

// console.log`123`;

// tag`first line\nSecond line`

// function tag(strings){
//     console.log(strings.raw[0]);
// }
// console.log('first line\nSecond line')

// console.log(String.raw({ raw: 'test' }, 0, 1, 2));

// function tag(strs) {
//     console.log(strs[0] === undefined)
//     console.log(strs.raw[0] === "\\unicode and \\u{55}");
// }
// tag`\unicode and \u{55}`

// let bad = `bad escape sequence: \unicode`;

// var regex = new RegExp(/xyz/, 'i');

// var s = '𠮷';
// var r = /^.$/.test(s);
// console.log(r);

// var r = /[a-z]{2}|[A-Z]/u.test('kc');
// console.log(r);

// var s = 'aaa_aa_a';
// var r1 = /a+/g;
// var r2 = /a+_/y;

// console.log(r1.exec(s));
// console.log(r1.exec(s));
// console.log(r1.exec(s));

// console.log(r2.exec(s));
// console.log(r2.exec(s));
// console.log(r2.exec(s));

// const REGEX = /a/y;
// REGEX.lastIndex = 3;
// console.log(REGEX.exec('xaya'));

// console.log('##'.split(/#/y));

// console.log('a1a2a3'.match(/a\d/gy));

// console.log('+'.match(/\+/y));

// const TOKEN_Y = /\s*(\+|[0-9]+)\s*/y;
// const TOKEN_G  = /\s*(\+|[0-9]+)\s*/g;

// console.log(tokenize(TOKEN_Y, '3 + 4'));
// // [ '3', '+', '4' ]
// console.log(tokenize(TOKEN_G, '3 + 4'));
// // [ '3', '+', '4' ]

// function tokenize(TOKEN_REGEX, str) {
//   let result = [];
//   let match;
//   while (match = TOKEN_REGEX.exec(str)) {
//     result.push(match[1]);
//   }
//   return result;
// }

// console.log(/\s*(\+|[0-9]+)\s*/ig.source);
// console.log(/abc/ig.flags);

// console.log(/^\n$/.test('\u000A'));

// console.log(/^\n$/);

// const re = /foo.bar/s;
// console.log(re.test('foo\nbar'));
// console.log(re.dotAll);

// const regexGreekSymbol = /\p{Script=Greek}/u
// console.log(regexGreekSymbol.test('π'))

// console.log(0o767 === 503)

// console.log(Number.isFinite(Infinity))
// console.log(typeof NaN);
// console.log(Number.parseInt('12.74'));
// console.log(Number.EPSILON.toFixed(20));
// console.log(9007199254740992 > Number.MAX_SAFE_INTEGER);
// console.log(Math.trunc('123.456'));
// console.log(0b1<<1);

// let b = 3;
// b **= 3;
// console.log(b);

// function foo() {
//     var args = [...arguments];
//     console.log(args);
// }
// foo(1,2,3);

// var arr = Array.from([1,2,3], (x)=>x*x);
// console.log(arr);

// var a = [1,,2,,3];
// var s = Array.from(a, (n)=>n||0);
// console.log(a);
// console.log(s);

var obj = {length: 2, arg: 'ch'};
var arr = Array.from(obj, () => 'jack');
console.log(arr);