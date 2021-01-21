// var gen = function* gen(){
//     try{
//         yield console.log('a');
//     }catch(e){

//     }
//     yield console.log('b');
//     yield console.log('c')
// }

// var g = gen();
// // g.next();
// // g.throw();
// // g.throw();
// console.log(g.next());
// console.log(g.next());

// let read = (function* (){
//     yield 'hello';
//     yield* 'hello';
// })();
// console.log(read.next().value);
// console.log(read.next().value);

// function Point(x = 0, y = 0) {
//     this.x = x;
//     this.y = y;
// }
// var p = new Point();
// console.log(p);

// function* makeSimpleGenerator(array){
//     var nextIndex = 0;
//     while(nextIndex < array.length){
//         yield array[nextIndex++];
//     }
// }

// var gen = makeSimpleGenerator(['yo', 'ya']);
// console.log(gen.next());
// console.log(gen.next());
// console.log(gen.next());

// function Person() {
//     this.name = 'hell';
// }

// var p1 = Person();
// console.log(p1);
// console.log(global.name);

// Function.prototype.my_bind = function(context){
//     var args = Array.prototype.slice.call(arguments, 1);
//     var self = this;
//     return function () {
//         var innerArgs = Array.prototype.slice.call(arguments);
//         var finalArgs = args.concat(innerArgs);
//         return self.apply(context, finalArgs);
//     }
// }

// function a(m, n, o) {
//     return this.name + ' ' + m + " " + n + ' ' + o;
// }

// var b = {name: 'kong'};
// var s = a.my_bind(b, 7, 8)(9);
// console.log(s);

// var name = 'tom';
// console.log(this);
// console.log('---------------------');
// function add(){
//     console.log(this);
// }
// add();

// function Person(name, age){
//     this.name = name;
//     this.age = age;
//     this.sayhello = function(){alert("hello");}
// }

// function Student(name, age, grade) {
//     Person.apply(this, arguments);
//     this.grade = grade;
// }

// var s1 = new Student('kake', 13, 5);
// s1.sayhello();
// console.log(s1);

// function Student(grade) {
//     this.grade = grade;
// }

// var s = Person.bind(new Student(5), 'jake');
// var s1 = new s(12);
// console.log(s1);

// var person = {
//     fullName: function () {
//         return this.firstName + " " + this.lastName;
//     }
// }
// var person1 = {
//     firstName: "Bill",
//     lastName: "Gates",
// }

// console.log(person.fullName.call(person1));

// console.dir(Function);

// var obj = function (name) {
//     this.name = name;
// }
// obj.__proto__ = {
//     b:44,
// }
// ob = new obj('ch');
// console.log(ob);

// var fn3 = function fn4() {
    
// }
// console.log(fn3.name);
// var fn5 = new Function();
// console.log(fn5.name);
// var fn6 = ()=>{}
// console.log(fn6.name);

// var price1 = 10;
// var price2 = 10;
// var price3 = new Number('10');
// var price4 = price3;
// console.log(price1 == price2);//true
// console.log(price1 == price3);//false
// price4 = 10;
// console.log(price4 == price3);//true
// console.log(price4 === price3);//false 
// let a = undefined, b = undefined;
// console.log(a+b);
// var a = {name: 'chen', toString: function(){return this}};
// function bfunc(){
//     this.sunf = ()=>{
//         return this;
//     }
// }
// console.log(new bfunc().sunf());

// class a{
    
// }
// a.test = true;
// b = new a();
// console.log(a.test);
// console.log(b.test);

// function testable(target) {
//     target.isTestable = true;
// }

// @testable
// class MyT{}

// console.log(MyT.isTestable)

// class a{
//     tt = true;
//     constructor(){
//         console.log(this.tt);
//     }
// }

// new a();

// var s = Object.keys("foo");
// console.log(s);

// class Person{  
//     // 构造  
//     constructor(x,y){  
//         this.x = x;  
//         this.y = y;  
//     }  
  
  
//     toString(){  
//         return (this.x + "的年龄是" +this.y+"岁");  
//     }  
// }  

