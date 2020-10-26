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

var f = function(){
    console.log(this);
}()