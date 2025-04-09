> **March 15th, 2025**  **19:06:23** 
> **Topics:** [[MATLAB L3]] 
> **Tags:** #CS 
---

**MATLAB Level 2: Intermediate to Advanced MATLAB Programming**

  

**Introduction**

  

Now that you have learned the **basics of MATLAB**, it’s time to dive deeper into **advanced topics like signal processing, machine learning, image processing, and Simulink**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced Matrix Operations & Linear Algebra**

✅ **Signal Processing & Fourier Transform (FFT)**

✅ **Machine Learning with MATLAB**

✅ **Image Processing & Computer Vision**

✅ **Simulink for System Modeling**

✅ **Optimization & Numerical Methods**

✅ **Parallel Computing & Performance Optimization**

✅ **Building a Full MATLAB Application**

  

By the end of this lesson, you will be able to **analyze signals, build machine learning models, process images, and optimize MATLAB performance**.

---

**1. Advanced Matrix Operations & Linear Algebra**

  

**1.1. Eigenvalues & Eigenvectors**

```
A = [4 -2; 1 1];
[eigenVectors, eigenValues] = eig(A);
disp(eigenValues);
disp(eigenVectors);
```

**1.2. Solving Linear Systems**

```
A = [3 2; 1 4];
b = [5; 6];
x = A\b;  % Solves Ax = b
disp(x);
```

**1.3. Matrix Inversion**

```
A = [2 3; 5 7];
A_inv = inv(A);
disp(A_inv);
```

  

---

**2. Signal Processing & Fourier Transform**

  

**2.1. Generating & Plotting a Signal**

```
fs = 1000;       % Sampling frequency
t = 0:1/fs:1;    % Time vector
f = 5;           % Frequency of the sine wave
signal = sin(2*pi*f*t);
plot(t, signal);
xlabel('Time (s)');
ylabel('Amplitude');
title('Sine Wave');
```

**2.2. Computing the Fast Fourier Transform (FFT)**

```
Y = fft(signal);
n = length(signal);
frequencies = (0:n-1)*(fs/n);
plot(frequencies, abs(Y));
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('FFT of Sine Wave');
```

**2.3. Designing a Low-Pass Filter**

```
fc = 10;   % Cutoff frequency
[b, a] = butter(4, fc/(fs/2));  % 4th order Butterworth filter
filtered_signal = filter(b, a, signal);
plot(t, filtered_signal);
title('Filtered Signal');
```

  

---

**3. Machine Learning with MATLAB**

  

**3.1. Loading a Dataset**

```
load fisheriris;
data = meas;      % Features
labels = species; % Labels
```

**3.2. Training a Decision Tree Classifier**

```
tree = fitctree(data, labels);
view(tree, 'Mode', 'graph');  % Display tree
```

**3.3. Using a Support Vector Machine (SVM)**

```
svmModel = fitcsvm(data, labels);
prediction = predict(svmModel, data(1, :));
disp(['Predicted label: ', prediction]);
```

**3.4. Performing k-Means Clustering**

```
k = 3;
[idx, centroids] = kmeans(data, k);
gscatter(data(:,1), data(:,2), idx);
title('k-Means Clustering');
```

  

---

**4. Image Processing & Computer Vision**

  

**4.1. Reading & Displaying an Image**

```
img = imread('peppers.png');
imshow(img);
title('Original Image');
```

**4.2. Converting to Grayscale**

```
gray_img = rgb2gray(img);
imshow(gray_img);
title('Grayscale Image');
```

**4.3. Edge Detection using Sobel Filter**

```
edges = edge(gray_img, 'sobel');
imshow(edges);
title('Edge Detection');
```

**4.4. Object Detection using Haar Cascades**

```
faceDetector = vision.CascadeObjectDetector;
bbox = step(faceDetector, img);
imshow(img);
hold on;
rectangle('Position', bbox, 'EdgeColor', 'r', 'LineWidth', 2);
title('Face Detection');
```

  

---

**5. Simulink for System Modeling**

  

**5.1. Opening Simulink**

```
simulink;
```

**5.2. Creating a Simple Model**

1. Open Simulink.

2. Add a **Sine Wave Block** (from Sources).

3. Add a **Scope Block** (from Sinks).

4. Connect the blocks and run the simulation.

---

**6. Optimization & Numerical Methods**

  

**6.1. Finding Minima with fminsearch**

```
f = @(x) x.^2 + 4*x + 5;
x_min = fminsearch(f, 0);
disp(['Minimum at x = ', num2str(x_min)]);
```

**6.2. Solving Differential Equations using ode45**

```
dydt = @(t,y) -2*y + sin(t);
[t, y] = ode45(dydt, [0 10], 1);
plot(t, y);
xlabel('Time');
ylabel('y');
title('Solution of dy/dt = -2y + sin(t)');
```

  

---

**7. Parallel Computing & Performance Optimization**

  

**7.1. Running Loops in Parallel**

```
parpool(4);  % Open 4 parallel workers
parfor i = 1:100
    disp(i);
end
delete(gcp); % Close parallel pool
```

**7.2. Profiling MATLAB Code for Optimization**

```
profile on;
for i = 1:1000
    sqrt(i);
end
profile viewer;
```

  

---

**8. Building a Full MATLAB Application**

  

**8.1. Creating a GUI in MATLAB**

```
app = uifigure;
btn = uibutton(app, 'Text', 'Click Me', 'Position', [100, 100, 100, 50]);
btn.ButtonPushedFcn = @(src, event) disp('Button Clicked!');
```

**8.2. MATLAB App Designer (Drag & Drop UI)**

1. Open MATLAB.

2. Type:

```
appdesigner
```

  

1. Create buttons, graphs, and callbacks.

---

**Conclusion**

  

**What You Learned in MATLAB Level 2:**

  

✅ **Advanced Matrix Operations & Linear Algebra**

✅ **Signal Processing & Fourier Transform (FFT)**

✅ **Machine Learning with MATLAB**

✅ **Image Processing & Computer Vision**

✅ **Simulink for System Modeling**

✅ **Optimization & Numerical Methods**

✅ **Parallel Computing & Performance Optimization**

✅ **Built a Full MATLAB Application**

  

Now, you’re ready for **MATLAB Level 3**, where we explore **Deep Learning, Hardware Interfacing (Arduino, Raspberry Pi), Financial Modeling, and Cloud Deployment!** 🚀