// Object.assign(Person.prototype,{  
//     getWidth(){  
//         console.log('12');  
//     },  
//     getHeight(){  
//         console.log('24');  
//     }  
// });  
// console.log(Person.prototype);
// console.log(Object.getOwnPropertyNames(Person.prototype))

// Object.assign(Person, {
//     tfunc(){
//         console.log("static method!")
//     }
// })
// Person.tfunc()
// console.log(Object.keys(Person))
// let per = new Person("lid", 23);
// console.log(per);
// let per2 = new Person("hen", 55);
// console.log(per.__proto__ === per2.__proto__);

// function PersonP(name, age){
//     this.name = name;
//     this.age = age;
//     this.sayhello = function(){alert("hello");}
// }
// let pp = new PersonP("chen", 13);
// let pp2 = new PersonP("chgen", 143);
// console.log(pp.__proto__ === pp2.__proto__);

// new A()
// function A(){}

// new B()
// class B{}

// class Person{  
//     // 构造  
//     constructor(x,y){  
//         this.x = x;  
//         this.y = y;  
//     }  
  
//     static getY(){
//         console.log(this.y);
//     }
  
//     toString(){  
//         return (this.x + "的年龄是" +this.y+"岁");  
//     }  
// }  

// Object.assign(Person, {
//     tfunc(){
//         console.log("static method!")
//     }
// })

// console.log(Object.getOwnPropertyNames(Person))

// const Expression = class Expre{
//     getClassName(){
//         return "c1=" + Expre.name + ", c2=" + Expression.name;
//     }
// }
// console.log(new Expression().getClassName());

// let b = (function (){
//     console.log("sss")
// })()
// console.log(b);

// let person = new class{
//     constructor(props){
//         this.props = props;
//     }
//     getProps(){
//         return this.props;
//     }
// }('props in constructor');
// console.log(person.getProps());

// class Person{  
//     tt2 = 'chen'
//     static tt3 = "hello"
//     // 构造  
//     constructor(x,y){  
//         this.x = x;  
//         this.y = y;  
//         this.tt();
//     }  
  
//     static getY(){
//         console.log(this.y);
//     }
  
//     toString(){  
//         return (this.x + "的年龄是" +this.y+"岁");  
//     }  

//     tt = function(){
//         console.log("wwww")
//     }
// }  
// let p = new Person("c", 33);
// console.log(p)
// console.log(Person.tt3)
// console.log(Object.keys(Person))
// console.log(Object.getOwnPropertyNames(Person))

// class StaticMethodParent{
//     prop = 1001;
//     static getCommon(){
//         console.log("father's method");
//     }
// }

// class StaticMethod extends StaticMethodParent{
//     static lastName = 'pcaca';
//     height = '150cm';
//     getHeight(){
//         return this.height;
//     }

//     constructor(){
//         super();
//         this.width = '40cm';
//         console.log(this.prop)
//     }

//     getWidth(){
//         return this.width;
//     }
//     static getAge(){
//         super.getCommon();
//         console.log('static')
//     }
// }

// StaticMethod.getAge()
// let b = new StaticMethod();
// console.log(b);

// console.log(0 == null)

// const obj1 = {};
// const obj2 = {
//     property1: 33
// }
// obj1.__proto__ = obj2;
// console.log(obj1.hasOwnProperty("property1"));
// console.log(obj1.property1)

// var buffer = new ArrayBuffer(8)
// console.log(ArrayBuffer.isView(buffer))
// var v = new Int32Array(buffer);
// console.log(ArrayBuffer.isView(v))
// console.log(v)

// var buffer = new ArrayBuffer(8)
// var i16 = new Int16Array(buffer, 2)
// console.log(i16)

// var x = new Int8Array([1,1]);
// var y = new Int8Array(x);
// console.log(x)
// console.log(y)
// console.log('-----------------')
// x[0] = 122;
// console.log(x)
// console.log(y)

