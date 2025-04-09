> **March 14th, 2025**  **18:35:45** 
> **Topics:** [[Ruby L3]] 
> **Tags:** #CS 
---

**Ruby Level 2: Intermediate to Advanced Ruby Programming**

  

**Introduction**

  

In **Ruby Level 2**, we explore **advanced programming concepts**, focusing on **metaprogramming, web development, APIs, and database interactions**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced Object-Oriented Programming (Modules, Mixins, Metaprogramming)**

✅ **Concurrency & Multithreading in Ruby**

✅ **Working with APIs (HTTP Requests, JSON Parsing)**

✅ **Database Management with ActiveRecord & PostgreSQL**

✅ **Web Development with Sinatra & Ruby on Rails**

✅ **Testing in Ruby (RSpec & MiniTest)**

✅ **Building a RESTful API in Ruby**

  

By the end of this lesson, you will be able to **build scalable Ruby applications and APIs**.

---

**1. Advanced Object-Oriented Programming**

  

**1.1. Modules & Mixins**

  

Ruby **doesn’t support multiple inheritance**, but we can **share behavior across classes using mixins**.

```
module Logger
  def log(message)
    puts "[LOG] #{message}"
  end
end

class User
  include Logger

  def create
    log("User created")
  end
end

user = User.new
user.create  # => [LOG] User created
```

**1.2. Metaprogramming (Dynamic Methods)**

  

Metaprogramming allows Ruby to **modify or create methods dynamically**.

  

**Define Methods Dynamically**

```
class Dynamic
  def self.create_method(name)
    define_method(name) do
      puts "Method #{name} called"
    end
  end
end

Dynamic.create_method(:hello)
obj = Dynamic.new
obj.hello  # => Method hello called
```

  

---

**2. Concurrency & Multithreading**

  

**2.1. Creating Threads**

  

Ruby **supports multithreading** but has a **Global Interpreter Lock (GIL)**, meaning only one thread runs at a time for CPU-bound tasks.

```
threads = []

5.times do |i|
  threads << Thread.new { puts "Thread #{i} is running" }
end

threads.each(&:join)
```

**2.2. Parallel Processing with fork**

  

Use fork to create **separate processes** (useful for CPU-heavy tasks).

```
fork { puts "This is a child process" }
puts "This is the parent process"
```

  

---

**3. Working with APIs**

  

**3.1. Making HTTP Requests**

```
require 'net/http'
require 'json'

url = URI("https://jsonplaceholder.typicode.com/posts/1")
response = Net::HTTP.get(url)
puts JSON.parse(response)["title"]
```

**3.2. Sending Data (POST Request)**

```
require 'net/http'

url = URI("https://jsonplaceholder.typicode.com/posts")
data = { title: "Hello", body: "Ruby API call" }.to_json

response = Net::HTTP.post(url, data, { "Content-Type" => "application/json" })
puts response.body
```

  

---

**4. Database Management with ActiveRecord & PostgreSQL**

  

**4.1. Setting Up ActiveRecord**

  

Install ActiveRecord:

```
gem install activerecord sqlite3
```

**4.2. Connecting to a Database**

```
require 'active_record'

ActiveRecord::Base.establish_connection(
  adapter: 'sqlite3',
  database: 'db.sqlite3'
)
```

**4.3. Defining a Model**

```
class User < ActiveRecord::Base
end
```

**4.4. Performing CRUD Operations**

```
User.create(name: "Alice")
user = User.find(1)
user.update(name: "Bob")
user.destroy
```

  

---

**5. Web Development with Sinatra & Rails**

  

**5.1. Creating a Sinatra Web App**

```
require 'sinatra'

get '/' do
  "Hello, Sinatra!"
end
```

Run:

```
ruby app.rb
```

Visit http://localhost:4567 in your browser.

  

**5.2. Introduction to Ruby on Rails**

  

Rails is **a powerful web framework** that follows the **MVC (Model-View-Controller) pattern**.

  

**Install Rails**

```
gem install rails
```

**Create a New Rails App**

```
rails new myapp
cd myapp
rails server
```

**Generate a Controller**

```
rails generate controller Home index
```

Edit app/controllers/home_controller.rb:

```
class HomeController < ApplicationController
  def index
    render plain: "Hello, Rails!"
  end
end
```

  

---

**6. Testing in Ruby**

  

**6.1. Writing Unit Tests with RSpec**

  

Install RSpec:

```
gem install rspec
```

Create a test file spec/calculator_spec.rb:

```
require_relative '../calculator'
require 'rspec'

describe "Calculator" do
  it "adds two numbers" do
    expect(2 + 3).to eq(5)
  end
end
```

Run tests:

```
rspec
```

  

---

**7. Building a RESTful API in Ruby**

  

**7.1. Creating a Sinatra API**

```
require 'sinatra'
require 'json'

users = [{ id: 1, name: "Alice" }]

get '/users' do
  content_type :json
  users.to_json
end

post '/users' do
  data = JSON.parse(request.body.read)
  users << { id: users.size + 1, name: data["name"] }
  status 201
end
```

Run:

```
ruby api.rb
```

Use curl to interact:

```
curl http://localhost:4567/users
```

  

---

**8. Final Project: Full-Stack Ruby on Rails App**

  

**8.1. Generate a New Rails App**

```
rails new blog
cd blog
rails generate scaffold Post title:string body:text
rails db:migrate
rails server
```

**8.2. Create a Controller**

```
rails generate controller Posts index
```

Modify app/controllers/posts_controller.rb:

```
class PostsController < ApplicationController
  def index
    @posts = Post.all
  end
end
```

**8.3. Add Routes**

  

Modify config/routes.rb:

```
Rails.application.routes.draw do
  resources :posts
  root "posts#index"
end
```

Visit http://localhost:3000/posts in the browser.

---

**Conclusion**

  

**What You Learned in Ruby Level 2:**

  

✅ **Advanced OOP (Modules, Mixins, Metaprogramming)**

✅ **Concurrency & Multithreading (Threads, Forks)**

✅ **Working with APIs (HTTP Requests, JSON Parsing)**

✅ **Database Management with ActiveRecord & PostgreSQL**

✅ **Web Development with Sinatra & Ruby on Rails**

✅ **Testing in Ruby (RSpec & MiniTest)**

✅ **Built a RESTful API in Ruby**

  

Now, you’re ready for **Ruby Level 3**, where we explore **Microservices, Cloud Deployment, WebSockets, and AI with Ruby!** 🚀