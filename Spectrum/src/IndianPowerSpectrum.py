import Image # port py27-pil needed

size = 1000

indian = Image.open("../Figures/Indian.bmp")
indian = indian.resize((size, size))

spectrum = Image.open("../Figures/Spectrum.png")
spectrum = spectrum.resize((2 * size, size))

result = Image.new("L", (3 * size, size))

result.paste(indian, (0, 0))
result.paste(spectrum, (size, 0))

result.save("../Figures/IndianPowerSpectrum.png");