// arr = [1,2,3,66];
// arr2 = ['chen', 'str'];
// console.log(arr.find((val, index)=>index===2))
// console.log(arr.filter((value)=>value>2))
// console.log(arr2.find((value)=>value==='str'))
// console.log(Object.keys(arr2))
// console.log(arr.reduce((prev, curr, cuindex, arr)=>{
//     if(cuindex == 0){
//         return prev + curr;
//     }else{
//         return 1;
//     }
// }))

// console.log(arr.filter((val)=>{
//     if(val>2){
//         return val;
//     }
// }))

// function filter(fn)
// {
//     res = [];
//     for(let i = 0; i<arr.length; i++){
//         let s = fn(arr[i])
//         if(s){
//             res.push(s)
//         }
//     }
//     return res;
// }
// console.log(filter((val)=>{
//     if(val>2){
//         return val;
//     }
// }))

// let iters = arr.values()
// for (const iterator of iters) {
//     console.log(iterator)
// }

// let iters = arr.keys()
// console.log(iters)
// for (const iterator of iters) {
//     console.log(iterator)
// }

// console.log(arr.some((val)=>{
//     if(val>100){
//         return true;
//     }else{
//         return false;
//     }
// }))

// const letters = ['a', 'b', 'c'];
// const numbers = [1,2,3];
// var s = letters.concat(numbers)
// console.log(s);
// console.log(letters);

// let arr32 = Uint32Array.of(0x12345678);
// console.log(arr32.buffer);

// var int8 = new Int8Array(1)
// int8[0] = -130
// console.log(int8[0])

// var a = new Int16Array(8);
// console.log(a.length)
// console.log(a.byteLength)

// let ui8 = Uint8Array.of(0,1,2);
// var s = ui8.slice(-2,-1)
// console.log(ui8)
// console.log(s)

// var ui16 = Uint16Array.from(Uint8Array.of(0,1,2));
// console.log(ui16);
// console.log(ui16.byteLength);

// var s = Int8Array.of(254)
// console.log(s)

// var buffer = new ArrayBuffer(24)
// var dv = new DataView(buffer)
// dv.setInt32(0,25)
// dv.setFloat32(4, 0.24)
// var v1 = dv.getInt32(0);
// var v2 = dv.getFloat32(4)
// console.log(v1)
// console.log(v2)

// var a = SIMD.Float32x4(-1,-2,0,0)

// var person = {
//     firstName: 'bill',
//     lastName: 'gates',
//     language: '',
//     set lang(lang){
//         this.language = lang.toUpperCase();
//     }
// }

// person.lang = 'enuk'
// console.log(person.language)

// import * as m from './test'
// console.log(counter)
// incCounter();
// console.log(counter)

// var mod = require('./test')
// console.log(mod.counter)
// mod.incCounter()
// console.log(mod.counter)

// var f = function(){
//     console.log(this);
// }()

// var proxy = new Proxy({name: 'chen'}, {
//     // get: function(target, property){
//     //     // return 3;
//     // }
// })

// console.log(proxy.name);
// console.log(proxy.title);

// var obj = {name: 'chen'};
// console.log('chen' in obj);

// var person = {
//     name: 'chen'
// };
// var proxy = new Proxy(person, {
//     get: function(target, property){
//         if(property in target){
//             return target[property];
//         }else{
//             throw new ReferenceError("property \"" + property + "\" does not exist.")
//         }
//     }
// })

// console.log(proxy.name);
// console.log(proxy.age);

// var arr = [1,2,3,4];
// var resu = arr.reduce((prev, curr)=>prev + curr, 0);
// console.log(resu);

// let validator = {
//     set: function(obj, prop, value){
//         if(prop === 'age'){
//             if(!Number.isInteger(value)){
//                 throw new TypeError('the age is not an integer');
//             }
//             if(value > 200){
//                 throw new RangeError('the age seems invalid');
//             }
//         }
//         obj[prop] = value;
//     }
// };

// let person = new Proxy({}, validator);
// person.age = 100;
// console.log(person.age);
// person.age = 300;

