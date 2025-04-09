> **March 15th, 2025**  **19:05:14** 
> **Topics:** [[MATLAB L2]] 
> **Tags:** #CS 
---

**MATLAB Level 1: Introduction to MATLAB Programming**

  

**Introduction**

  

MATLAB (**Matrix Laboratory**) is a **high-level programming language** widely used for **numerical computing, data analysis, visualization, and engineering applications**.

  

**What You’ll Learn in This Lesson:**

  

✅ **MATLAB Basics (Syntax, Variables, Data Types, Operators)**

✅ **Vectors, Matrices & Array Operations**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Functions & Scripts**

✅ **Data Visualization (Plots, Graphs, Histograms)**

✅ **File Handling (Reading/Writing Files, CSV, Excel)**

✅ **Building a Simple MATLAB Application**

  

By the end of this lesson, you will be able to **write basic MATLAB scripts, manipulate matrices, and visualize data effectively**.

---

**1. Setting Up MATLAB**

  

**1.1. Installing MATLAB**

• Download MATLAB from [mathworks.com](https://www.mathworks.com/products/matlab.html).

• Alternatively, use **MATLAB Online** or **GNU Octave** (open-source alternative).

  

**1.2. Running MATLAB Code**

• **MATLAB Command Window**: Type commands interactively.

• **Script (.m file)**: Create a new script (script.m) and run:

```
run('script.m')
```

  

---

**2. MATLAB Basics: Variables, Data Types & Operators**

  

**2.1. Variables & Assignment**

```
x = 10;      % Integer
y = 3.14;    % Floating-point
name = 'Alice'; % String
```

**2.2. Data Types**

```
a = 5;        % Integer
b = 3.5;      % Double (Floating point)
c = true;     % Boolean
d = 'Hello';  % String
```

**2.3. Operators**

```
x = 10; y = 3;
sum = x + y;        % Addition
diff = x - y;       % Subtraction
product = x * y;    % Multiplication
quotient = x / y;   % Division
remainder = mod(x, y); % Modulus
```

  

---

**3. Vectors, Matrices & Array Operations**

  

**3.1. Creating Vectors & Matrices**

```
v = [1 2 3 4 5];      % Row vector
w = [1; 2; 3; 4; 5];  % Column vector

A = [1 2 3; 4 5 6; 7 8 9]; % 3x3 Matrix
```

**3.2. Accessing Elements**

```
x = A(2,3);  % Access row 2, column 3
row = A(2,:);  % Extract row 2
col = A(:,3);  % Extract column 3
```

**3.3. Matrix Operations**

```
B = A + 2;    % Add 2 to each element
C = A * A;    % Matrix multiplication
D = A .* A;   % Element-wise multiplication
E = A.^2;     % Element-wise squaring
```

  

---

**4. Control Flow (If-Else, Loops, Switch)**

  

**4.1. If-Else Statements**

```
x = 10;
if x > 5
    disp('x is greater than 5');
elseif x == 5
    disp('x is exactly 5');
else
    disp('x is less than 5');
end
```

**4.2. For Loop**

```
for i = 1:5
    disp(['Iteration: ' num2str(i)]);
end
```

**4.3. While Loop**

```
count = 0;
while count < 3
    disp(['Count: ' num2str(count)]);
    count = count + 1;
end
```

**4.4. Switch Case**

```
grade = 'A';
switch grade
    case 'A'
        disp('Excellent');
    case 'B'
        disp('Good');
    case 'C'
        disp('Average');
    otherwise
        disp('Fail');
end
```

  

---

**5. Functions & Scripts**

  

**5.1. Creating Functions**

  

Save this as squareNumber.m:

```
function result = squareNumber(x)
    result = x^2;
end
```

Call the function:

```
y = squareNumber(5);
disp(y);
```

**5.2. Anonymous Functions**

```
square = @(x) x^2;
disp(square(4));
```

  

---

**6. Data Visualization (Plots, Graphs, Histograms)**

  

**6.1. Line Plot**

```
x = linspace(0, 10, 100);
y = sin(x);
plot(x, y, 'r--');  % Red dashed line
xlabel('X-axis');
ylabel('Y-axis');
title('Sine Function');
grid on;
```

**6.2. Scatter Plot**

```
x = rand(1, 100);
y = rand(1, 100);
scatter(x, y, 'b');
title('Scatter Plot');
```

**6.3. Bar Graph**

```
x = ["Apples", "Bananas", "Cherries"];
y = [10, 20, 15];
bar(y);
set(gca, 'xticklabel', x);
title('Fruit Sales');
```

**6.4. Histogram**

```
data = randn(1, 1000);
histogram(data, 20);
title('Histogram of Random Data');
```

  

---

**7. File Handling (Reading/Writing Files, CSV, Excel)**

  

**7.1. Writing to a File**

```
fileID = fopen('output.txt', 'w');
fprintf(fileID, 'Hello, MATLAB!');
fclose(fileID);
```

**7.2. Reading a File**

```
fileID = fopen('output.txt', 'r');
data = fscanf(fileID, '%s');
disp(data);
fclose(fileID);
```

**7.3. Working with CSV Files**

```
data = [1 2 3; 4 5 6; 7 8 9];
csvwrite('data.csv', data);

readData = csvread('data.csv');
disp(readData);
```

**7.4. Working with Excel Files**

```
xlswrite('data.xlsx', data);
readExcel = xlsread('data.xlsx');
disp(readExcel);
```

  

---

**8. Building a Simple MATLAB Application**

  

**8.1. Generate & Plot a Sine Wave**

```
function sineWaveApp()
    f = input('Enter frequency (Hz): ');
    t = 0:0.01:1;
    y = sin(2*pi*f*t);
    
    figure;
    plot(t, y, 'b');
    xlabel('Time (s)');
    ylabel('Amplitude');
    title(['Sine Wave - ' num2str(f) ' Hz']);
end
```

Run:

```
sineWaveApp();
```

  

---

**Conclusion**

  

**What You Learned in MATLAB Level 1:**

  

✅ **MATLAB Basics (Syntax, Variables, Data Types, Operators)**

✅ **Vectors, Matrices & Array Operations**

✅ **Control Flow (If-Else, Loops, Switch Statements)**

✅ **Functions & Scripts**

✅ **Data Visualization (Plots, Graphs, Histograms)**

✅ **File Handling (Reading/Writing Files, CSV, Excel)**

✅ **Built a Simple MATLAB Application**

  

Now, you’re ready for **MATLAB Level 2**, where we explore **Advanced Signal Processing, Machine Learning, Image Processing, and Simulink!** 🚀