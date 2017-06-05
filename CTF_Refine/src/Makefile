all : ../Figures/CTF_Refine_2017-02-28_06.png \
      ../Figures/CTF_Refine_2017-02-28_08.png \
	  ../Figures/CTF_Refine_Compare_2017-02-28_06_08.png \
	  ../Figures/Particle_Grading_Compare_2017-02-28_08_09.png \
	  ../Figures/CTF_Refine_2017-02-28_10.png \
	  ../Figures/CTF_Refine_2017-03-01_01.png \
	  ../Figures/CTF_Refine_2017-03-02_02.png \
      ../Figures/Comparison_2017-03-02_02_VS_2017-02-26_04.png \
	  ../Figures/CTF_Refine_2017-03-02_12.png \
	  ../Figures/Particle_Grading_Compare_2017-03-02_11_12.png \
	  ../Figures/CTF_Refine_2017-03-03_02.png \
      ../Figures/CTF_Refine_2017-03-02_09_VS_2017-03-03_02.png \
	  ../Figures/CTF_Refine_2017-03-04_10.png \
      ../Figures/CTF_Refine_2017-03-05_01.png \
	  ../Figures/CTF_Refine_2017-03-05_06_VS_2017-03-05_07.png \
	  ../Figures/Particle_Grading_Compare_2017-03-05_08_09.png \
	  ../Figures/Compare_RELION_2017-03-06_02.png \
	  ../Figures/Compare_RELION_2017-03-06_04.png \
	  ../Figures/Compare_RELION_Unmasked_2017-03-06_04.png \
	  ../Figures/Compare_RELION_Unmasked_2017-03-06_06.png \
	  ../Figures/Particle_Grading_Unmasked_2017-03-06_06_08.png \
      ../Figures/CTF_Refinement_Unmasked_2017-03-06_06_09.png \
      ../Figures/Particle_Filter_Based_Unmasked_2017-03-06_08_09.png \
      ../Figures/Grid_Correction_Unmasked_2017-03-23_06_07.png \
      ../Figures/Grid_Correction_Unmasked_2017-03-23_06_08.png \
      ../Figures/CTF_Refine_2017-04-09_12.png \
	  ../Figures/CTF_Refine_2017-04-10_01.png \
	  ../Figures/CTF_Refine_2017-04-10_05.png \
	  ../Figures/CTF_Refine_2017-06-01_01.png \
	  ../Figures/CTF_Refine_RF_2017-06-05.png

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

../Figures/CTF_Refine_2017-03-02_12.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-03-02_12.txt \
	                                      ../Data/CTF_Refine_001_2017-03-02_12.txt \
	                                      ../Data/CTF_Refine_002_2017-03-02_12.txt \
	                                      ../Data/CTF_Refine_003_2017-03-02_12.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"

../Figures/Particle_Grading_Compare_2017-03-02_11_12.png : FSC_Compare.py \
	                                                       ../Data/FSC_Final_2017-03-02_11.txt \
	                                                       ../Data/FSC_Final_2017-03-02_12.txt
	python $^ $@ "Without CTF Refine" \
		         "With CTF Refine" \
				 "Comparsion Between CTF Refine or Not"

../Figures/CTF_Refine_2017-03-03_02.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-03-02_02.txt \
	                                      ../Data/CTF_Refine_001_2017-03-02_02.txt \
	                                      ../Data/CTF_Refine_002_2017-03-02_02.txt \
	                                      ../Data/CTF_Refine_003_2017-03-02_02.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"

../Figures/CTF_Refine_2017-03-02_09_VS_2017-03-03_02.png : FSC_Compare.py \
	                                                       ../Data/FSC_Final_2017-03-02_09.txt \
	                                                       ../Data/FSC_Final_2017-03-03_02.txt
	python $^ $@ "Without CTF Refine" \
		         "With CTF Refine" \
				 "Comparsion Between CTF Refine or Not"