// var twice = {
//     apply(target, ctx, args){
//         return Reflect.apply(...arguments) * 2;
//     }
// };
// function sum(left, right){
//     return left + right;
// };
// var proxy = new Proxy(sum, twice);
// console.log(proxy(1,2));
// console.log(proxy.call(null, 5,6));
// console.log(proxy.apply(null, [7,8]));

// var adds = [1,2,3].join(', ');
// console.log(adds)

// var p = new Proxy(function(){}, {
//     construct: function(target, args){
//         console.log('called:' + args.join(', '));
//         return {value: args[0] * 10};
//     }
// });

// var pp = new p(2);
// console.log(pp);

// var target = {prop1: 'foo'};
// delete target.prop1;
// console.log(target);

// var str = 'chen玩我';
// console.log(str.substring(1,5))
// console.log(str.slice(1,5))
// console.log(str)

// let joker = {name: 'joker'};
// let parent = {
//     name: 'parent',
//     show(){
//         console.log(this.name);
//     }
// }
// Object.setPrototypeOf(joker, parent);
// let joker2 = Object.create(joker);
// joker2.name = 'joker2';
// // joker.show();
// // joker2.show();

// var handler = {
//     defineProperty(target, key, descriptor){
//         return false;
//     }
// }
// var proxy = new Proxy(joker2, handler);
// console.log(Object.getPrototypeOf(proxy));
// proxy.age = 100;

// var handler = {
//     defineProperty(target, key, descriptor) {
//         console.log(key);
//         return false;
//     }
// };
// var target = {};
// var proxy = new Proxy(target, handler);
// proxy.foo = 'bar'
// console.log(proxy);

// var handler = {
//     getOwnPropertyDescriptor(target, key){
//         if(key[0] === '_'){
//             return;
//         }
//         return Object.getOwnPropertyDescriptor(target, key);
//     }
// };

// var target = {_foo: 'bar', baz: 'tar'};
// var proxy = new Proxy(target, handler);
// console.log(Object.getOwnPropertyDescriptor(proxy, 'wat'))
// console.log(Object.getOwnPropertyDescriptor(proxy, '_foo'))
// console.log(Object.getOwnPropertyDescriptor(proxy, 'baz'))


// let joker = {name: 'joker'};
// let parent = {
//     name: 'parent',
//     show(){
//         console.log(this.name);
//     }
// }
// Object.setPrototypeOf(joker, parent);
// let joker2 = Object.create(joker);
// console.log(joker2)
// console.log(Object.keys(joker2))
// joker2.title = 'joker2';
// console.log(joker2)
// console.log(Object.keys(joker2))

// let obj = {name: 'chen'};
// let proxy = new Proxy(obj, {});
// console.log(proxy['name']);
// Object.setPrototypeOf(proxy, {});

// var it = makeIterator(['a', 'b']);
// console.log(it.next())
// console.log(it.next())
// console.log(it.next())

// function makeIterator(array) {
//     var nextIndex = 0;
//     return {
//         next: function(){
//             return nextIndex < array.length ? 
//             {value: array[nextIndex++], done: false} : 
//             {value: undefined, done: true};
//         }
//     }
// }

// var obj = {};
// console.log(obj['name']);
// console.log(undefined == false);

// let arr = ['a', 'b', 'c'];
// let iter = arr[Symbol.iterator]();
// console.log(iter.next());
// console.log(iter.next());
// console.log(iter.next());
// console.log(iter.next());

// class RangeIterator{
//     constructor(start, stop){
//         this.value = start;
//         this.stop = stop;
//     }

//     [Symbol.iterator]() {return this;}

//     next(){
//         var value = this.value;
//         if(value < this.stop){
//             this.value++;
//             return {done: false, value: value};
//         }else{
//             return {done: true, value: undefined};
//         }
//     }
// }

// function range(start, stop){
//     return new RangeIterator(start, stop);
// }

// for(let value of range(0,3)){
//     console.log(value);
// }
// console.log(window);

