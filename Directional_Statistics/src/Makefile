all : standard before_perturb perturb after_perturb VMS new sym

before_perturb : 4D_ACG_Resample_Before_Perturb_Polar.png

perturb : 4D_ACG_Resample_Perturb_0.05_Polar.png 4D_ACG_Resample_Perturb_0.1_Polar.png 4D_ACG_Resample_Perturb_0.3_Polar.png 4D_ACG_Resample_Perturb_0.5_Polar.png 4D_ACG_Resample_Perturb_0.9_Polar.png

after_perturb : 4D_ACG_Resample_After_Perturb_0.05_Polar.png 4D_ACG_Resample_After_Perturb_0.5_Polar.png 4D_ACG_Resample_After_Perturb_0.7_Polar.png 4D_ACG_Resample_After_Perturb_0.75_Polar.png 4D_ACG_Resample_After_Perturb_0.8_Polar.png 4D_ACG_Resample_After_Perturb_0.9_Polar.png

standard : 4D_ACG_I.png 4D_ACG_5_1.png 4D_ACG_25_1.png 4D_ACG_125_1.png 4D_ACG_I_Polar.png 4D_ACG_5_1_Polar.png 4D_ACG_25_1_Polar.png 4D_ACG_125_1_Polar.png

new : ACG_1_5_5_5.png

sym : C15_2017-04-20_01.png \
	  O_2017-04-20_02.png \
	  O_2017-04-20_03.png \
	  O_2017-04-20_04.png \
	  C15_2017-04-20_05.png \
	  C15_2017-04-20_07.png \
	  C15_2017-04-20_08.png

ACG_1_5_5_5.png : Quaternion_Polar.py ../Data/ACG_1_5_5_5.txt
	python $^ "Distribition with Matrix [[1, 0, 0, 0], [0, 5, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]]"

VMS : PDF_VMS.png Sample_VMS.png Sample_VMS_Unit_Vector.png

4D_ACG_I.png : Quaternion.py ../Data/4D_ACG_I.txt
	python $^ "Distribition with Matrix [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_5_1.png : Quaternion.py ../Data/4D_ACG_5_1.txt
	python $^ "Distribition with Matrix [[5, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_25_1.png : Quaternion.py ../Data/4D_ACG_25_1.txt
	python $^ "Distribition with Matrix [[25, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_125_1.png : Quaternion.py ../Data/4D_ACG_125_1.txt
	python $^ "Distribition with Matrix [[125, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_I_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_I.txt
	python $^ "Distribition with Matrix [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_5_1_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_5_1.txt
	python $^ "Distribition with Matrix [[5, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_25_1_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_25_1.txt
	python $^ "Distribition with Matrix [[25, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_125_1_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_125_1.txt
	python $^ "Distribition with Matrix [[125, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]"

4D_ACG_Resample_Before_Perturb_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_Before_Perturb.txt
	python $^ "5% Global, 95% Single Point, Before Perturbation"

4D_ACG_Resample_Perturb_0.05_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_Perturb_0.05.txt
	python $^ "Perturbation of 5% Global, 95% Single Point"

4D_ACG_Resample_Perturb_0.1_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_Perturb_0.1.txt
	python $^ "Perturbation of 10% Global, 90% Single Point"

4D_ACG_Resample_Perturb_0.3_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_Perturb_0.3.txt
	python $^ "Perturbation of 30% Global, 70% Single Point"

4D_ACG_Resample_Perturb_0.5_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_Perturb_0.5.txt
	python $^ "Perturbation of 50% Global, 50% Single Point"

4D_ACG_Resample_Perturb_0.9_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_Perturb_0.9.txt
	python $^ "Perturbation of 90% Global, 10% Single Point"

4D_ACG_Resample_After_Perturb_0.05_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_After_Perturb_0.05.txt
	python $^ "5% Global, 95% Single Point, After Perturbation"

4D_ACG_Resample_After_Perturb_0.5_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_After_Perturb_0.5.txt
	python $^ "50% Global, 50% Single Point, After Perturbation"

4D_ACG_Resample_After_Perturb_0.7_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_After_Perturb_0.7.txt
	python $^ "70% Global, 30% Single Point, After Perturbation"

4D_ACG_Resample_After_Perturb_0.75_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_After_Perturb_0.75.txt
	python $^ "75% Global, 25% Single Point, After Perturbation"

4D_ACG_Resample_After_Perturb_0.8_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_After_Perturb_0.8.txt
	python $^ "80% Global, 20% Single Point, After Perturbation"

4D_ACG_Resample_After_Perturb_0.9_Polar.png : Quaternion_Polar.py ../Data/4D_ACG_Resample_After_Perturb_0.9.txt
	python $^ "90% Global, 10% Single Point, After Perturbation"

PDF_VMS.png : PDF_VMS.py ../Data/PDF_VMS.txt
	python $^

Sample_VMS.png : Sample_VMS.py ../Data/Sample_VMS.txt
	python $^

Sample_VMS_Unit_Vector.png : Sample_VMS_Unit_Vector.py ../Data/Sample_VMS_Unit_Vector.txt
	python $^

C15_2017-04-20_01.png : Quaternion_Polar.py ../Data/C15_2017-04-20_01.txt
	python $^ "C15_2017-04-20_01"

O_2017-04-20_02.png : Quaternion_Polar.py ../Data/O_2017-04-20_02.txt
	python $^ "O_2017-04-20_02"

O_2017-04-20_03.png : Quaternion_Polar.py ../Data/O_2017-04-20_03.txt
	python $^ "O_2017-04-20_03"

O_2017-04-20_04.png : Quaternion_Polar.py ../Data/O_2017-04-20_04.txt
	python $^ "O_2017-04-20_04"

C15_2017-04-20_05.png : Quaternion_Polar.py ../Data/C15_2017-04-20_05.txt
	python $^ "C15_2017-04-20_05"

C15_2017-04-20_07.png : Quaternion_Polar.py ../Data/C15_2017-04-20_07.txt
	python $^ "C15_2017-04-20_07"

C15_2017-04-20_08.png : Quaternion_Polar.py ../Data/C15_2017-04-20_08.txt
	python $^ "C15_2017-04-20_08"