../Figures/CTF_Refine_2017-03-04_10.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-03-04_10.txt \
	                                      ../Data/CTF_Refine_001_2017-03-04_10.txt \
	                                      ../Data/CTF_Refine_002_2017-03-04_10.txt \
	                                      ../Data/CTF_Refine_003_2017-03-04_10.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"

../Figures/CTF_Refine_2017-03-05_01.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-03-05_01.txt \
	                                      ../Data/CTF_Refine_001_2017-03-05_01.txt \
	                                      ../Data/CTF_Refine_002_2017-03-05_01.txt \
	                                      ../Data/CTF_Refine_003_2017-03-05_01.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"

../Figures/CTF_Refine_2017-03-05_06_VS_2017-03-05_07.png : FSC_Compare.py \
	                                                       ../Data/FSC_Round_018_2017-03-05_06.txt \
	                                                       ../Data/FSC_Round_018_2017-03-05_07.txt
	python $^ $@ "CTF Refine" \
		         "Without CTF Refine" \
				 "Comparsion Between CTF Refine or Not"

../Figures/Particle_Grading_Compare_2017-03-05_08_09.png : FSC_Compare.py \
	                                                       ../Data/FSC_Final_2017-03-05_08.txt \
	                                                       ../Data/FSC_Final_2017-03-05_09.txt
	python $^ $@ "Without Particle Grading" \
		         "With Particle Grading" \
				 "Comparsion Between Particle Grading or Not"

../Figures/Compare_RELION_2017-03-06_02.png : FSC_Compare_RELION.py \
	                                          ../Data/C4_RELION_FSC.txt \
											  ../Data/FSC_Final_2017-03-06_02.txt
	python $^ $@ "RELION" \
		         "Particle Grading" \
				 "C4, 80K+, Compare with RELION with Particle Grading"

../Figures/Compare_RELION_2017-03-06_04.png : FSC_Compare_RELION.py \
	                                          ../Data/C4_RELION_FSC.txt \
											  ../Data/FSC_Final_2017-03-06_04.txt
	python $^ $@ "RELION" \
		         "Particle Grading" \
				 "C4, 80K+, Compare with RELION with Particle Grading"

../Figures/Compare_RELION_Unmasked_2017-03-06_04.png : FSC_Compare_RELION_Unmasked.py \
	                                                   ../Data/C4_RELION_FSC.txt \
											           ../Data/FSC_Final_Unmasked_2017-03-06_04.txt
	python $^ $@ "RELION" \
		         "Particle Grading" \
				 "C4, 80K+, Compare with RELION with Particle Grading"

../Figures/Compare_RELION_Unmasked_2017-03-06_06.png : FSC_Compare_RELION_Unmasked.py \
	                                                   ../Data/C4_RELION_FSC.txt \
											           ../Data/FSC_Final_Unmasked_2017-03-06_06.txt
	python $^ $@ "RELION" \
		         "Particle Grading" \
				 "C4, 80K+, Compare with RELION with Particle Grading"

../Figures/Particle_Grading_Unmasked_2017-03-06_06_08.png : FSC_Compare.py \
											                ../Data/FSC_Final_Unmasked_2017-03-06_06.txt \
											                ../Data/FSC_Final_Unmasked_2017-03-06_08.txt
	python $^ $@ "+ Particle Grading" \
		         "- Particle Grading" \
			     "FSC Comparison between Particle or Not"
	
../Figures/CTF_Refinement_Unmasked_2017-03-06_06_09.png : FSC_Compare.py \
						                                  ../Data/FSC_Final_Unmasked_2017-03-06_06.txt \
											              ../Data/FSC_Final_Unmasked_2017-03-06_09.txt
	python $^ $@ "- CTF Refinement" \
		         "+ CTF Refinement" \
				 "FSC Comparison between CTF Refinement or Not"

