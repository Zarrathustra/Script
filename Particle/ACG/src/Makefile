all : AngleC1.png \
	  AngleC15.png \
	  QuaternionC15.png

AngleC1.png : ../Data/AngleC1.txt Angle_Polar.py
	python Angle_Polar.py ../Data/AngleC1.txt

AngleC15.png : ../Data/AngleC15.txt Angle_Polar.py
	python Angle_Polar.py ../Data/AngleC15.txt

QuaternionC15.png : ../Data/QuaternionC15.par Quaternion_Polar.py
	python Quaternion_Polar.py ../Data/QuaternionC15.par
