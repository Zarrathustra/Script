all : 4D_ACG_I.png 4D_ACG_5_1.png 4D_ACG_I_Polar.png 4D_ACG_5_1_Polar.png

4D_ACG_I.png : Quaternion.py ../Data/4D_ACG_I.txt
	python $^ "Distribition with Matrix [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_5_1.png : Quaternion.py ../Data/4D_ACG_5_1.txt
	python $^ "Distribition with Matrix [[5, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_I_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_I.txt
	python $^ "Distribition with Matrix [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_5_1_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_5_1.txt
	python $^ "Distribition with Matrix [[5, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"
