// code reuse in js

// by Object method
const person = {
    name: 'John',
    greet() {
      console.log(`Hello, ${this.name}!`);
    },
  };

person.greet();

// by Classes
class Greeter {
    constructor(name) {
      this.name = name;
    }
  
    greet() {
      console.log(`Hello, ${this.name}!`);
    }
  }
  
const john = new Greeter('John');
const alice = new Greeter('Alice');

john.greet();
alice.greet();

//  by Module System

// math.js
import { add } from './math.js';  
console.log(add(2, 3)); // 5
  