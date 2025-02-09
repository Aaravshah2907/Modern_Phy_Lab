python3 calculations.py
gnuplot -p experiment2_graph.gp < original_readings.csv
qlmanage -t -s 1000 -o . Experimental_graph.svg
cp Experimental_graph.svg.png Experimental_graph.png
rm Experimental_graph.svg.png