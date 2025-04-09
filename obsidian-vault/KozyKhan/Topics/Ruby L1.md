> **March 14th, 2025**  **18:35:12** 
> **Topics:** [[Ruby L2]] 
> **Tags:** #CS 
---

**Ruby Level 1: From Beginner to Intermediate in One Lesson**

  

**Introduction**

  

Ruby is a **dynamic, object-oriented programming language** known for **simplicity and productivity**. It is widely used in **web development (Ruby on Rails), scripting, and automation**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Ruby Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops)**

✅ **Methods & Blocks**

✅ **Object-Oriented Programming (Classes, Objects, Inheritance)**

✅ **File Handling (Reading & Writing Files)**

✅ **Ruby Gems & Package Management**

✅ **Basic Web Development with Sinatra**

✅ **Building a Simple Ruby Application**

  

By the end of this lesson, you will be able to **write functional Ruby programs and build simple web applications**.

---

**1. Setting Up Ruby**

  

**1.1. Installing Ruby**

  

Install Ruby using:

• **macOS/Linux:**

```
brew install ruby
```

  

• **Windows:** Download from [rubyinstaller.org](https://rubyinstaller.org/).

  

**1.2. Running Ruby Code**

• **Interactive Mode (IRB):**

```
irb
```

  

• **Executing a Script:**

```
ruby my_script.rb
```

  

---

**2. Ruby Basics: Variables, Data Types & Operators**

  

**2.1. Variables & Data Types**

```
age = 25           # Integer
pi = 3.14          # Float
is_ruby_fun = true # Boolean
name = "Alice"     # String
fruits = ["apple", "banana", "cherry"] # Array
person = { name: "Alice", age: 25 } # Hash (Dictionary)
```

**2.2. Operators**

```
a, b = 10, 3
puts a + b  # Addition
puts a - b  # Subtraction
puts a * b  # Multiplication
puts a / b  # Division
puts a % b  # Modulus
puts a ** b # Exponentiation
```

  

---

**3. Control Flow (If-Else, Loops)**

  

**3.1. If-Else Statement**

```
age = 18
if age >= 18
  puts "You are an adult."
else
  puts "You are a minor."
end
```

**3.2. Loops**

  

**For Loop**

```
for i in 1..5
  puts "Iteration: #{i}"
end
```

**While Loop**

```
count = 0
while count < 5
  puts count
  count += 1
end
```

**Do-While Loop**

```
num = 0
begin
  puts "Number: #{num}"
  num += 1
end while num < 5
```

  

---

**4. Methods & Blocks**

  

**4.1. Defining a Method**

```
def greet(name)
  "Hello, #{name}"
end

puts greet("Alice")
```

**4.2. Method with Default Arguments**

```
def greet(name = "Guest")
  "Hello, #{name}"
end

puts greet
puts greet("Bob")
```

**4.3. Blocks & Yield**

```
def repeat_twice
  yield
  yield
end

repeat_twice { puts "Hello!" }
```

  

---

**5. Object-Oriented Programming (OOP)**

  

**5.1. Defining a Class & Creating an Object**

```
class Car
  attr_accessor :brand, :speed

  def initialize(brand, speed)
    @brand = brand
    @speed = speed
  end

  def drive
    puts "#{@brand} is driving at #{@speed} km/h"
  end
end

my_car = Car.new("Toyota", 120)
my_car.drive
```

**5.2. Inheritance**

```
class Animal
  def speak
    puts "Animal makes a sound"
  end
end

class Dog < Animal
  def speak
    puts "Woof!"
  end
end

dog = Dog.new
dog.speak
```

  

---

**6. File Handling (Reading & Writing Files)**

  

**6.1. Writing to a File**

```
File.open("example.txt", "w") do |file|
  file.puts "Hello, file!"
end
```

**6.2. Reading from a File**

```
File.open("example.txt", "r") do |file|
  puts file.read
end
```

  

---

**7. Ruby Gems & Package Management**

  

**7.1. Installing Gems**

```
gem install sinatra
```

**7.2. Using a Gem in a Script**

```
require 'date'
puts Date.today
```

  

---

**8. Basic Web Development with Sinatra**

  

Sinatra is a lightweight web framework for Ruby.

  

**8.1. Installing Sinatra**

```
gem install sinatra
```

**8.2. Creating a Simple Web App**

```
require 'sinatra'

get '/' do
  "Hello, Sinatra!"
end
```

Run the app:

```
ruby my_app.rb
```

Then visit http://localhost:4567 in a browser.

---

**9. Final Project: Building a Simple To-Do List**

  

**9.1. Ruby Code (todo.rb)**

```
tasks = []

loop do
  puts "To-Do List:"
  tasks.each_with_index { |task, index| puts "#{index + 1}. #{task}" }
  
  puts "Enter a task (or 'exit' to quit):"
  input = gets.chomp
  break if input.downcase == "exit"
  
  tasks << input
end
```

  

---

**10. Conclusion**

  

**What You Learned in Ruby Level 1:**

  

✅ **Ruby Basics (Syntax, Variables, Data Types, Operators)**

✅ **Control Flow (If-Else, Loops)**

✅ **Methods & Blocks**

✅ **Object-Oriented Programming (Classes, Objects, Inheritance)**

✅ **File Handling (Reading & Writing Files)**

✅ **Ruby Gems & Package Management**

✅ **Basic Web Development with Sinatra**

✅ **Built a Simple Ruby Application**

  

Now, you’re ready for **Ruby Level 2**, where we explore **Advanced OOP, Web APIs, Metaprogramming, and Ruby on Rails!** 🚀