// let obj = {
//     data: ['hello', 'world'],
//     [Symbol.iterator](){
//         const self = this;
//         let index = 0;
//         return {
//             next(){
//                 if(index < self.data.length){
//                     return{
//                         value: self.data[index++],
//                         done: false
//                     };
//                 }else{
//                     return {value: undefined, done: true};
//                 }
//             }
//         }
//     }
// }

// for (const iterator of obj) {
//     console.log(iterator);
// }

// let iterable = {
//     // 0:'a',
//     1:'b',
//     // 2:'c',
//     3:'d',
//     length:3,
//     [Symbol.iterator]: Array.prototype[Symbol.iterator]
// };
// for (const item of iterable) {
//     console.log(item);
// }

// let obj = {
//     data: ['hello', 'world'],
//     [Symbol.iterator](){
//         const self = this;
//         let index = 0;
//         return {
//             next(){
//                 if(index < self.data.length){
//                     return{
//                         value: self.data[index++],
//                         done: false
//                     };
//                 }else{
//                     return {value: undefined, done: true};
//                 }
//             }
//         }
//     }
// }

// for (const iterator of obj) {
//     console.log(iterator);
// }
// var s = [...obj]
// console.log(s)
// console.log(typeof s)
// console.log(typeof [])

// var sostr = 'hi';
// console.log(typeof sostr[Symbol.iterator])

// var iter = sostr[Symbol.iterator]();
// console.log(iter.next())
// console.log(iter.next())
// console.log(iter.next())

// var myIterable = {}
// myIterable[Symbol.iterator] = function* (){
//     yield 1;
//     yield 2;
//     yield* [3,4,5];
// }
// var s = [...myIterable]
// console.log(s)

// var es5 = {
//     title: 'es'
// }
// var es6 = {
//     edition: 6,
//     committee: 'TC39',
//     standard: 'ECMA-262'
// };
// Object.setPrototypeOf(es6, es5);
// // for (const key in es6) {
// //     // if (es6.hasOwnProperty(key)) {
// //         const element = es6[key];
// //         console.log(key + ": " + element);
// //     // }
// // }

// for (const key of Object.entries(es6)) {
//     console.log(key);
// }

// var object = [1,4,6,7]
// for (const key in object) {
//     if (object.hasOwnProperty(key)) {
//         const element = object[key];
//         if (element>5){
//             continue;
//         }
        
//         console.log(key + ': ' + element);
        
//     }
// }
// console.log('-------------')

// var fs = require("fs")

// fs.readFile('test1.py', function(err, data){
//     if(err){
//         return console.error(err);
//     }
//     console.log(typeof data);
//     console.log("async read: ", data.toString());
// })

// var readFile = require('fs-readfile-promise');
// var co = require('co');
// var b = readFile('test1.py').then(function(data){
//     console.log(data.toString())
// }).then(function(){
//     return readFile('test.html');
// }).then(function(data){
//     console.log(data.toString());
// }).catch(function(err){
//     console.log(err);
// })

// var fetch = require('node-fetch')

// function* gen(){
//     var url = 'https://api.github.com/users/github';
//     var result = yield fetch(url);
//     console.log(result.bio)
// }

// var g = gen();
// var result = g.next();

// result.value.then(function(data){
//     return data.json();
// }).then(function(data){
//     g.next(data);
// })

// var url = 'https://api.github.com/users/github';
// fetch(url).then((data)=>data.json()).then((data)=>{
//     console.log(data.bio);
// })

// var Thunk = function(fn){
//     return function(...args){
//         return function(callback){
//             console.log(this);
//             return fn.call(this, ...args, callback)
//         }
//     }
// }

// function f(a, cb){
//     cb(a);
// }

// let ft = Thunk(f)
// let log = console.log.bind(console);
// ft(1)(log)

// var gen = function* (){
//     var f1 = yield readFile('test.html');
//     var f2 = yield readFile('test1.py');
//     console.log(f1.toString());
//     console.log(f2.toString());
// };

