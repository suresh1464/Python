def Total_Cylinder_volume(radius,height): # Assign default value for height =7 if you dont supply height value it will take default else it will take whatever we supply
     volume = 0
     print("Radius is :",radius)
     print("Height is :",height)
     volume = 3.14*(radius**2)*height # pir**2*h
     #print("Volume is :",volume)
     return volume

r = 10
h = 7

vol  = Total_Cylinder_volume(r,h)   # Positional Arguments
vol1 = Total_Cylinder_volume(h,r)  # If we give wrong arguments it will change whole value
vol2 = Total_Cylinder_volume(height=h,radius=r)  # Keyword arguments. Event order is different but keyword specification is correct it will give right value
print("Total Volume is:",vol)
print("Total Volume is:",vol1)
print("Total Volume is:",vol2)