../Figures/Particle_Filter_Based_Unmasked_2017-03-06_08_09.png : FSC_Compare.py \
						                                          ../Data/FSC_Final_Unmasked_2017-03-06_08.txt \
									          		              ../Data/FSC_Final_Unmasked_2017-03-06_09.txt
	python $^ $@ "- CTF Refinement - Particle Grading" \
		         "+ CTF Refinement + Particle Grading" \
			 	 "FSC Comparison"
	
../Figures/Grid_Correction_Unmasked_2017-03-23_06_07.png : FSC_Compare.py \
						                                          ../Data/FSC_Final_Unmasked_2017-03-23_06.txt \
									          		              ../Data/FSC_Final_Unmasked_2017-03-23_07.txt
	python $^ $@ "WT" \
		         "Divide Kernel in Real Space" \
				 "Grid Correction Comparison"
	
../Figures/Grid_Correction_Unmasked_2017-03-23_06_08.png : FSC_Compare.py \
						                                          ../Data/FSC_Final_Unmasked_2017-03-23_06.txt \
									          		              ../Data/FSC_Final_Unmasked_2017-03-23_08.txt
	python $^ $@ "WT" \
		         "Multiple Kernel in Real Space" \
		         "Grid Correction Comparison"
		
../Figures/CTF_Refine_2017-04-09_12.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-04-09_12.txt \
	                                      ../Data/CTF_Refine_001_2017-04-09_12.txt \
	                                      ../Data/CTF_Refine_002_2017-04-09_12.txt \
	                                      ../Data/CTF_Refine_003_2017-04-09_12.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"
		
../Figures/CTF_Refine_2017-04-10_01.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-04-10_01.txt \
	                                      ../Data/CTF_Refine_001_2017-04-10_01.txt \
	                                      ../Data/CTF_Refine_002_2017-04-10_01.txt \
	                                      ../Data/CTF_Refine_003_2017-04-10_01.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"
			
../Figures/CTF_Refine_2017-04-10_05.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-04-10_05.txt \
	                                      ../Data/CTF_Refine_001_2017-04-10_05.txt \
	                                      ../Data/CTF_Refine_002_2017-04-10_05.txt \
	                                      ../Data/CTF_Refine_003_2017-04-10_05.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"
		
../Figures/CTF_Refine_2017-06-01_01.png : FSC_Compare_4.py \
	                                      ../Data/CTF_Refine_000_2017-06-01_01.txt \
	                                      ../Data/CTF_Refine_001_2017-06-01_01.txt \
	                                      ../Data/CTF_Refine_002_2017-06-01_01.txt \
	                                      ../Data/CTF_Refine_003_2017-06-01_01.txt
	python $^ $@ "Comparison Between CTF Refine or Not" \
		         "Before CTF Refine" \
				 "CTF Refine Round 1" \
				 "CTF Refine Round 2" \
				 "CTF Refine Round 3"

../Figures/CTF_Refine_RF_2017-06-05.png : FSC_Compare_7.py \
	                                      ../Data/CTF_Refine_Before_Refine_2017-06-05.txt \
										  ../Data/CTF_Refine_RF_1_2017-06-05.txt \
										  ../Data/CTF_Refine_RF_2_2017-06-05.txt \
										  ../Data/CTF_Refine_RF_3_2017-06-05.txt \
										  ../Data/CTF_Refine_RF_4_2017-06-05.txt \
										  ../Data/CTF_Refine_RF_5_2017-06-05.txt \
										  ../Data/CTF_Refine_RF_10_2017-06-05.txt
	python $^ $@ "Comparison Various Defocus Factor" \
	             "Before CTF Refine" \
				 "CTF Refine Factor = 1" \
				 "CTF Refine Factor = 2" \
				 "CTF Refine Factor = 3" \
				 "CTF Refine Factor = 4" \
				 "CTF Refine Factor = 5" \
				 "CTF Refine Factor = 10" \


clean :
	rm ../Figures/*.png