// co(gen).then(function(data){
//     console.log('finished:', data);
// })

// var fs = require('fs')

// var readFile = function(fileName){
//     return new Promise(function(resolve, reject){
//         fs.readFile(fileName, function(error, data){
//             if(error) return reject(error);
//             resolve(data);
//         })
//     })
// }

// var gen = function* (){
//     var f1 = yield readFile('test1.py')
//     var f2 = yield readFile('test.html')
//     console.log(f1.toString())
//     console.log(f2.toString())
// }

// function run(gen){
//     var g = gen()

//     function next(data){
//         var result = g.next(data);
//         if(result.done) return result.value;
//         result.value.then(function(data){
//             next(data);
//         })
//     }

//     next();
// }

// run(gen);

// console.log(typeof null)

// var fs = require('fs')
// var co = require('co')

// var readFile = function(fileName){
//     return new Promise(function(resolve, reject){
//         fs.readFile(fileName, function(error, data){
//             if(error) return reject(error);
//             resolve(data);
//         })
//     })
// }

// co(function* (){
//     var values = ['test1.py', 'test.html']
//     yield values.map(so)
// }).then((data)=>{
//     console.log(data)
// })

// function* so(x){
//     var f = yield readFile(x)
//     console.log(f.toString())
//     return 'hhh'
// }

// async function f(){
//     return 'hello world'
// }
// f().then(v=>console.log(v))

// async function f(){
//     throw new Error('wwwwwwwwwwwwwwwww');
// }

// f().then(v=>{}, e=>console.error('e'))

// async function f(){
//     try{
//         await Promise.reject('error')
//     }catch(e){
//         console.log(e)
//     }
//     return await Promise.resolve('success')
// }

// f().then(v=>console.log(v))

// var fs = require('fs')

// var readFile = function(fileName){
//     return new Promise(function(resolve, reject){
//         fs.readFile(fileName, function(error, data){
//             if(error) return reject(error);
//             resolve(data);
//         })
//     })
// }

// async function f(){
//     return await readFile('test.html')
// }
// f().then(v=>console.log(v.toString()))

// function spawn(genF){
//     return new Promise(function(resolve, reject){
//         var gen = genF()
//         function step(nextF){
//             try{
//                 var next = nextF();
//             }catch(e){
//                 return reject(e)
//             }
//             if(next.done){
//                 return resolve(next.value);
//             }
//             Promise.resolve(next.value).then(function(v){
//                 step(function(){return gen.next(v);})
//             }, function(e){
//                 step(function(){return gen.throw(e);})
//             })
//         }
//         step(function(){return gen.next(undefined);})
//     })
// }

// function fn(){
//     return spawn(function* (){
//         var f = yield readFile('test.html')
//         return f
//     })
// }

// fn().then(v=>console.log(v.toString()))

// function* f(){
//     var f1 = yield 1
//     console.log(f1)
//     var f2 = yield 2
//     console.log(f2)
//     return 3
// }

// var ff = f()
// var a1 = ff.next('a')
// var a2 = ff.next('b')
// var a3 = ff.next('c')
// console.log(a1)
// console.log(a2)
// console.log(a3)

// function timeout(ms){
//     return new Promise((resolve)=>{
//         setTimeout(resolve, ms)
//     })
// }

// async function asyncPrint(value, ms){
//     await timeout(ms)
//     console.log(value)
// }

// asyncPrint('hello world', 5000)

// async function f(){
//     var date = new Date()
//     var se = date.getSeconds()
//     var mi = date.getMilliseconds()
//     let [foo, bar] = await Promise.all([readFile('Game_atlas0.png'), readFile('test.js')])
//     // var foo = await readFile('Game_atlas0.png')
//     // var dd = await readFile('test.js')
//     var date2 = new Date()
//     var se2 = date2.getSeconds()
//     var mi2 = date2.getMilliseconds()
//     console.log(se2 - se)
//     console.log(mi2 - mi)
// }
// f()

