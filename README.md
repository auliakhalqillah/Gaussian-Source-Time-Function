# Gaussian Source Time Function
The gaussian function is

![gaussian equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/13993a37c117176295fada7cdaa9c1ef1ae769f7)

where the

```
a = height of the curve's peak (standard deviation)
b = mean
c = a --> c^2 = variance
```

If we apply the gaussian function to the time function, it can be written

![gaussian equation 2](https://latex.codecogs.com/png.latex?f%28t%29%20%3D%20a%20%5Ccdot%20%5Cexp%5Cleft%28-%5Cfrac%7B%28t-tdom%29%5E2%7D%7Bc%5E2%7D%20%5Cright%29%20%3D%20a%20%5Ccdot%20%5Cexp%5Cleft%28-%5Cfrac%7B%28t-tdom%29%5E2%7D%7Ba%5E2%7D%20%5Cright%29)

where the 

 ```
 a = 1/Tdom or Fdom
 t0 = Tdom
 c = a
 ```
 
 Tdom is dominant period and Fdom is dominant frequency.
 
 The first derivative of gaussian function can be written
 
 ![gaussian equation 3](https://latex.codecogs.com/png.latex?f%27%28t%29%20%3D%20%5Cfrac%7B-2%28t-tdom%29%7D%7Ba%7D%20%5Cexp%20%5Cleft%20%28%20%5Cfrac%7B-%28t-tdom%29%5E2%7D%7Ba%5E2%7D%20%5Cright%20%29)
 
 # Simulation
 We silumate the gaussian source time function by using some parameters bellow
 
 ```
 n = 1000
 mint = 0
 maxt = 5
 dt = (maxt-mint)/n
 fdom = 5
 tdom = 2.5
 a = 1/tdom
 ```
 
 the result of gaussian source time function is
 
 ![simulation](https://github.com/auliakhalqillah/Gaussian-Source-Time-Function/blob/main/Gaussian_Source_Time_Fucntion.png)
 
 the orange line is the original gaussian function and the blue line is first derivative of gaussian function
 
 # Contact
 email: auliakhalqillah.mail@gmail.com
