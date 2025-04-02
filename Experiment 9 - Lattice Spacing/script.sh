gnuplot -p experiment9_mono.gp < original_data.csv
qlmanage -t -s 1000 -o . Experimental_mono.svg
cp Experimental_mono.svg.png Experimental_mono.png
rm Experimental_mono.svg.png
gnuplot -p experiment9_di.gp < original_data.csv
qlmanage -t -s 1000 -o . Experimental_di.svg
cp Experimental_di.svg.png Experimental_di.png
rm Experimental_di.svg.png