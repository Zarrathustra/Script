all : ../Figures/CTF_Refine_2017-02-28_06.png \
      ../Figures/CTF_Refine_2017-02-28_08.png \
	  ../Figures/CTF_Refine_Compare_2017-02-28_06_08.png \
	  ../Figures/Particle_Grading_Compare_2017-02-28_08_09.png \
	  ../Figures/CTF_Refine_2017-02-28_10.png \
	  ../Figures/CTF_Refine_2017-03-01_01.png \
	  ../Figures/CTF_Refine_2017-03-02_02.png \
      ../Figures/Comparison_2017-03-02_02_VS_2017-02-26_04.png

../Figures/CTF_Refine_2017-02-28_06.png : FSC_Compare.py \
	                                      ../Data/CTF_Refine_000_2017-02-28_06.txt \
				 		                  ../Data/CTF_Refine_001_2017-02-28_06.txt
	python $^ $@ "Before CTF Refine" \
		         "CTF Refine Round 1" \
				 "CTF Refine Perturbation Factor = 0.5, Standard Deviation = 0.005"

../Figures/CTF_Refine_2017-02-28_08.png : FSC_Compare.py \
	                                      ../Data/CTF_Refine_000_2017-02-28_08.txt \
				 		                  ../Data/CTF_Refine_001_2017-02-28_08.txt
	python $^ $@ "Before CTF Refine" \
		         "CTF Refine Round 1" \
				 "CTF Refine Perturbation Factor = 0.5, Standard Deviation = 0"
 
../Figures/CTF_Refine_Compare_2017-02-28_06_08.png : FSC_Compare_4.py \
	                                                 ../Data/CTF_Refine_000_2017-02-28_06.txt \
	                                                 ../Data/CTF_Refine_001_2017-02-28_06.txt \
			 		                                 ../Data/CTF_Refine_000_2017-02-28_08.txt \
				 		                             ../Data/CTF_Refine_001_2017-02-28_08.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine, sigma = 0.005" \
		         "CTF Refine Round 1, sigma = 0.005" \
		         "Before CTF Refine, sigma = 0" \
		         "CTF Refine Round 1, sigma = 0"

../Figures/Particle_Grading_Compare_2017-02-28_08_09.png : FSC_Compare.py \
	                                                       ../Data/FSC_2017-02-28_08.txt \
	                                                       ../Data/FSC_2017-02-28_09.txt
	python $^ $@ "Without Particle Grading" \
		         "With Particle Grading" \
				 "Comparsion Between Particle Grading or Not"

../Figures/CTF_Refine_2017-02-28_10.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-02-28_10.txt \
	                                      ../Data/CTF_Refine_001_2017-02-28_10.txt \
			 		                      ../Data/CTF_Refine_002_2017-02-28_10.txt \
				 		                  ../Data/CTF_Refine_003_2017-02-28_10.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"

../Figures/CTF_Refine_2017-03-01_01.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-03-01_01.txt \
	                                      ../Data/CTF_Refine_001_2017-03-01_01.txt \
	                                      ../Data/CTF_Refine_002_2017-03-01_01.txt \
	                                      ../Data/CTF_Refine_003_2017-03-01_01.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"

../Figures/CTF_Refine_2017-03-02_02.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-03-02_02.txt \
	                                      ../Data/CTF_Refine_001_2017-03-02_02.txt \
	                                      ../Data/CTF_Refine_002_2017-03-02_02.txt \
	                                      ../Data/CTF_Refine_003_2017-03-02_02.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"

../Figures/Comparison_2017-03-02_02_VS_2017-02-26_04.png : FSC_Compare.py \
	                                                    ../Data/FSC_Final_2017-03-02_02.txt \
	                                                    ../Data/FSC_Final_2017-02-26_04.txt
	python $^ $@ "With Particle Grading & CTF Refine" \
		         "Without Particle Grading & CTF Refine" \
				 "Comparison Between Particle Grading & CTF Refine or Not"