// var await = 1
// function f(val){
//     return val * val
// }
// function th(val){
//     throw new Error(val * val)
// }
// var arr = [f, f, th, f]
// async function ch(arr){
//     var ret = null
//     try{
//         var i = 1
//         for(var anim of arr){
//             ret = await anim(i++)
//             console.log(ret)
//         }
//     }catch(e){
//         console.log(e)
//     }
//     return ret
// }

// var s = Promise.resolve()
// s.then(()=>{return ch(arr)}).then(v=>console.log(v))
// console.log(re)

// async function* gen1() {
//     yield 'a';
//     yield 'b';
//     return 2;
//   }

// var g = gen1()
// g.next().then(val => {
//     console.log(val)
// })
// g.next().then(val => {
//     console.log(val)
// })
// g.next().then(val => {
//     console.log(val)
// })

// var getJSON = function(url){
//     var promise = new Promise(function(resolve, reject){
//         var client = new XMLHttpRequest();
//         client.open("GET", url)
//         client.onreadystatechange = handler
//         client.responseType = 'json'
//         client.setRequestHeader("Accept", "application/json")
//         client.send()

//         function handler(){
//             if(this.readyState !== 4){
//                 return;
//             }
//             if(this.status === 200){
//                 resolve(this.response);
//             }else{
//                 reject(new Error(this.statusText))
//             }
//         }
//     })
//     return promise
// }

// getJSON("./package.json").then(json => console.log(JSON.stringify(json)),
// error=>console.error('error: ', error))

// var p1 = new Promise(function(resolve, reject){
//     setTimeout(()=>reject(new Error('fail')), 3000)
// })

// var p2 = new Promise(function(resolve, reject){
//     setTimeout(()=>{
//         console.log("p2")
//         resolve(p1)}, 1000)
// })

// p2.then(result=>console.log('result')).catch(error=>console.log(error))

// var promise = new Promise(function(resolve, reject){
//     resolve('ok');
//     // throw new Error('test');
// })
// promise.then(function(){
//     console.log("hhh")
//     throw new Error('test')
//     }).
//     then(function(value){
//     console.log(value)
    
//     }, function(error){console.log(error)})
//     // .catch(function(error){console.log(error)})

// var someAsyncThing = function(){
//     return new Promise(function(resolve, reject){
//         resolve(x + 2);
//     })
// }
// someAsyncThing().then(function(){console.log('eve')})

// Promise.resolve().then(function(value){
//     console.log('carry on')
//     throw new Error('error')
// }).catch(function(error){
//     console.log(error)
// })

// var someAsyncThing = function(){
//     return new Promise(function(resolve, reject){
//         console.log("111");
//         resolve('value')
//     })
// }

// someAsyncThing().then(function(value){
//     console.log(value)
// })

// console.log("222")

// var promises = [2,3,4,55].map(function(value){
//     return new Promise(function(resolve, reject){
//         setTimeout(()=>resolve(value), 5500 - value * 100)
//     })
// })
// Promise.race(promises).then(function(data){
//     console.log(data)
// })

// setTimeout(function(){
//     console.log('three')
// }, 0)
// Promise.resolve().then(function(){
//     console.log('two')
// })
// console.log('one')

// function getFoo(){
//     return new Promise(function(resolve, reject){
//         resolve('foo')
//     })
// }
// var g = function* (){
//     try{
//         var foo = yield getFoo();
//         console.log(foo)
//         var foo = yield getFoo();
//         console.log(foo)
//     }catch(e){
//         console.log(e);
//     }
// }

// function run(generator){
//     var it = generator();
//     function go(result){
//         if(result.done) return result.value;
//         return result.value.then(function(value){
//             return go(it.next(value));
//         }, function(error){
//             return go(it.throw(error))
//         })
//     }
//     go(it.next());
// }
// run(g)

// const f = () => console.log('now')
// Promise.try(f);
// console.log('next')

// var t = typeof 1
// console.log(t)
// var b = true
// var arr = [1,b?null:2,3]
// console.log(arr)

var a = [1,3,2].sort();
console.log(a)