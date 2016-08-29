all : ../Figures/FSC_5000_10x_Low_Ref.png \
	  ../Figures/FSC_40000_10x_Low_Ref.png \
	  ../Figures/FSC_5000_10x_High_Ref.png

../Figures/FSC_5000_10x_Low_Ref.png : FSC.py ../Data/FSC_5000_10x_Low_Ref.txt
	python FSC.py ../Data/FSC_5000_10x_Low_Ref.txt

../Figures/FSC_40000_10x_Low_Ref.png : FSC.py ../Data/FSC_40000_10x_Low_Ref.txt
	python FSC.py ../Data/FSC_40000_10x_Low_Ref.txt

../Figures/FSC_5000_10x_High_Ref.png : FSC.py ../Data/FSC_5000_10x_High_Ref.txt
	python FSC.py ../Data/FSC_5000_10x_High_Ref.txt

clean :
	rm ../Figures/*.png
